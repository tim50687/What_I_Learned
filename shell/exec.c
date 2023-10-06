#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <readline/readline.h>
#include <readline/history.h>

// Basic execvp
// int main()
// {

//     char *argv[] = {"ls", "-alh", NULL};
//     execvp(argv[0], argv);
// }

// Combine with fork

char **get_input(char *);
int cd(char *path);

int main()
{
    char **command;
    char *input;
    pid_t child_pid;
    int stat_loc;

    while (1)
    {
        input = readline("unixsh> ");
        command = get_input(input);

        if (!command[0])
        { /* Handle empty commands */
            free(input);
            free(command);
            continue;
        }
        // cd command
        if (strcmp(command[0], "cd") == 0)
        {
            if (cd(command[1]) < 0)
            {
                perror(command[1]);
            }
            continue;
        }

        child_pid = fork();
        if (child_pid < 0)
        {
            perror("Fork failed");
            exit(1);
        }

        if (child_pid == 0)
        {
            /* Never returns if the call is successful */
            if (execvp(command[0], command) < 0)
            {
                perror(command[0]);
                exit(1);
            }
        }
        else
        {
            waitpid(child_pid, &stat_loc, WUNTRACED);
        }

        free(input);
        free(command);
    }

    return 0;
}

char **get_input(char *input)
{
    char **command = malloc(8 * sizeof(char *));
    if (command == NULL)
    {
        perror("malloc failed");
        exit(1);
    }

    char *separator = " ";
    char *parsed;
    int index = 0;

    parsed = strtok(input, separator);
    while (parsed != NULL)
    {
        command[index] = parsed;
        index++;

        parsed = strtok(NULL, separator);
    }

    command[index] = NULL;
    return command;
}

int cd(char *path)
{
    return chdir(path);
}