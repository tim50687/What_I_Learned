# Example
- `{genres: 'Drama'}` : Find all movies with the genre Drama. Even if genres is an array, it will still work.

- `{genres: 'Drama', type: "movie"}` : Find all movies with the genre Drama and type movie. Logical AND.

- `{type: "movie" ,$or:[{genres: "Drama"}, {genres: "History"}]}` : Find all movies with the genre Drama or History. Logical OR.

- `{type: "movie", genres: {$all: ["Drama", "History"]}}` : Find all movies with the genre Drama and History.
    - You can use `$all` to find all documents with an array that contains all the elements in the query.

- `{type: "movie", genres: {$size:2}}` : Find all movies with 2 genres. genres is an array.

- `{"imdb.id": {$gte:20000, $lte:40000}}` : Find all documents with an imdb id between 20000 and 40000.
    - `imdb.id` is a nested field. It is an object with a field id.

- `{"tomatoes.boxOffice": "$6.6M", type: "movie"}` : Find all movies with a tomatoes boxOffice field equal to $6.6M.
    - `tomatoes.boxOffice` is a nested field. It is an object with a field boxOffice.

- `{ "tomatoes.critic.rating": { $exists: true } }` : Find all documents that have a tomatoes.critic.rating field.
    - `tomatoes.critic.rating` is a nested field. It is an object with a field rating.

- `{ "tomatoes.critic.rating": {$gte: 6, $lte: 8} }` : Find all documents that have a tomatoes.critic.rating field between 6 and 8.
    - `tomatoes.critic.rating` is a nested field. It is an object with a field rating.

- `{fullplot: null}` : see if a field is null or missing.



# HW 9

-  `{"address.market": {$in: ["Hong Kong", "New York", "Porto", "Sydney", "Istanbul"]}}` : Find all documents with an address.market field equal to Hong Kong, New York, Porto, Sydney or Istanbul.
    - `address.market` is a nested field. It is an object with a field market.