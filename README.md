# twitch-pyql

Twitch's Typed, Annotated GraphQL operations

[`endpoints.py`](endpoints.py) should provide you a representation of twitch's GraphQL operations, with a fully typed requests and responses. At the time you read, it's a v2 version of generated endpoints

If there are any uncovered keys - they are Dict/List type, which can be marked as `Falsy[List[Any]]`

Note that `Falsy` type comes from my [`sputchedtools`](https://pypi.org/project/sputchedtools) module

> [!CAUTION]
> Pythons blacklisted keywords are changed to add underscore `_` at the end. In a line that contains this key, there will be comment at the end: `# WARNING: ADDED UNDERSCORE`

> [!NOTE]
> `endpoints.py` will be updated to most up-to-date whenever i feel like, it can be either an hour or a month. For latest changes, `Promises` implementation (with all caviats), dm https://t.me/reddyy0x

Example:

```python
from endpoints import VideoCommentsByOffsetOrCursor, VideoCommentsByOffsetOrCursorResponse

# Request is typed
payload: dict = VideoCommentsByOffsetOrCursor.build_query({'videoId': ..., 'contentOffsetSeconds': ...})
payload: dict = VideoCommentsByOffsetOrCursor.build_query({'videoId': ..., 'cursor': ...})

response: VideoCommentsByOffsetOrCursorResponse = promises.add(payload)
# Fully typed path
response['video']['comments']['edges'][0]['node']['message']['fragments'][0]['text']
