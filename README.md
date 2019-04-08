# BotBrain Server
Heroku based API server

## API Documentation

Base URL - Get from Heroku after hosting. And use the following endpoints

1. `/` - Show the plain server information
2. `/lists` - Based on the query parameter of `id`, the appropriate list number is returned. If no `id` is given, this endpoint returns all the list names as an array.
3. `/products` - Returns a list of all the available products in the shop
4. `/botNav` - This is the API endpoint which manages a bot session. This endpoint takes a query parameter, `list` which is the list number to compute the path for. The first request returns `Follow Bot` after computing the path which can be obtained from `/getPath`, and any subsequent requests before the particular session has ended returns `Session Underway`. To end the session, see `/endSession`. GET this endpoint to 
5. `/getPath` - GET this after calling `/botNav` (from the bot preferably) to get a sequence of commands as a json string, which can be parsed and used by the bot.
6. `/endSession` - Endpoint for the bot to indicate the termination of a session, thereby ensuring successful completion of a session.
7. `/appCont` - This endpoint is used from the app to signal the bot to continue onward.
8. `/test`,`/testinit`,`/testcont` - Testing endpoints for testing integration of the server with the bot
