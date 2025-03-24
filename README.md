# twitch-pyql

Twitch's Typed, Annotated GraphQL operations

This library provides representation of request/responses types within all endpoints used when surfing through https://twitch.tv. Type definitions are automatically generated and **may not represent all possible types**, but gives you a better experience extracting response keys.

Example:

```python
from endpoints import VideoCommentsByOffsetOrCursor, VideoCommentsByOffsetOrCursorResponse

# Request is typed
payload: dict = VideoCommentsByOffsetOrCursor.build_query({'videoId': ..., 'contentOffsetSeconds': ...})
payload: dict = VideoCommentsByOffsetOrCursor.build_query({'videoId': ..., 'cursor': ...})

response: VideoCommentsByOffsetOrCursorResponse = promises.add(payload)
# Fully typed path
response['video']['comments']['edges'][0]['node']['message']['fragments'][0]['text']