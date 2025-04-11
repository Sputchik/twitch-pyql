from typing import Dict, TypedDict, List, Any, Union
from types import NoneType
from sptz import Falsy


__all__ = [
	"Endpoint",
	"Endpoints",

	"AccessGetFeatureClipRestrictionsQueryRequest",
	"AccessGetFeatureClipRestrictionsQueryResponse",
	"AcknowledgeUnbanRequestPromptRequest",
	"AcknowledgeUnbanRequestPromptResponse",
	"AvailableEmotesForChannelPaginatedRequest",
	"AvailableEmotesForChannelPaginatedResponse",
	"BlockedUsersRequest",
	"BlockedUsersResponse",
	"BrowsePage_AllDirectoriesRequest1",
	"BrowsePage_AllDirectoriesRequest2",
	"BrowsePage_AllDirectoriesResponse",
	"BrowseVerticalDirectoryRequest",
	"BrowseVerticalDirectoryResponse",
	"CanCreateClipRequest",
	"CanCreateClipResponse",
	"CanViewersExportQueryRequest",
	"CanViewersExportQueryResponse",
	"ChannelAvatarRequest",
	"ChannelAvatarResponse",
	"ChannelClipCoreRequest",
	"ChannelClipCoreResponse",
	"ChannelCollaborationEligibilityQueryRequest",
	"ChannelCollaborationEligibilityQueryResponse",
	"ChannelLeaderboardsRequest",
	"ChannelLeaderboardsResponse",
	"ChannelPage_SetSessionStatusRequest",
	"ChannelPage_SetSessionStatusResponse",
	"ChannelPage_SubscribeButton_UserRequest1",
	"ChannelPage_SubscribeButton_UserRequest2",
	"ChannelPage_SubscribeButton_UserResponse",
	"ChannelPointsContextRequest",
	"ChannelPointsContextResponse",
	"ChannelPointsGlobalContextRequest",
	"ChannelPointsGlobalContextResponse",
	"ChannelPointsPredictionContextRequest",
	"ChannelPointsPredictionContextResponse",
	"ChannelShellRequest",
	"ChannelShellResponse",
	"ChannelSkinsRequest",
	"ChannelSkinsResponse",
	"ChannelSocialButtonsRequest",
	"ChannelSocialButtonsResponse",
	"ChannelSupportButtonsRequest",
	"ChannelSupportButtonsResponse",
	"ChannelVideoCoreRequest",
	"ChannelVideoCoreResponse",
	"ChannelVideoShelvesQueryRequest",
	"ChannelVideoShelvesQueryResponse",
	"ChatClipRequest",
	"ChatClipResponse",
	"ChatFilterContextManager_UserRequest",
	"ChatFilterContextManager_UserResponse",
	"ChatInputRequest",
	"ChatInputResponse",
	"ChatInput_BadgesRequest",
	"ChatInput_BadgesResponse",
	"ChatList_BadgesRequest",
	"ChatList_BadgesResponse",
	"ChatModeratorStrikeStatusRequest",
	"ChatModeratorStrikeStatusResponse",
	"ChatRestrictionsRequest",
	"ChatRestrictionsResponse",
	"ChatRoomBanStatusRequest",
	"ChatRoomBanStatusResponse",
	"ChatRoomStateRequest",
	"ChatRoomStateResponse",
	"ChatScreenReaderAutoAnnounceRequest",
	"ChatScreenReaderAutoAnnounceResponse",
	"Chat_ChannelDataRequest",
	"Chat_ChannelDataResponse",
	"Chat_EarnedBadges_InitialSubStatusRequest",
	"Chat_EarnedBadges_InitialSubStatusResponse",
	"Chat_OrbisPresetTextRequest",
	"Chat_OrbisPresetTextResponse",
	"Chat_ShareResub_ChannelDataRequest",
	"Chat_ShareResub_ChannelDataResponse",
	"Chat_UserDataRequest",
	"Chat_UserDataResponse",
	"ClaimCommunityPointsRequest",
	"ClaimCommunityPointsResponse",
	"ClipMetadataRequest",
	"ClipMetadataResponse",
	"ClipsCards__UserRequest",
	"ClipsCards__UserResponse",
	"ClipsExperimentEnrollmentStatusRequest",
	"ClipsExperimentEnrollmentStatusResponse",
	"CollectionCarouselQueryRequest",
	"CollectionCarouselQueryResponse",
	"CommercialCommandHandler_ChannelDataRequest",
	"CommercialCommandHandler_ChannelDataResponse",
	"CommonHooks_BlockedUsersRequest",
	"CommonHooks_BlockedUsersResponse",
	"CommunityOnboardingAllowlistRequest",
	"CommunityOnboardingAllowlistResponse",
	"CommunityPointsAvailableClaimRequest",
	"CommunityPointsAvailableClaimResponse",
	"CommunityPointsChatPrivateCalloutUserRequest",
	"CommunityPointsChatPrivateCalloutUserResponse",
	"CommunitySupportSettingsRequest",
	"CommunitySupportSettingsResponse",
	"ConsentRequest",
	"ConsentResponse",
	"ContentClassificationContextRequest1",
	"ContentClassificationContextRequest2",
	"ContentClassificationContextRequest3",
	"ContentClassificationContextResponse1",
	"ContentClassificationContextResponse2",
	"ContentClassificationContextResponse3",
	"ContentPolicyPropertiesQueryRequest",
	"ContentPolicyPropertiesQueryResponse1",
	"ContentPolicyPropertiesQueryResponse2",
	"CoreActionsCurrentUserRequest",
	"CoreActionsCurrentUserResponse",
	"CurrentUserBannedStatusRequest",
	"CurrentUserBannedStatusResponse",
	"CurrentUserModeratorStatusRequest1",
	"CurrentUserModeratorStatusRequest2",
	"CurrentUserModeratorStatusResponse",
	"CurrentUserStrikeStatusRequest",
	"CurrentUserStrikeStatusResponse",
	"DirectoryCollection_BrowsableCollectionRequest1",
	"DirectoryCollection_BrowsableCollectionRequest2",
	"DirectoryCollection_BrowsableCollectionResponse",
	"DropCurrentSessionContextRequest",
	"DropCurrentSessionContextResponse",
	"DropsHighlightService_AvailableDropsRequest",
	"DropsHighlightService_AvailableDropsResponse",
	"EmotesForChannelFollowStatusRequest",
	"EmotesForChannelFollowStatusResponse",
	"FeaturedClipsShelfCoverRequest",
	"FeaturedClipsShelfCoverResponse",
	"FeaturedContentCarouselStreamsRequest",
	"FeaturedContentCarouselStreamsResponse",
	"FilterableVideoTower_VideosRequest1",
	"FilterableVideoTower_VideosRequest2",
	"FilterableVideoTower_VideosResponse",
	"FollowButton_FollowUserRequest",
	"FollowButton_FollowUserResponse",
	"FollowButton_UnfollowUserRequest",
	"FollowButton_UnfollowUserResponse",
	"FollowButton_UserRequest",
	"FollowButton_UserResponse",
	"FollowedIndex_CurrentUserRequest",
	"FollowedIndex_CurrentUserResponse",
	"FollowedIndex_FollowCountRequest",
	"FollowedIndex_FollowCountResponse",
	"FollowedStreamsContinueWatchingRequest",
	"FollowedStreamsContinueWatchingResponse",
	"FollowedStreamsRequest",
	"FollowedStreamsResponse",
	"FollowedVideos_CurrentUserRequest",
	"FollowedVideos_CurrentUserResponse",
	"FollowingGames_CurrentUserRequest",
	"FollowingGames_CurrentUserResponse",
	"FollowingLive_CurrentUserRequest",
	"FollowingLive_CurrentUserResponse",
	"FollowingPage_RecommendedChannelsRequest",
	"FollowingPage_RecommendedChannelsResponse",
	"FrontPageNew_UserRequest",
	"FrontPageNew_UserResponse",
	"GetDisplayNameRequest",
	"GetDisplayNameResponse",
	"GetGuestSessionBlocksAndBansRequest",
	"GetGuestSessionBlocksAndBansResponse",
	"GetIDFromLoginRequest",
	"GetIDFromLoginResponse",
	"GetPinnedChatRequest",
	"GetPinnedChatResponse",
	"GetUserIDRequest",
	"GetUserIDResponse",
	"GlobalBadgesRequest",
	"GlobalBadgesResponse",
	"GuestListQueryRequest",
	"GuestListQueryResponse",
	"GuestStarActiveJoinRequestRequest",
	"GuestStarActiveJoinRequestResponse",
	"GuestStarBatchCollaborationQueryRequest",
	"GuestStarBatchCollaborationQueryResponse",
	"GuestStarChannelPageCollaborationQueryRequest",
	"GuestStarChannelPageCollaborationQueryResponse",
	"HappeningNowSettingsRequest",
	"HappeningNowSettingsResponse",
	"HomeOfflineCarouselRequest",
	"HomeOfflineCarouselResponse",
	"HomeShelfEditorRequest",
	"HomeShelfEditorResponse",
	"HomeShelfGamesRequest",
	"HomeShelfGamesResponse",
	"HomeShelfUsersRequest",
	"HomeShelfUsersResponse",
	"HomeShelfVideosRequest",
	"HomeShelfVideosResponse",
	"LastUnbanRequestRequest",
	"LastUnbanRequestResponse",
	"LowerHomeHeaderRequest",
	"LowerHomeHeaderResponse",
	"MessageBufferChatHistoryRequest1",
	"MessageBufferChatHistoryRequest2",
	"MessageBufferChatHistoryResponse",
	"MessageBuffer_ChannelRequest",
	"MessageBuffer_ChannelResponse",
	"NielsenContentMetadataRequest",
	"NielsenContentMetadataResponse1",
	"NielsenContentMetadataResponse2",
	"OneClickEligibilityRequest",
	"OneClickEligibilityResponse",
	"OneTapFeedRequest",
	"OneTapFeedResponse",
	"OnsiteNotifications_SummaryRequest",
	"OnsiteNotifications_SummaryResponse",
	"PaidPinnedChatRequest",
	"PaidPinnedChatResponse",
	"PbyPGameRequest",
	"PbyPGameResponse",
	"PersistentGoalFollowButton_UserRequest",
	"PersistentGoalFollowButton_UserResponse",
	"PinnedChatSettingsRequest",
	"PinnedChatSettingsResponse",
	"PinnedCheersSettingsRequest",
	"PinnedCheersSettingsResponse",
	"PlaybackAccessTokenRequest",
	"PlaybackAccessTokenResponse1",
	"PlaybackAccessTokenResponse2",
	"PrefetchPlaybackAccessTokenRequest",
	"PrefetchPlaybackAccessTokenResponse",
	"RealtimeStreamTagListRequest",
	"RealtimeStreamTagListResponse",
	"RecapEligibilityQueryRequest",
	"RecapEligibilityQueryResponse",
	"ReportMenuItemRequest",
	"ReportMenuItemResponse",
	"RoleRestrictedRequest",
	"RoleRestrictedResponse",
	"SearchResultsPage_SearchResultsRequest",
	"SearchResultsPage_SearchResultsResponse",
	"ShareClipRenderStatusRequest",
	"ShareClipRenderStatusResponse",
	"SharedChatModeratorStrikesRequest",
	"SharedChatModeratorStrikesResponse",
	"SharedChatSessionRequest",
	"SharedChatSessionResponse",
	"ShelvesRequest1",
	"ShelvesRequest2",
	"ShelvesRequest3",
	"ShelvesRequest4",
	"ShelvesResponse",
	"ShoutoutHighlightServiceQueryRequest",
	"ShoutoutHighlightServiceQueryResponse1",
	"ShoutoutHighlightServiceQueryResponse2",
	"StoryChannelQueryRequest",
	"StoryChannelQueryResponse",
	"StreamChatRequest",
	"StreamChatResponse",
	"StreamMetadataRequest",
	"StreamMetadataResponse",
	"StreamRefetchManagerRequest",
	"StreamRefetchManagerResponse",
	"StreamScheduleRequest",
	"StreamScheduleResponse",
	"SubscribedContextRequest",
	"SubscribedContextResponse",
	"SyncedSettingsChatPauseSettingRequest",
	"SyncedSettingsChatPauseSettingResponse",
	"SyncedSettingsDeletedMessageDisplaySettingRequest",
	"SyncedSettingsDeletedMessageDisplaySettingResponse",
	"SyncedSettingsEmoteAnimationsRequest",
	"SyncedSettingsEmoteAnimationsResponse",
	"SyncedSettingsReadableChatColorsRequest",
	"SyncedSettingsReadableChatColorsResponse",
	"TitleMentionsRequest",
	"TitleMentionsResponse",
	"UpdateConsentMutationRequest",
	"UpdateConsentMutationResponse",
	"UseLiveBroadcastRequest",
	"UseLiveBroadcastResponse",
	"UseLiveRequest",
	"UseLiveResponse",
	"UseViewCountRequest",
	"UseViewCountResponse",
	"UserMenuCurrentUserRequest",
	"UserMenuCurrentUserResponse",
	"UserModStatusRequest",
	"UserModStatusResponse",
	"VODMidrollManagerRequest",
	"VODMidrollManagerResponse",
	"VerifyEmail_CurrentUserRequest",
	"VerifyEmail_CurrentUserResponse",
	"VideoAccessToken_ClipRequest",
	"VideoAccessToken_ClipResponse",
	"VideoCommentsByOffsetOrCursorRequest1",
	"VideoCommentsByOffsetOrCursorRequest2",
	"VideoCommentsByOffsetOrCursorResponse",
	"VideoCommentsRequest",
	"VideoCommentsResponse",
	"VideoMarkersChatCommandRequest",
	"VideoMarkersChatCommandResponse",
	"VideoMetadataRequest",
	"VideoMetadataResponse",
	"VideoPlayerClipPostplayRecommendationsOverlayRequest",
	"VideoPlayerClipPostplayRecommendationsOverlayResponse",
	"VideoPlayerClipsButtonBroadcasterRequest",
	"VideoPlayerClipsButtonBroadcasterResponse",
	"VideoPlayerOfflineRecommendationsOverlayRequest",
	"VideoPlayerOfflineRecommendationsOverlayResponse",
	"VideoPlayerStatusOverlayChannelRequest",
	"VideoPlayerStatusOverlayChannelResponse",
	"VideoPlayerStreamMetadataRequest",
	"VideoPlayerStreamMetadataResponse",
	"VideoPlayerVODPostplayRecommendationsRequest",
	"VideoPlayerVODPostplayRecommendationsResponse",
	"VideoPlayer_AgeGateOverlayBroadcasterRequest",
	"VideoPlayer_AgeGateOverlayBroadcasterResponse",
	"VideoPlayer_ChapterSelectButtonVideoRequest",
	"VideoPlayer_ChapterSelectButtonVideoResponse",
	"VideoPlayer_MutedSegmentsAlertOverlayRequest",
	"VideoPlayer_MutedSegmentsAlertOverlayResponse",
	"VideoPlayer_VODSeekbarPreviewVideoRequest",
	"VideoPlayer_VODSeekbarPreviewVideoResponse",
	"VideoPlayer_VODSeekbarRequest",
	"VideoPlayer_VODSeekbarResponse",
	"VideoPlayer_VideoSourceManagerRequest",
	"VideoPlayer_VideoSourceManagerResponse",
	"VideoPreviewCard__VideoMomentsRequest",
	"VideoPreviewCard__VideoMomentsResponse",
	"VideoPreviewOverlayRequest",
	"VideoPreviewOverlayResponse",
	"WatchStreakExperimentRequest",
	"WatchStreakExperimentResponse",
	"Whispers_Whispers_UserWhisperThreadsRequest",
	"Whispers_Whispers_UserWhisperThreadsResponse",
	"WithIsStreamLiveQueryRequest",
	"WithIsStreamLiveQueryResponse",
	"incrementClipViewCountRequest",
	"incrementClipViewCountResponse",
	"queryUserViewedVideoRequest",
	"queryUserViewedVideoResponse",
	"updateUserViewedVideoRequest",
	"updateUserViewedVideoResponse"
]


class Endpoint:

	def __init__(self):
		self.extensions = {
			'persistedQuery': {
				'sha256Hash': self.sha256Hash,
				'version': 1,
			}
		}

		self.draft = {
			'extensions': self.extensions,
			'operationName': self.operation_name,
			'variables': {}
		}

	def build_query(self, variables: Dict = {}) -> Dict:
		"""Build the query for the endpoint."""
		...

class AccessGetFeatureClipRestrictionsQueryRequest(TypedDict):
	channelLogin: str

class AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsData(TypedDict):
	featuringRestrictedTo: NoneType
	__typename: str

class AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelData(TypedDict):
	id: str
	clipsSettings: AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsData
	__typename: str

class AccessGetFeatureClipRestrictionsQueryResponseUserData(TypedDict):
	id: str
	channel: AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelData
	__typename: str

class AccessGetFeatureClipRestrictionsQueryResponse(TypedDict):
	user: AccessGetFeatureClipRestrictionsQueryResponseUserData

class AcknowledgeUnbanRequestPromptRequest(TypedDict):
	channelLogin: str

class AcknowledgeUnbanRequestPromptResponseChannelData(TypedDict):
	id: str
	profileImageURL: str
	__typename: str

class AcknowledgeUnbanRequestPromptResponse(TypedDict):
	channel: AcknowledgeUnbanRequestPromptResponseChannelData

class AvailableEmotesForChannelPaginatedRequest(TypedDict):
	channelID: str
	withOwner: bool
	pageLimit: int

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeDataEmotesData(TypedDict):
	id: str
	setID: str
	token: str
	modifiers: NoneType
	type: str
	assetType: str
	__typename: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeData(TypedDict):
	id: str
	emotes: List[AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeDataEmotesData]
	owner: Union[NoneType, AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeDataOwnerData]
	__typename: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeData
	__typename: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedData(TypedDict):
	edges: List[AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesData]
	pageInfo: AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataPageinfoData
	__typename: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfData(TypedDict):
	availableEmoteSetsPaginated: Union[NoneType, AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedData]
	__typename: str

class AvailableEmotesForChannelPaginatedResponseChannelData(TypedDict):
	id: str
	self: AvailableEmotesForChannelPaginatedResponseChannelDataSelfData
	__typename: str

class AvailableEmotesForChannelPaginatedResponse(TypedDict):
	channel: AvailableEmotesForChannelPaginatedResponseChannelData

class BlockedUsersRequest(TypedDict):
	...

class BlockedUsersResponseCurrentuserData(TypedDict):
	id: str
	blockedUsers: Falsy[List[Any]]
	__typename: str

class BlockedUsersResponse(TypedDict):
	currentUser: BlockedUsersResponseCurrentuserData

class BrowsePage_AllDirectoriesRequest1OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class BrowsePage_AllDirectoriesRequest1OptionsData(TypedDict):
	recommendationsContext: BrowsePage_AllDirectoriesRequest1OptionsDataRecommendationscontextData
	requestID: str
	sort: str
	tags: Falsy[List[Any]]

class BrowsePage_AllDirectoriesRequest1(TypedDict):
	limit: int
	options: BrowsePage_AllDirectoriesRequest1OptionsData

class BrowsePage_AllDirectoriesRequest2OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class BrowsePage_AllDirectoriesRequest2OptionsData(TypedDict):
	recommendationsContext: BrowsePage_AllDirectoriesRequest2OptionsDataRecommendationscontextData
	requestID: str
	sort: str
	tags: Falsy[List[Any]]

class BrowsePage_AllDirectoriesRequest2(TypedDict):
	limit: int
	options: BrowsePage_AllDirectoriesRequest2OptionsData
	cursor: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesDataNodeDataTagsData(TypedDict):
	id: str
	isLanguageTag: bool
	localizedName: str
	tagName: str
	__typename: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesDataNodeData(TypedDict):
	id: str
	slug: str
	displayName: str
	name: str
	avatarURL: str
	viewersCount: int
	tags: List[BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesDataNodeDataTagsData]
	originalReleaseDate: Union[str, NoneType]
	__typename: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesData(TypedDict):
	cursor: str
	trackingID: str
	node: BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesDataNodeData
	__typename: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsData(TypedDict):
	edges: List[BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesData]
	pageInfo: BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataPageinfoData
	__typename: str

class BrowsePage_AllDirectoriesResponse(TypedDict):
	directoriesWithTags: BrowsePage_AllDirectoriesResponseDirectorieswithtagsData

class BrowseVerticalDirectoryRequestRecommendationscontextData(TypedDict):
	platform: str

class BrowseVerticalDirectoryRequest(TypedDict):
	imageWidth: int
	id: str
	recommendationsContext: BrowseVerticalDirectoryRequestRecommendationscontextData
	contentMin: int
	contentMax: int
	includeIsDJ: bool

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensDataNodeData(TypedDict):
	text: str
	hasEmphasis: bool
	location: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensDataNodeData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensData]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensDataNodeData(TypedDict):
	text: str
	hasEmphasis: bool
	location: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensDataNodeData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensData]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1GametagsData(TypedDict):
	id: str
	isLanguageTag: bool
	localizedName: str
	tagName: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1(TypedDict):
	id: str
	slug: str
	name: str
	viewersCount: int
	displayName: str
	boxArtURL: str
	gameTags: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1GametagsData]
	originalReleaseDate: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterData(TypedDict):
	id: str
	broadcastSettings: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataBroadcastsettingsData
	profileImageURL: str
	displayName: str
	login: str
	primaryColorHex: Union[NoneType, str]
	roles: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataRolesData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2GameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2FreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2PreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2(TypedDict):
	id: str
	broadcaster: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterData
	game: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2GameData
	freeformTags: Falsy[List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2FreeformtagsData]]
	viewersCount: int
	previewImageURL: str
	createdAt: str
	type: str
	previewThumbnailProperties: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2PreviewthumbnailpropertiesData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: Union[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1, BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2]
	trackingID: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentData(TypedDict):
	edges: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesData]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData1(TypedDict):
	text: str
	hasEmphasis: bool
	location: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2CollectionnameData(TypedDict):
	fallbackLocalizedTitle: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2(TypedDict):
	id: str
	slug: str
	collectionName: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2CollectionnameData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensData(TypedDict):
	node: Union[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData1, BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensData]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData1(TypedDict):
	text: str
	hasEmphasis: bool
	location: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2CollectionnameData(TypedDict):
	fallbackLocalizedTitle: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2(TypedDict):
	id: str
	slug: str
	collectionName: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2CollectionnameData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensData(TypedDict):
	node: Union[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData1, BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensData]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesData(TypedDict):
	content: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentData
	id: str
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleData
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleData
	type: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensDataNodeData(TypedDict):
	text: str
	hasEmphasis: bool
	location: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensDataNodeData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensData]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensDataNodeData(TypedDict):
	text: str
	hasEmphasis: bool
	location: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensDataNodeData
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensData]
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsData(TypedDict):
	id: str
	shelves: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesData]
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleData
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleData
	trackingID: str
	__typename: str

class BrowseVerticalDirectoryResponseVerticaldirectoryData(TypedDict):
	id: str
	trackingID: Falsy[str]
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleData
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleData
	shelfGroups: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsData]
	__typename: str

class BrowseVerticalDirectoryResponse(TypedDict):
	verticalDirectory: BrowseVerticalDirectoryResponseVerticaldirectoryData

class CanCreateClipRequest(TypedDict):
	broadcasterID: Union[NoneType, str]
	vodID: Union[str, NoneType]

class CanCreateClipResponseCancreateclipData(TypedDict):
	isAllowed: bool
	errorCode: NoneType
	requiredFollowingLengthMinutes: Falsy[int]
	__typename: str

class CanCreateClipResponse(TypedDict):
	canCreateClip: CanCreateClipResponseCancreateclipData

class CanViewersExportQueryRequest(TypedDict):
	channelLogin: str

class CanViewersExportQueryResponseUserDataChannelDataClipssettingsData(TypedDict):
	isClipsCreationEnabled: bool
	isViewerExportsEnabled: bool
	__typename: str

class CanViewersExportQueryResponseUserDataChannelData(TypedDict):
	id: str
	clipsSettings: CanViewersExportQueryResponseUserDataChannelDataClipssettingsData
	__typename: str

class CanViewersExportQueryResponseUserData(TypedDict):
	id: str
	channel: CanViewersExportQueryResponseUserDataChannelData
	__typename: str

class CanViewersExportQueryResponse(TypedDict):
	user: CanViewersExportQueryResponseUserData

class ChannelAvatarRequest(TypedDict):
	channelLogin: str
	includeIsDJ: bool

class ChannelAvatarResponseUserDataFollowersData(TypedDict):
	totalCount: int
	__typename: str

class ChannelAvatarResponseUserDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class ChannelAvatarResponseUserData(TypedDict):
	id: str
	followers: ChannelAvatarResponseUserDataFollowersData
	roles: ChannelAvatarResponseUserDataRolesData
	primaryColorHex: Union[NoneType, str]
	__typename: str

class ChannelAvatarResponse(TypedDict):
	user: ChannelAvatarResponseUserData

class ChannelClipCoreRequest(TypedDict):
	clipSlug: str

class ChannelClipCoreResponseClipDataBroadcasterDataChannelDataSelfData(TypedDict):
	isAuthorized: bool
	restrictionType: NoneType
	__typename: str

class ChannelClipCoreResponseClipDataBroadcasterDataChannelDataTrailerData(TypedDict):
	video: NoneType
	__typename: str

class ChannelClipCoreResponseClipDataBroadcasterDataChannelData(TypedDict):
	id: str
	self: ChannelClipCoreResponseClipDataBroadcasterDataChannelDataSelfData
	trailer: ChannelClipCoreResponseClipDataBroadcasterDataChannelDataTrailerData
	__typename: str

class ChannelClipCoreResponseClipDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: str
	profileImageURL: str
	stream: NoneType
	__typename: str
	channel: ChannelClipCoreResponseClipDataBroadcasterDataChannelData

class ChannelClipCoreResponseClipDataGueststarparticipantsData(TypedDict):
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]
	__typename: str

class ChannelClipCoreResponseClipData(TypedDict):
	id: str
	videoOffsetSeconds: Union[int, NoneType]
	broadcaster: ChannelClipCoreResponseClipDataBroadcasterData
	isFeatured: bool
	guestStarParticipants: ChannelClipCoreResponseClipDataGueststarparticipantsData
	__typename: str

class ChannelClipCoreResponse(TypedDict):
	clip: ChannelClipCoreResponseClipData

class ChannelCollaborationEligibilityQueryRequestOptionsData(TypedDict):
	channelIDs: List[str]

class ChannelCollaborationEligibilityQueryRequest(TypedDict):
	options: ChannelCollaborationEligibilityQueryRequestOptionsData

class ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesDataChannelcollabsData(TypedDict):
	id: str
	canJoinStatus: str
	__typename: str

class ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesData(TypedDict):
	channelCollabs: List[ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesDataChannelcollabsData]
	__typename: str

class ChannelCollaborationEligibilityQueryResponse(TypedDict):
	guestStarCollaborationStatuses: ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesData

class ChannelLeaderboardsRequest(TypedDict):
	first: int
	isClipLeaderboardEnabled: bool
	channelID: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesDataNodeDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesDataNodeData(TypedDict):
	id: str
	score: int
	rank: int
	user: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesDataNodeDataUserData
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesData(TypedDict):
	cursor: str
	node: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesDataNodeData
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsData(TypedDict):
	edges: Falsy[List[ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesData]]
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsData(TypedDict):
	id: str
	items: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsData
	myPosition: NoneType
	secondsRemaining: Falsy[int]
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeData(TypedDict):
	id: str
	score: int
	rank: int
	user: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeDataUserData
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesData(TypedDict):
	cursor: str
	node: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeData
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsData(TypedDict):
	edges: Falsy[List[ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesData]]
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftData(TypedDict):
	id: str
	items: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsData
	myPosition: NoneType
	secondsRemaining: Falsy[int]
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetData(TypedDict):
	bits: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsData
	subGift: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftData
	__typename: str

class ChannelLeaderboardsResponseUserDataChannelData(TypedDict):
	id: str
	leaderboardTimePeriod: str
	leaderboardSet: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetData
	__typename: str

class ChannelLeaderboardsResponseUserDataCheerDataSettingsData(TypedDict):
	id: str
	cheerMinimumBits: int
	__typename: str

class ChannelLeaderboardsResponseUserDataCheerData(TypedDict):
	id: str
	settings: ChannelLeaderboardsResponseUserDataCheerDataSettingsData
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataPriceinfoData(TypedDict):
	currency: str
	exponent: int
	price: int
	id: str
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData(TypedDict):
	key: str
	value: str
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: NoneType
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData]
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData(TypedDict):
	chargeModel: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData(TypedDict):
	min: int
	max: int
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData(TypedDict):
	id: str
	tplr: str
	platform: str
	eligibility: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData
	tagBindings: List[ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData]
	giftType: str
	listing: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData
	promotion: NoneType
	quantity: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityData(TypedDict):
	offer: Union[NoneType, ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData]
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingData(TypedDict):
	community: Union[NoneType, List[ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityData]]
	__typename: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsData(TypedDict):
	id: str
	name: str
	price: str
	priceInfo: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataPriceinfoData
	gifting: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingData
	__typename: str

class ChannelLeaderboardsResponseUserData(TypedDict):
	id: str
	login: str
	displayName: str
	channel: ChannelLeaderboardsResponseUserDataChannelData
	cheer: ChannelLeaderboardsResponseUserDataCheerData
	subscriptionProducts: List[ChannelLeaderboardsResponseUserDataSubscriptionproductsData]
	__typename: str

class ChannelLeaderboardsResponseCurrentuserData(TypedDict):
	id: str
	__typename: str

class ChannelLeaderboardsResponse(TypedDict):
	user: ChannelLeaderboardsResponseUserData
	currentUser: Union[NoneType, ChannelLeaderboardsResponseCurrentuserData]

class ChannelPage_SetSessionStatusRequestInputDataActivityData(TypedDict):
	userID: str
	type: str

class ChannelPage_SetSessionStatusRequestInputData(TypedDict):
	sessionID: str
	availability: str
	activity: Union[NoneType, ChannelPage_SetSessionStatusRequestInputDataActivityData]

class ChannelPage_SetSessionStatusRequest(TypedDict):
	input: ChannelPage_SetSessionStatusRequestInputData

class ChannelPage_SetSessionStatusResponseSetsessionstatusData(TypedDict):
	setAgainInSeconds: int
	__typename: str

class ChannelPage_SetSessionStatusResponse(TypedDict):
	setSessionStatus: ChannelPage_SetSessionStatusResponseSetsessionstatusData

class ChannelPage_SubscribeButton_UserRequest1(TypedDict):
	login: str
	includeExpiredDunning: bool

class ChannelPage_SubscribeButton_UserRequest2(TypedDict):
	login: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataTagbindingsData(TypedDict):
	key: str
	value: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceDataDiscountData(TypedDict):
	price: int
	total: int
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceDataDiscountData]
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanData
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalData]
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingData(TypedDict):
	chargeModel: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelData
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataPromotionDataPromodisplayData(TypedDict):
	discountPercent: int
	discountType: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataPromotionData(TypedDict):
	id: str
	name: str
	promoDisplay: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataPromotionDataPromodisplayData
	priority: Falsy[int]
	promoType: str
	endAt: NoneType
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataQuantityData(TypedDict):
	min: int
	max: int
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersData(TypedDict):
	id: str
	tplr: str
	platform: str
	eligibility: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataEligibilityData
	tagBindings: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataTagbindingsData]
	giftType: NoneType
	listing: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingData
	promotion: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataPromotionData]
	quantity: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataQuantityData
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData(TypedDict):
	key: str
	value: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: NoneType
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData]
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData(TypedDict):
	chargeModel: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData(TypedDict):
	min: int
	max: int
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData(TypedDict):
	id: str
	tplr: str
	platform: str
	eligibility: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData
	tagBindings: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData]
	giftType: str
	listing: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData
	promotion: NoneType
	quantity: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityData(TypedDict):
	offer: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData]
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingData(TypedDict):
	community: Union[NoneType, List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityData]]
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsData(TypedDict):
	id: str
	emoteSetID: str
	name: str
	hasAdFree: bool
	tier: str
	offers: Union[NoneType, List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersData]]
	gifting: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingData
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSelfDataCumulativetenureData(TypedDict):
	daysRemaining: Falsy[int]
	months: Falsy[int]
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserDataSelfData(TypedDict):
	canPrimeSubscribe: bool
	cumulativeTenure: ChannelPage_SubscribeButton_UserResponseUserDataSelfDataCumulativetenureData
	follower: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSelfDataFollowerData]
	subscriptionBenefit: NoneType
	__typename: str

class ChannelPage_SubscribeButton_UserResponseUserData(TypedDict):
	id: str
	displayName: str
	primaryColorHex: Union[str, NoneType]
	subscriptionProducts: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsData]
	self: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSelfData]
	__typename: str

class ChannelPage_SubscribeButton_UserResponseRequestinfoData(TypedDict):
	countryCode: str
	__typename: str

class ChannelPage_SubscribeButton_UserResponse(TypedDict):
	user: ChannelPage_SubscribeButton_UserResponseUserData
	requestInfo: ChannelPage_SubscribeButton_UserResponseRequestinfoData

class ChannelPointsContextRequest(TypedDict):
	channelLogin: str
	includeGoalTypes: List[str]

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData(TypedDict):
	id: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataLastviewedcontentData(TypedDict):
	contentType: str
	lastViewedAt: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsDataRewardData(TypedDict):
	id: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsData(TypedDict):
	reward: ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsDataRewardData
	userRedemptionsCurrentStream: Falsy[int]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsData(TypedDict):
	availableClaim: Union[NoneType, ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData]
	__typename: str
	balance: Falsy[int]
	activeMultipliers: Falsy[List[Any]]
	canRedeemRewardsForFree: bool
	lastViewedContent: List[ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataLastviewedcontentData]
	userRedemptions: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsData]]

class ChannelPointsContextResponseCommunityDataChannelDataSelfData(TypedDict):
	communityPoints: Union[NoneType, ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsData]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataImageData(TypedDict):
	url: str
	url2x: str
	url4x: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataDefaultimageData(TypedDict):
	url: str
	url2x: str
	url4x: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerStream: Falsy[int]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperuserperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerUserPerStream: Falsy[int]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataGlobalcooldownsettingData(TypedDict):
	isEnabled: bool
	globalCooldownSeconds: Falsy[int]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsData(TypedDict):
	id: str
	backgroundColor: NoneType
	bitsCost: Union[int, NoneType]
	cost: Union[int, NoneType]
	defaultBackgroundColor: str
	defaultBitsCost: Falsy[int]
	defaultCost: Falsy[int]
	defaultImage: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataDefaultimageData
	image: NoneType
	isEnabled: bool
	isHiddenForSubs: bool
	cooldownExpiresAt: NoneType
	isInStock: bool
	redemptionsRedeemedCurrentStream: NoneType
	minimumCost: Falsy[int]
	pricingType: str
	type: str
	updatedForIndicatorAt: Union[str, NoneType]
	globallyUpdatedForIndicatorAt: str
	maxPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperstreamsettingData
	maxPerUserPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperuserperstreamsettingData
	globalCooldownSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataGlobalcooldownsettingData
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataDefaultimageData(TypedDict):
	url: str
	url2x: str
	url4x: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataImageData(TypedDict):
	url: str
	url2x: str
	url4x: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataMaxperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerStream: Falsy[int]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataMaxperuserperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerUserPerStream: Falsy[int]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataGlobalcooldownsettingData(TypedDict):
	isEnabled: bool
	globalCooldownSeconds: Falsy[int]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsData(TypedDict):
	id: str
	backgroundColor: str
	cooldownExpiresAt: Union[str, NoneType]
	cost: int
	defaultImage: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataDefaultimageData
	image: Union[NoneType, ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataImageData]
	maxPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataMaxperstreamsettingData
	maxPerUserPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataMaxperuserperstreamsettingData
	globalCooldownSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataGlobalcooldownsettingData
	isEnabled: bool
	isInStock: bool
	isPaused: bool
	isSubOnly: bool
	isUserInputRequired: bool
	shouldRedemptionsSkipRequestQueue: bool
	redemptionsRedeemedCurrentStream: Union[Falsy[int], NoneType]
	prompt: Union[NoneType, str]
	title: str
	updatedForIndicatorAt: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataGoalsDataDefaultimageData(TypedDict):
	url: str
	url2x: str
	url4x: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataGoalsData(TypedDict):
	backgroundColor: str
	description: NoneType
	durationDays: int
	endedAt: str
	amountNeeded: int
	id: str
	defaultImage: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataGoalsDataDefaultimageData
	image: NoneType
	isInStock: bool
	smallContribution: int
	perStreamUserMaximumContribution: int
	pointsContributed: int
	startedAt: str
	status: str
	title: str
	type: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataEmoteData(TypedDict):
	id: str
	token: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataEmoteData(TypedDict):
	id: str
	token: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataModifierData(TypedDict):
	id: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsData(TypedDict):
	id: str
	emote: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataEmoteData
	modifier: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataModifierData
	globallyUpdatedForIndicatorAt: str
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsData(TypedDict):
	id: str
	isUnlockable: bool
	emote: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataEmoteData
	modifications: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsData]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataWatchstreakpointsData(TypedDict):
	points: int
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataMultipliersData(TypedDict):
	reasonCode: str
	factor: Union[int, float]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningData(TypedDict):
	id: str
	averagePointsPerHour: int
	cheerPoints: int
	claimPoints: int
	followPoints: int
	passiveWatchPoints: int
	raidPoints: int
	subscriptionGiftPoints: int
	watchStreakPoints: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataWatchstreakpointsData]
	multipliers: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataMultipliersData]
	__typename: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsData(TypedDict):
	name: Union[str, NoneType]
	image: Union[NoneType, ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataImageData]
	__typename: str
	automaticRewards: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsData]
	customRewards: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsData]]
	goals: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataGoalsData]]
	isEnabled: bool
	raidPointAmount: int
	emoteVariants: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsData]
	earning: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningData

class ChannelPointsContextResponseCommunityDataChannelData(TypedDict):
	id: str
	self: ChannelPointsContextResponseCommunityDataChannelDataSelfData
	__typename: str
	communityPointsSettings: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsData

class ChannelPointsContextResponseCommunityDataSelfData(TypedDict):
	isModerator: bool
	__typename: str

class ChannelPointsContextResponseCommunityData(TypedDict):
	id: str
	displayName: str
	profileImageURL: str
	channel: ChannelPointsContextResponseCommunityDataChannelData
	__typename: str
	self: Union[NoneType, ChannelPointsContextResponseCommunityDataSelfData]

class ChannelPointsContextResponseCurrentuserDataCommunitypointsDataLastviewedcontentData(TypedDict):
	contentID: str
	contentType: str
	lastViewedAt: str
	__typename: str

class ChannelPointsContextResponseCurrentuserDataCommunitypointsData(TypedDict):
	lastViewedContent: List[ChannelPointsContextResponseCurrentuserDataCommunitypointsDataLastviewedcontentData]
	__typename: str

class ChannelPointsContextResponseCurrentuserData(TypedDict):
	id: str
	communityPoints: ChannelPointsContextResponseCurrentuserDataCommunitypointsData
	__typename: str

class ChannelPointsContextResponse(TypedDict):
	community: ChannelPointsContextResponseCommunityData
	currentUser: Union[NoneType, ChannelPointsContextResponseCurrentuserData]

class ChannelPointsGlobalContextRequest(TypedDict):
	...

class ChannelPointsGlobalContextResponseEmotemodifiersDataIcondarkData(TypedDict):
	url: str
	url2x: str
	url4x: str
	__typename: str

class ChannelPointsGlobalContextResponseEmotemodifiersDataIconlightData(TypedDict):
	url: str
	url2x: str
	url4x: str
	__typename: str

class ChannelPointsGlobalContextResponseEmotemodifiersData(TypedDict):
	id: str
	title: str
	iconDark: ChannelPointsGlobalContextResponseEmotemodifiersDataIcondarkData
	iconLight: ChannelPointsGlobalContextResponseEmotemodifiersDataIconlightData
	__typename: str

class ChannelPointsGlobalContextResponse(TypedDict):
	emoteModifiers: List[ChannelPointsGlobalContextResponseEmotemodifiersData]

class ChannelPointsPredictionContextRequest(TypedDict):
	count: int
	channelLogin: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataPredictionsettingsData(TypedDict):
	isEligibleForPredictions: bool
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataCreatedbyData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsData(TypedDict):
	id: str
	points: int
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsDataUserData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataBadgeData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: NoneType
	clickURL: NoneType
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: int
	totalUsers: int
	topPredictors: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsData]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataBadgeData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsData(TypedDict):
	id: str
	createdAt: str
	createdBy: ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataCreatedbyData
	endedAt: NoneType
	lockedAt: NoneType
	outcomes: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesData]
	predictionWindowSeconds: int
	status: str
	title: str
	winningOutcome: NoneType
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataCreatedbyData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsData(TypedDict):
	id: str
	points: int
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsDataUserData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataBadgeData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: NoneType
	clickURL: NoneType
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: int
	totalUsers: int
	topPredictors: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsData]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataBadgeData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsData(TypedDict):
	id: str
	createdAt: str
	createdBy: ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataCreatedbyData
	endedAt: NoneType
	lockedAt: str
	outcomes: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesData]
	predictionWindowSeconds: int
	status: str
	title: str
	winningOutcome: NoneType
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataCreatedbyData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsData(TypedDict):
	id: str
	points: Falsy[int]
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsDataUserData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataBadgeData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: NoneType
	clickURL: NoneType
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: Falsy[int]
	totalUsers: Falsy[int]
	topPredictors: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsData]]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataBadgeData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsData(TypedDict):
	id: str
	points: Falsy[int]
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsDataUserData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataBadgeData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: NoneType
	clickURL: NoneType
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: Falsy[int]
	totalUsers: Falsy[int]
	topPredictors: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsData]]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataBadgeData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeData(TypedDict):
	id: str
	createdAt: str
	createdBy: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataCreatedbyData
	endedAt: str
	lockedAt: str
	outcomes: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesData]
	predictionWindowSeconds: int
	status: str
	title: str
	winningOutcome: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesData(TypedDict):
	node: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsData(TypedDict):
	edges: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesData]]
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataSelfData(TypedDict):
	recentPredictions: Union[NoneType, Falsy[List[Any]]]
	__typename: str

class ChannelPointsPredictionContextResponseCommunityDataChannelData(TypedDict):
	id: str
	predictionSettings: ChannelPointsPredictionContextResponseCommunityDataChannelDataPredictionsettingsData
	activePredictionEvents: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsData]]
	lockedPredictionEvents: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsData]]
	resolvedPredictionEvents: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsData
	self: ChannelPointsPredictionContextResponseCommunityDataChannelDataSelfData
	__typename: str

class ChannelPointsPredictionContextResponseCommunityData(TypedDict):
	id: str
	channel: ChannelPointsPredictionContextResponseCommunityDataChannelData
	__typename: str

class ChannelPointsPredictionContextResponseCurrentuserDataPredictionssettingsData(TypedDict):
	hasAcceptedTOS: bool
	isTemporaryChatBadgeEnabled: bool
	__typename: str

class ChannelPointsPredictionContextResponseCurrentuserData(TypedDict):
	id: str
	predictionsSettings: ChannelPointsPredictionContextResponseCurrentuserDataPredictionssettingsData
	__typename: str

class ChannelPointsPredictionContextResponse(TypedDict):
	community: ChannelPointsPredictionContextResponseCommunityData
	currentUser: Union[NoneType, ChannelPointsPredictionContextResponseCurrentuserData]

class ChannelShellRequest(TypedDict):
	login: str

class ChannelShellResponseUserorerrorDataStreamData(TypedDict):
	id: str
	viewersCount: int
	__typename: str

class ChannelShellResponseUserorerrorDataChannelDataSelfData(TypedDict):
	isAuthorized: bool
	restrictionType: NoneType
	__typename: str

class ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoDataSelfData(TypedDict):
	viewingHistory: NoneType
	__typename: str

class ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoData(TypedDict):
	id: str
	self: ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoDataSelfData
	__typename: str

class ChannelShellResponseUserorerrorDataChannelDataTrailerData(TypedDict):
	video: Union[NoneType, ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoData]
	__typename: str

class ChannelShellResponseUserorerrorDataChannelDataHomeDataPreferencesData(TypedDict):
	heroPreset: str
	__typename: str

class ChannelShellResponseUserorerrorDataChannelDataHomeData(TypedDict):
	preferences: ChannelShellResponseUserorerrorDataChannelDataHomeDataPreferencesData
	__typename: str

class ChannelShellResponseUserorerrorDataChannelData(TypedDict):
	id: str
	self: ChannelShellResponseUserorerrorDataChannelDataSelfData
	trailer: ChannelShellResponseUserorerrorDataChannelDataTrailerData
	home: ChannelShellResponseUserorerrorDataChannelDataHomeData
	__typename: str

class ChannelShellResponseUserorerrorData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: Union[str, NoneType]
	profileImageURL: str
	stream: Union[NoneType, ChannelShellResponseUserorerrorDataStreamData]
	__typename: str
	bannerImageURL: Union[NoneType, str]
	channel: ChannelShellResponseUserorerrorDataChannelData

class ChannelShellResponse(TypedDict):
	userOrError: ChannelShellResponseUserorerrorData

class ChannelSkinsRequestSponsorshipsparamsDataPreviewoverrideData(TypedDict):
	dspCreativeOverride: Falsy[str]
	campaignOverride: Falsy[str]
	productInstanceOverride: Falsy[str]

class ChannelSkinsRequestSponsorshipsparamsData(TypedDict):
	deviceMake: Falsy[str]
	deviceOS: Falsy[str]
	deviceType: str
	platform: str
	previewOverride: ChannelSkinsRequestSponsorshipsparamsDataPreviewoverrideData

class ChannelSkinsRequest(TypedDict):
	channelLogin: str
	sponsorshipsParams: ChannelSkinsRequestSponsorshipsparamsData

class ChannelSkinsResponseChannelData(TypedDict):
	id: str
	sponsorships: NoneType
	__typename: str

class ChannelSkinsResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType
	__typename: str

class ChannelSkinsResponseUserData(TypedDict):
	id: str
	displayName: str
	profileImageURL: str
	login: str
	primaryColorHex: Union[NoneType, str]
	self: Union[NoneType, ChannelSkinsResponseUserDataSelfData]
	__typename: str

class ChannelSkinsResponseCurrentuserData(TypedDict):
	id: str
	hasTurbo: bool
	__typename: str

class ChannelSkinsResponseRequestinfoData(TypedDict):
	countryCodeAlpha2: str
	__typename: str

class ChannelSkinsResponse(TypedDict):
	channel: ChannelSkinsResponseChannelData
	user: ChannelSkinsResponseUserData
	currentUser: Union[NoneType, ChannelSkinsResponseCurrentuserData]
	requestInfo: ChannelSkinsResponseRequestinfoData

class ChannelSocialButtonsRequest(TypedDict):
	channelID: str

class ChannelSocialButtonsResponseChannelDataLocalemotesetsDataEmotesData(TypedDict):
	id: str
	token: str
	type: str
	__typename: str

class ChannelSocialButtonsResponseChannelDataLocalemotesetsData(TypedDict):
	id: str
	emotes: List[ChannelSocialButtonsResponseChannelDataLocalemotesetsDataEmotesData]
	productType: str
	__typename: str

class ChannelSocialButtonsResponseChannelData(TypedDict):
	id: str
	localEmoteSets: List[ChannelSocialButtonsResponseChannelDataLocalemotesetsData]
	__typename: str

class ChannelSocialButtonsResponse(TypedDict):
	channel: ChannelSocialButtonsResponseChannelData

class ChannelSupportButtonsRequest(TypedDict):
	channelLogin: str

class ChannelSupportButtonsResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool
	__typename: str

class ChannelSupportButtonsResponseUserDataSelfData(TypedDict):
	follower: Union[NoneType, ChannelSupportButtonsResponseUserDataSelfDataFollowerData]
	__typename: str

class ChannelSupportButtonsResponseUserData(TypedDict):
	id: str
	displayName: str
	self: Union[NoneType, ChannelSupportButtonsResponseUserDataSelfData]
	__typename: str

class ChannelSupportButtonsResponse(TypedDict):
	user: ChannelSupportButtonsResponseUserData

class ChannelVideoCoreRequest(TypedDict):
	videoID: str

class ChannelVideoCoreResponseVideoDataOwnerDataChannelDataSelfData(TypedDict):
	isAuthorized: bool
	restrictionType: NoneType
	__typename: str

class ChannelVideoCoreResponseVideoDataOwnerDataChannelDataTrailerData(TypedDict):
	video: NoneType
	__typename: str

class ChannelVideoCoreResponseVideoDataOwnerDataChannelData(TypedDict):
	id: str
	self: ChannelVideoCoreResponseVideoDataOwnerDataChannelDataSelfData
	trailer: ChannelVideoCoreResponseVideoDataOwnerDataChannelDataTrailerData
	__typename: str

class ChannelVideoCoreResponseVideoDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: str
	profileImageURL: str
	stream: NoneType
	__typename: str
	channel: ChannelVideoCoreResponseVideoDataOwnerDataChannelData

class ChannelVideoCoreResponseVideoData(TypedDict):
	id: str
	owner: ChannelVideoCoreResponseVideoDataOwnerData
	__typename: str

class ChannelVideoCoreResponse(TypedDict):
	video: ChannelVideoCoreResponseVideoData

class ChannelVideoShelvesQueryRequest(TypedDict):
	includePreviewBlur: bool
	channelLogin: str
	first: int

class ChannelVideoShelvesQueryResponseCurrentuserData(TypedDict):
	id: str
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataOwnerData(TypedDict):
	id: str
	login: str
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	roles: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataOwnerDataRolesData
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: NoneType
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeData(TypedDict):
	animatedPreviewURL: str
	game: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataGameData
	id: str
	lengthSeconds: int
	owner: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	self: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeDataSelfData
	title: str
	viewCount: int
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesData(TypedDict):
	cursor: str
	node: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesDataNodeData
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsData(TypedDict):
	totalCount: int
	edges: List[ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataEdgesData]
	pageInfo: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsDataPageinfoData
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionData(TypedDict):
	id: str
	description: Falsy[str]
	owner: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataOwnerData
	thumbnailURL: str
	title: str
	type: str
	updatedAt: str
	lengthSeconds: int
	__typename: str
	items: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionDataItemsData

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1CuratorData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1ClipgameData(TypedDict):
	id: str
	slug: str
	name: str
	boxArtURL: str
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: str
	roles: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterDataRolesData
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1GueststarparticipantsData(TypedDict):
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1(TypedDict):
	id: str
	slug: str
	clipTitle: str
	clipViewCount: int
	curator: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1CuratorData
	clipGame: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1ClipgameData
	broadcaster: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterData
	thumbnailURL: str
	createdAt: str
	durationSeconds: int
	isFeatured: bool
	guestStarParticipants: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1GueststarparticipantsData
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2GameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2OwnerDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2OwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	roles: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2OwnerDataRolesData
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2SelfDataViewinghistoryData(TypedDict):
	position: Union[NoneType, int]
	updatedAt: Union[NoneType, str]
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2SelfData(TypedDict):
	isRestricted: bool
	viewingHistory: Union[NoneType, ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2SelfDataViewinghistoryData]
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2(TypedDict):
	animatedPreviewURL: str
	game: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2GameData
	id: str
	lengthSeconds: int
	owner: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2OwnerData
	previewThumbnailURL: str
	publishedAt: str
	self: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2SelfData
	title: str
	viewCount: int
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	description: NoneType
	type: str
	collection: Union[NoneType, ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataCollectionData]
	items: List[Union[ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1, ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2]]
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesData(TypedDict):
	cursor: str
	node: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesDataNodeData
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesData(TypedDict):
	edges: Falsy[List[ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesData]]
	pageInfo: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataPageinfoData
	__typename: str

class ChannelVideoShelvesQueryResponseUserData(TypedDict):
	id: str
	displayName: str
	primaryColorHex: str
	videoShelves: ChannelVideoShelvesQueryResponseUserDataVideoshelvesData
	__typename: str

class ChannelVideoShelvesQueryResponse(TypedDict):
	currentUser: Union[NoneType, ChannelVideoShelvesQueryResponseCurrentuserData]
	user: ChannelVideoShelvesQueryResponseUserData

class Chat_ChannelDataRequest(TypedDict):
	channelLogin: str

class Chat_ChannelDataResponseChannelDataChatsettingsData(TypedDict):
	rules: Falsy[List[Falsy[str]]]
	__typename: str

class Chat_ChannelDataResponseChannelDataSelfData(TypedDict):
	isEditor: bool
	isModerator: bool
	isVIP: bool
	__typename: str

class Chat_ChannelDataResponseChannelData(TypedDict):
	id: str
	login: str
	displayName: str
	chatSettings: Chat_ChannelDataResponseChannelDataChatsettingsData
	self: Union[NoneType, Chat_ChannelDataResponseChannelDataSelfData]
	__typename: str

class Chat_ChannelDataResponse(TypedDict):
	channel: Chat_ChannelDataResponseChannelData

class Chat_EarnedBadges_InitialSubStatusRequest(TypedDict):
	channelLogin: str

class Chat_EarnedBadges_InitialSubStatusResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType
	__typename: str

class Chat_EarnedBadges_InitialSubStatusResponseUserData(TypedDict):
	id: str
	self: Chat_EarnedBadges_InitialSubStatusResponseUserDataSelfData
	__typename: str

class Chat_EarnedBadges_InitialSubStatusResponse(TypedDict):
	user: Chat_EarnedBadges_InitialSubStatusResponseUserData

class Chat_OrbisPresetTextRequest(TypedDict):
	login: str

class Chat_OrbisPresetTextResponseUserDataStreamData(TypedDict):
	id: str
	platform: NoneType
	__typename: str

class Chat_OrbisPresetTextResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, Chat_OrbisPresetTextResponseUserDataStreamData]
	__typename: str

class Chat_OrbisPresetTextResponse(TypedDict):
	user: Chat_OrbisPresetTextResponseUserData

class Chat_ShareResub_ChannelDataRequest(TypedDict):
	channelLogin: str

class Chat_ShareResub_ChannelDataResponseUserDataSelfData(TypedDict):
	resubNotification: NoneType
	__typename: str

class Chat_ShareResub_ChannelDataResponseUserData(TypedDict):
	id: str
	self: Chat_ShareResub_ChannelDataResponseUserDataSelfData
	__typename: str

class Chat_ShareResub_ChannelDataResponse(TypedDict):
	user: Chat_ShareResub_ChannelDataResponseUserData

class Chat_UserDataRequest(TypedDict):
	...

class Chat_UserDataResponseUserDataRolesData(TypedDict):
	isGlobalMod: NoneType
	isSiteAdmin: NoneType
	isStaff: NoneType
	__typename: str

class Chat_UserDataResponseUserData(TypedDict):
	id: str
	displayName: str
	login: str
	roles: Chat_UserDataResponseUserDataRolesData
	__typename: str

class Chat_UserDataResponse(TypedDict):
	user: Chat_UserDataResponseUserData

class ChatClipRequest(TypedDict):
	clipSlug: str

class ChatClipResponseClipDataVideoData(TypedDict):
	id: str
	__typename: str

class ChatClipResponseClipData(TypedDict):
	id: str
	videoOffsetSeconds: Union[int, NoneType]
	durationSeconds: int
	video: Union[NoneType, ChatClipResponseClipDataVideoData]
	__typename: str

class ChatClipResponse(TypedDict):
	clip: ChatClipResponseClipData

class ChatFilterContextManager_UserRequest(TypedDict):
	...

class ChatFilterContextManager_UserResponseCurrentuserData(TypedDict):
	id: str
	createdAt: str
	__typename: str

class ChatFilterContextManager_UserResponse(TypedDict):
	currentUser: ChatFilterContextManager_UserResponseCurrentuserData

class ChatInputRequest(TypedDict):
	channelLogin: str
	isEmbedded: bool

class ChatInputResponseCurrentuserData(TypedDict):
	id: str
	bitsBalance: Falsy[int]
	__typename: str

class ChatInputResponseChannelDataSelfDataChatmoderatorstrikestatusData(TypedDict):
	id: str
	banDetails: NoneType
	warningDetails: NoneType
	timeoutDetails: NoneType
	__typename: str

class ChatInputResponseChannelDataSelfData(TypedDict):
	chatModeratorStrikeStatus: ChatInputResponseChannelDataSelfDataChatmoderatorstrikestatusData
	__typename: str

class ChatInputResponseChannelDataCheerDataSettingsData(TypedDict):
	id: str
	emoteMinimumBits: int
	cheerMinimumBits: int
	event: NoneType
	__typename: str

class ChatInputResponseChannelDataCheerData(TypedDict):
	id: str
	settings: ChatInputResponseChannelDataCheerDataSettingsData
	__typename: str

class ChatInputResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, ChatInputResponseChannelDataSelfData]
	displayName: str
	profileImageURL: str
	cheer: ChatInputResponseChannelDataCheerData
	__typename: str

class ChatInputResponse(TypedDict):
	currentUser: Union[NoneType, ChatInputResponseCurrentuserData]
	channel: ChatInputResponseChannelData

class ChatInput_BadgesRequest(TypedDict):
	...

class ChatInput_BadgesResponseCurrentuserData(TypedDict):
	id: str
	chatColor: NoneType
	displayName: str
	login: str
	__typename: str

class ChatInput_BadgesResponse(TypedDict):
	currentUser: ChatInput_BadgesResponseCurrentuserData

class ChatList_BadgesRequest(TypedDict):
	channelLogin: str

class ChatList_BadgesResponseUserDataBroadcastbadgesData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: str
	clickURL: Union[NoneType, str]
	__typename: str

class ChatList_BadgesResponseUserDataSelfData(TypedDict):
	selectedBadge: NoneType
	displayBadges: Falsy[List[Any]]
	__typename: str

class ChatList_BadgesResponseUserData(TypedDict):
	id: str
	primaryColorHex: Union[str, NoneType]
	broadcastBadges: Falsy[List[ChatList_BadgesResponseUserDataBroadcastbadgesData]]
	self: Union[NoneType, ChatList_BadgesResponseUserDataSelfData]
	__typename: str

class ChatList_BadgesResponse(TypedDict):
	user: ChatList_BadgesResponseUserData

class ChatModeratorStrikeStatusRequest(TypedDict):
	channelID: str
	targetUserID: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataModerateduserData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataRoomownerData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusData(TypedDict):
	id: str
	moderatedUser: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataModerateduserData
	roomOwner: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataRoomownerData
	banDetails: NoneType
	timeoutDetails: NoneType
	warningDetails: NoneType
	__typename: str

class ChatModeratorStrikeStatusResponse(TypedDict):
	chatModeratorStrikeStatus: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusData

class ChatRestrictionsRequest(TypedDict):
	channelLogin: str

class ChatRestrictionsResponseChannelDataSelfDataFollowerData(TypedDict):
	followedAt: str
	__typename: str

class ChatRestrictionsResponseChannelDataSelfData(TypedDict):
	chatRestrictedReasons: List[str]
	lastRecentChatMessageAt: NoneType
	follower: Union[NoneType, ChatRestrictionsResponseChannelDataSelfDataFollowerData]
	banStatus: NoneType
	isFirstTimeChatter: bool
	subscriptionBenefit: NoneType
	isVIP: bool
	isModerator: bool
	__typename: str

class ChatRestrictionsResponseChannelDataChatsettingsData(TypedDict):
	requireVerifiedAccount: bool
	__typename: str

class ChatRestrictionsResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, ChatRestrictionsResponseChannelDataSelfData]
	chatSettings: ChatRestrictionsResponseChannelDataChatsettingsData
	__typename: str

class ChatRestrictionsResponseCurrentuserData(TypedDict):
	id: str
	createdAt: str
	isEmailVerified: bool
	isPhoneNumberVerified: bool
	__typename: str

class ChatRestrictionsResponse(TypedDict):
	channel: ChatRestrictionsResponseChannelData
	currentUser: Union[NoneType, ChatRestrictionsResponseCurrentuserData]

class ChatRoomBanStatusRequest(TypedDict):
	targetUserID: str
	channelID: str

class ChatRoomBanStatusResponseTargetuserData(TypedDict):
	id: str
	login: str
	__typename: str

class ChatRoomBanStatusResponse(TypedDict):
	chatRoomBanStatus: NoneType
	targetUser: ChatRoomBanStatusResponseTargetuserData

class ChatRoomStateRequest(TypedDict):
	login: str

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialemailverificationconfigData(TypedDict):
	minimumAccountAgeInMinutes: Falsy[int]
	minimumFollowerAgeInMinutes: Falsy[int]
	shouldRestrictBasedOnAccountAge: bool
	shouldRestrictFirstTimeChatters: bool
	shouldRestrictBasedOnFollowerAge: bool
	__typename: str

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialphoneverificationconfigData(TypedDict):
	minimumAccountAgeInMinutes: Falsy[int]
	minimumFollowerAgeInMinutes: Falsy[int]
	shouldRestrictBasedOnAccountAge: bool
	shouldRestrictFirstTimeChatters: bool
	shouldRestrictBasedOnFollowerAge: bool
	__typename: str

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsData(TypedDict):
	emailVerificationMode: str
	partialEmailVerificationConfig: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialemailverificationconfigData
	phoneVerificationMode: str
	partialPhoneVerificationConfig: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialphoneverificationconfigData
	isSubscriberExempt: bool
	isVIPExempt: bool
	isModeratorExempt: bool
	__typename: str

class ChatRoomStateResponseChannelDataChatsettingsData(TypedDict):
	isEmoteOnlyModeEnabled: bool
	followersOnlyDurationMinutes: Union[Falsy[int], NoneType]
	slowModeDurationSeconds: Union[int, NoneType]
	accountVerificationOptions: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsData
	__typename: str

class ChatRoomStateResponseChannelDataSubscriptionproductsData(TypedDict):
	id: str
	hasSubOnlyChat: bool
	__typename: str

class ChatRoomStateResponseChannelData(TypedDict):
	id: str
	chatSettings: ChatRoomStateResponseChannelDataChatsettingsData
	subscriptionProducts: List[ChatRoomStateResponseChannelDataSubscriptionproductsData]
	__typename: str

class ChatRoomStateResponse(TypedDict):
	channel: ChatRoomStateResponseChannelData

class ChatScreenReaderAutoAnnounceRequest(TypedDict):
	...

class ChatScreenReaderAutoAnnounceResponseCurrentuserData(TypedDict):
	id: str
	isChatScreenReaderAutoAnnounceEnabled: bool
	__typename: str

class ChatScreenReaderAutoAnnounceResponse(TypedDict):
	currentUser: ChatScreenReaderAutoAnnounceResponseCurrentuserData

class ClaimCommunityPointsRequestInputData(TypedDict):
	channelID: str
	claimID: str

class ClaimCommunityPointsRequest(TypedDict):
	input: ClaimCommunityPointsRequestInputData

class ClaimCommunityPointsResponseClaimcommunitypointsDataClaimData(TypedDict):
	id: str
	multipliers: Falsy[List[Any]]
	pointsEarnedBaseline: int
	pointsEarnedTotal: int
	__typename: str

class ClaimCommunityPointsResponseClaimcommunitypointsData(TypedDict):
	claim: ClaimCommunityPointsResponseClaimcommunitypointsDataClaimData
	currentPoints: int
	error: NoneType
	__typename: str

class ClaimCommunityPointsResponse(TypedDict):
	claimCommunityPoints: ClaimCommunityPointsResponseClaimcommunitypointsData

class ClipMetadataRequest(TypedDict):
	clipSlug: str

class ClipMetadataResponseCurrentuserDataSelfData(TypedDict):
	isEditor: bool
	__typename: str

class ClipMetadataResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType
	isSiteAdmin: NoneType
	__typename: str

class ClipMetadataResponseCurrentuserData(TypedDict):
	id: str
	login: str
	self: ClipMetadataResponseCurrentuserDataSelfData
	roles: ClipMetadataResponseCurrentuserDataRolesData
	__typename: str

class ClipMetadataResponseClipDataGueststarparticipantsData(TypedDict):
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]
	__typename: str

class ClipMetadataResponseClipData(TypedDict):
	id: str
	guestStarParticipants: ClipMetadataResponseClipDataGueststarparticipantsData
	__typename: str

class ClipMetadataResponseRequestinfoData(TypedDict):
	countryCode: str
	__typename: str

class ClipMetadataResponse(TypedDict):
	currentUser: Union[NoneType, ClipMetadataResponseCurrentuserData]
	clip: ClipMetadataResponseClipData
	requestInfo: ClipMetadataResponseRequestinfoData

class ClipsCards__UserRequestCriteriaData(TypedDict):
	filter: str
	shouldFilterByDiscoverySetting: bool

class ClipsCards__UserRequest(TypedDict):
	login: str
	limit: int
	criteria: ClipsCards__UserRequestCriteriaData
	cursor: Union[str, NoneType]

class ClipsCards__UserResponseUserDataClipsDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataCuratorData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	boxArtURL: str
	__typename: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: str
	roles: ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataBroadcasterDataRolesData
	__typename: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataGueststarparticipantsData(TypedDict):
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]
	__typename: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeData(TypedDict):
	id: str
	slug: str
	url: str
	embedURL: str
	title: str
	viewCount: int
	language: str
	curator: ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataCuratorData
	game: ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataGameData
	broadcaster: ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataBroadcasterData
	thumbnailURL: str
	createdAt: str
	durationSeconds: int
	champBadge: NoneType
	isFeatured: bool
	guestStarParticipants: Union[NoneType, ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataGueststarparticipantsData]
	__typename: str

class ClipsCards__UserResponseUserDataClipsDataEdgesData(TypedDict):
	cursor: Union[str, NoneType]
	node: ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeData
	__typename: str

class ClipsCards__UserResponseUserDataClipsData(TypedDict):
	pageInfo: ClipsCards__UserResponseUserDataClipsDataPageinfoData
	edges: List[ClipsCards__UserResponseUserDataClipsDataEdgesData]
	__typename: str

class ClipsCards__UserResponseUserData(TypedDict):
	id: str
	clips: ClipsCards__UserResponseUserDataClipsData
	__typename: str

class ClipsCards__UserResponse(TypedDict):
	user: ClipsCards__UserResponseUserData

class ClipsExperimentEnrollmentStatusRequest(TypedDict):
	channelID: str

class ClipsExperimentEnrollmentStatusResponseIsenrolledinclipsexperimentData(TypedDict):
	id: str
	isEnrolled: bool
	__typename: str

class ClipsExperimentEnrollmentStatusResponse(TypedDict):
	isEnrolledInClipsExperiment: ClipsExperimentEnrollmentStatusResponseIsenrolledinclipsexperimentData

class CollectionCarouselQueryRequest(TypedDict):
	includePreviewBlur: bool
	collectionID: str
	first: int

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str
	__typename: str

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	roles: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataOwnerDataRolesData
	__typename: str

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: NoneType
	__typename: str

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeData(TypedDict):
	animatedPreviewURL: str
	game: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataGameData
	id: str
	lengthSeconds: int
	owner: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	self: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataSelfData
	title: str
	viewCount: int
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	__typename: str

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesData(TypedDict):
	cursor: str
	node: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeData
	__typename: str

class CollectionCarouselQueryResponseCollectionDataItemsDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class CollectionCarouselQueryResponseCollectionDataItemsData(TypedDict):
	totalCount: int
	edges: List[CollectionCarouselQueryResponseCollectionDataItemsDataEdgesData]
	pageInfo: CollectionCarouselQueryResponseCollectionDataItemsDataPageinfoData
	__typename: str

class CollectionCarouselQueryResponseCollectionDataOwnerData(TypedDict):
	id: str
	login: str
	__typename: str

class CollectionCarouselQueryResponseCollectionData(TypedDict):
	items: CollectionCarouselQueryResponseCollectionDataItemsData
	id: str
	description: Falsy[str]
	owner: CollectionCarouselQueryResponseCollectionDataOwnerData
	thumbnailURL: str
	title: str
	type: str
	updatedAt: str
	lengthSeconds: int
	__typename: str

class CollectionCarouselQueryResponse(TypedDict):
	collection: CollectionCarouselQueryResponseCollectionData

class CommercialCommandHandler_ChannelDataRequest(TypedDict):
	channelLogin: str

class CommercialCommandHandler_ChannelDataResponseChannelDataRolesData(TypedDict):
	isPartner: bool
	isAffiliate: bool
	__typename: str

class CommercialCommandHandler_ChannelDataResponseChannelData(TypedDict):
	id: str
	roles: CommercialCommandHandler_ChannelDataResponseChannelDataRolesData
	__typename: str

class CommercialCommandHandler_ChannelDataResponse(TypedDict):
	channel: CommercialCommandHandler_ChannelDataResponseChannelData

class CommonHooks_BlockedUsersRequest(TypedDict):
	...

class CommonHooks_BlockedUsersResponseCurrentuserData(TypedDict):
	id: str
	blockedUsers: Falsy[List[Any]]
	__typename: str

class CommonHooks_BlockedUsersResponse(TypedDict):
	currentUser: Union[NoneType, CommonHooks_BlockedUsersResponseCurrentuserData]

class CommunityOnboardingAllowlistRequest(TypedDict):
	channelID: str

class CommunityOnboardingAllowlistResponseCommunityonboardingDataChannelallowlistsData(TypedDict):
	experimentName: str
	__typename: str

class CommunityOnboardingAllowlistResponseCommunityonboardingData(TypedDict):
	channelAllowLists: Falsy[List[CommunityOnboardingAllowlistResponseCommunityonboardingDataChannelallowlistsData]]
	__typename: str

class CommunityOnboardingAllowlistResponse(TypedDict):
	communityOnboarding: CommunityOnboardingAllowlistResponseCommunityonboardingData

class CommunityPointsAvailableClaimRequest(TypedDict):
	channelID: str

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData(TypedDict):
	id: str
	__typename: str

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsData(TypedDict):
	availableClaim: Union[NoneType, CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData]
	__typename: str
	balance: Falsy[int]
	activeMultipliers: Falsy[List[Any]]
	canRedeemRewardsForFree: bool

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfData(TypedDict):
	communityPoints: CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsData
	__typename: str

class CommunityPointsAvailableClaimResponseCommunityDataChannelData(TypedDict):
	id: str
	self: CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfData
	__typename: str

class CommunityPointsAvailableClaimResponseCommunityData(TypedDict):
	id: str
	login: str
	channel: CommunityPointsAvailableClaimResponseCommunityDataChannelData
	__typename: str

class CommunityPointsAvailableClaimResponse(TypedDict):
	community: CommunityPointsAvailableClaimResponseCommunityData

class CommunityPointsChatPrivateCalloutUserRequest(TypedDict):
	login: str

class CommunityPointsChatPrivateCalloutUserResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType
	isModerator: bool
	__typename: str

class CommunityPointsChatPrivateCalloutUserResponseUserData(TypedDict):
	id: str
	self: CommunityPointsChatPrivateCalloutUserResponseUserDataSelfData
	__typename: str

class CommunityPointsChatPrivateCalloutUserResponse(TypedDict):
	user: CommunityPointsChatPrivateCalloutUserResponseUserData

class CommunitySupportSettingsRequest(TypedDict):
	channelID: str

class CommunitySupportSettingsResponseUserDataSettingsDataLeaderboardData(TypedDict):
	isCheerEnabled: bool
	isSubGiftEnabled: bool
	isClipEnabled: bool
	defaultLeaderboard: str
	timePeriod: str
	__typename: str

class CommunitySupportSettingsResponseUserDataSettingsDataRecentchannelsupporteventsData(TypedDict):
	isOptedOut: bool
	__typename: str

class CommunitySupportSettingsResponseUserDataSettingsData(TypedDict):
	leaderboard: CommunitySupportSettingsResponseUserDataSettingsDataLeaderboardData
	recentChannelSupportEvents: CommunitySupportSettingsResponseUserDataSettingsDataRecentchannelsupporteventsData
	__typename: str

class CommunitySupportSettingsResponseUserData(TypedDict):
	id: str
	login: str
	settings: CommunitySupportSettingsResponseUserDataSettingsData
	__typename: str

class CommunitySupportSettingsResponse(TypedDict):
	user: CommunitySupportSettingsResponseUserData

class ConsentRequest(TypedDict):
	id: str
	includeNewCookieConsentFields: bool
	includeTCData: bool

class ConsentResponseConsentDataVendorstatusData(TypedDict):
	name: str
	consentStatus: str
	hasUserSetConsent: bool
	isVisible: bool
	__typename: str

class ConsentResponseConsentDataVendorconsentstatusDataStatusData1(TypedDict):
	name: str
	consentStatus: str
	hasUserSetConsent: bool
	isVisible: bool
	cookieVendorType: str
	features: Union[NoneType, List[str]]
	purposes: Union[NoneType, List[str]]
	flexiblePurposes: Union[NoneType, List[str]]
	specialFeatures: Union[NoneType, List[str]]
	specialPurposes: Union[NoneType, List[str]]
	policyURL: str
	cookieMaxAgeSeconds: Falsy[int]
	__typename: str

class ConsentResponseConsentDataVendorconsentstatusDataStatusData2(TypedDict):
	name: str
	consentStatus: str
	hasUserSetConsent: bool
	isVisible: bool
	cookieVendorType: str
	policyURL: str
	__typename: str

class ConsentResponseConsentDataVendorconsentstatusData(TypedDict):
	status: List[Union[ConsentResponseConsentDataVendorconsentstatusDataStatusData1, ConsentResponseConsentDataVendorconsentstatusDataStatusData2]]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataPurposeData(TypedDict):
	consents: Union[str, NoneType]
	legitimateInterests: Union[Falsy[str], NoneType]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataVendorData(TypedDict):
	consents: Union[str, NoneType]
	legitimateInterests: Union[Falsy[str], NoneType]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataTcdataData(TypedDict):
	tcString: Falsy[str]
	tcfPolicyVersion: Falsy[int]
	cmpID: Falsy[str]
	cmpVersion: Falsy[int]
	ifGDPRApplies: bool
	isServiceSpecific: bool
	hasNonStandardStacks: bool
	publisherCountryCode: Falsy[str]
	hasPurposeOneTreatment: bool
	purpose: ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataPurposeData
	vendor: ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataVendorData
	specialFeatureOptins: Union[str, NoneType]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataPurposeDataIabinformationData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: List[str]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataPurposeData(TypedDict):
	iabInformation: ConsentResponseConsentDataGdpruserpreferencesDataPurposeDataIabinformationData
	consentStatus: str
	hasUserSetConsent: bool
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataSpecialpurposeData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: List[str]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataFeaturesData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: Falsy[List[Any]]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsDataIabinformationData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: Falsy[List[Any]]
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsData(TypedDict):
	iabInformation: ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsDataIabinformationData
	consentStatus: str
	hasUserSetConsent: bool
	__typename: str

class ConsentResponseConsentDataGdpruserpreferencesData(TypedDict):
	tcData: ConsentResponseConsentDataGdpruserpreferencesDataTcdataData
	purpose: List[ConsentResponseConsentDataGdpruserpreferencesDataPurposeData]
	specialPurpose: List[ConsentResponseConsentDataGdpruserpreferencesDataSpecialpurposeData]
	features: List[ConsentResponseConsentDataGdpruserpreferencesDataFeaturesData]
	specialFeatureOptIns: List[ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsData]
	hasUserSetPurposeConsent: bool
	__typename: str

class ConsentResponseConsentDataDmauserpreferencesData(TypedDict):
	hasDmaOptIn: bool
	__typename: str

class ConsentResponseConsentData(TypedDict):
	id: str
	isDeniedUnderage: bool
	privacyLawName: str
	shouldShowNotification: bool
	shouldShowSettingsPage: bool
	shouldShowDismissButton: bool
	shouldSkipDmaBanner: bool
	vendorStatus: List[ConsentResponseConsentDataVendorstatusData]
	vendorConsentStatus: ConsentResponseConsentDataVendorconsentstatusData
	gdprUserPreferences: ConsentResponseConsentDataGdpruserpreferencesData
	dmaUserPreferences: ConsentResponseConsentDataDmauserpreferencesData
	__typename: str

class ConsentResponse(TypedDict):
	consent: ConsentResponseConsentData

class ContentClassificationContextRequest1(TypedDict):
	clipSlug: Falsy[str]
	isStream: bool
	isClip: bool
	isVOD: bool
	login: str

class ContentClassificationContextRequest2(TypedDict):
	clipSlug: Falsy[str]
	isStream: bool
	isClip: bool
	isVOD: bool
	vodID: str

class ContentClassificationContextRequest3(TypedDict):
	clipSlug: str
	isStream: bool
	isClip: bool
	isVOD: bool

class ContentClassificationContextResponse1UserDataStreamDataGameData(TypedDict):
	id: str
	name: str
	__typename: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelsData(TypedDict):
	id: str
	localizedName: str
	__typename: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	signPost: str
	contentClassificationLabels: Falsy[List[str]]
	__typename: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	contentGate: str
	__typename: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesData(TypedDict):
	signPostProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData
	contentGateProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData
	__typename: str

class ContentClassificationContextResponse1UserDataStreamData(TypedDict):
	id: str
	game: ContentClassificationContextResponse1UserDataStreamDataGameData
	contentClassificationLabels: Falsy[List[ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelsData]]
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesData
	__typename: str

class ContentClassificationContextResponse1UserData(TypedDict):
	id: str
	stream: Union[NoneType, ContentClassificationContextResponse1UserDataStreamData]
	displayName: str
	__typename: str

class ContentClassificationContextResponse1(TypedDict):
	user: ContentClassificationContextResponse1UserData

class ContentClassificationContextResponse2VideoDataGameData(TypedDict):
	id: str
	name: str
	__typename: str

class ContentClassificationContextResponse2VideoDataOwnerData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelsData(TypedDict):
	id: str
	localizedName: str
	__typename: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	signPost: str
	contentClassificationLabels: Falsy[List[str]]
	__typename: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	contentGate: str
	__typename: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesData(TypedDict):
	signPostProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData
	contentGateProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData
	__typename: str

class ContentClassificationContextResponse2VideoData(TypedDict):
	id: str
	broadcastType: str
	game: ContentClassificationContextResponse2VideoDataGameData
	owner: ContentClassificationContextResponse2VideoDataOwnerData
	contentClassificationLabels: Falsy[List[ContentClassificationContextResponse2VideoDataContentclassificationlabelsData]]
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesData
	__typename: str

class ContentClassificationContextResponse2(TypedDict):
	video: ContentClassificationContextResponse2VideoData

class ContentClassificationContextResponse3ClipDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	__typename: str

class ContentClassificationContextResponse3ClipDataGameData(TypedDict):
	id: str
	name: str
	__typename: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelsData(TypedDict):
	id: str
	localizedName: str
	__typename: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	signPost: str
	contentClassificationLabels: Falsy[List[str]]
	__typename: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	contentGate: str
	__typename: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesData(TypedDict):
	signPostProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData
	contentGateProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData
	__typename: str

class ContentClassificationContextResponse3ClipData(TypedDict):
	id: str
	slug: str
	broadcaster: ContentClassificationContextResponse3ClipDataBroadcasterData
	game: ContentClassificationContextResponse3ClipDataGameData
	contentClassificationLabels: Falsy[List[ContentClassificationContextResponse3ClipDataContentclassificationlabelsData]]
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesData
	__typename: str

class ContentClassificationContextResponse3(TypedDict):
	clip: ContentClassificationContextResponse3ClipData

class ContentPolicyPropertiesQueryRequest(TypedDict):
	login: Falsy[str]
	vodID: Falsy[str]
	isLive: bool
	isVOD: bool

class ContentPolicyPropertiesQueryResponse1UserDataStreamDataContentpolicypropertiesData(TypedDict):
	hasBrandedContent: bool
	__typename: str

class ContentPolicyPropertiesQueryResponse1UserDataStreamData(TypedDict):
	id: str
	contentPolicyProperties: ContentPolicyPropertiesQueryResponse1UserDataStreamDataContentpolicypropertiesData
	__typename: str

class ContentPolicyPropertiesQueryResponse1UserData(TypedDict):
	id: str
	stream: Union[NoneType, ContentPolicyPropertiesQueryResponse1UserDataStreamData]
	__typename: str

class ContentPolicyPropertiesQueryResponse1(TypedDict):
	user: ContentPolicyPropertiesQueryResponse1UserData

class ContentPolicyPropertiesQueryResponse2VideoDataContentpolicypropertiesData(TypedDict):
	hasBrandedContent: bool
	__typename: str

class ContentPolicyPropertiesQueryResponse2VideoDataOwnerData(TypedDict):
	id: str
	login: str
	__typename: str

class ContentPolicyPropertiesQueryResponse2VideoData(TypedDict):
	id: str
	broadcastType: str
	contentPolicyProperties: ContentPolicyPropertiesQueryResponse2VideoDataContentpolicypropertiesData
	owner: ContentPolicyPropertiesQueryResponse2VideoDataOwnerData
	__typename: str

class ContentPolicyPropertiesQueryResponse2(TypedDict):
	video: ContentPolicyPropertiesQueryResponse2VideoData

class CoreActionsCurrentUserRequest(TypedDict):
	...

class CoreActionsCurrentUserResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType
	__typename: str

class CoreActionsCurrentUserResponseCurrentuserDataSettingsData(TypedDict):
	preferredLanguageTag: str
	__typename: str

class CoreActionsCurrentUserResponseCurrentuserData(TypedDict):
	displayName: str
	id: str
	login: str
	roles: CoreActionsCurrentUserResponseCurrentuserDataRolesData
	settings: CoreActionsCurrentUserResponseCurrentuserDataSettingsData
	__typename: str

class CoreActionsCurrentUserResponse(TypedDict):
	currentUser: CoreActionsCurrentUserResponseCurrentuserData

class CurrentUserBannedStatusRequest(TypedDict):
	channelLogin: str

class CurrentUserBannedStatusResponseChannelDataSelfData(TypedDict):
	banStatus: NoneType
	__typename: str

class CurrentUserBannedStatusResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, CurrentUserBannedStatusResponseChannelDataSelfData]
	__typename: str

class CurrentUserBannedStatusResponse(TypedDict):
	channel: CurrentUserBannedStatusResponseChannelData

class CurrentUserModeratorStatusRequest1(TypedDict):
	channelID: str

class CurrentUserModeratorStatusRequest2(TypedDict):
	channelLogin: str

class CurrentUserModeratorStatusResponseUserDataSelfData(TypedDict):
	isModerator: bool
	__typename: str

class CurrentUserModeratorStatusResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, CurrentUserModeratorStatusResponseUserDataSelfData]
	__typename: str

class CurrentUserModeratorStatusResponseCurrentuserData(TypedDict):
	id: str
	__typename: str

class CurrentUserModeratorStatusResponse(TypedDict):
	user: CurrentUserModeratorStatusResponseUserData
	currentUser: Union[NoneType, CurrentUserModeratorStatusResponseCurrentuserData]

class CurrentUserStrikeStatusRequest(TypedDict):
	channelLogin: str

class CurrentUserStrikeStatusResponseChannelDataSelfDataChatmoderatorstrikestatusData(TypedDict):
	id: str
	banDetails: NoneType
	timeoutDetails: NoneType
	warningDetails: NoneType
	__typename: str

class CurrentUserStrikeStatusResponseChannelDataSelfData(TypedDict):
	chatModeratorStrikeStatus: CurrentUserStrikeStatusResponseChannelDataSelfDataChatmoderatorstrikestatusData
	__typename: str

class CurrentUserStrikeStatusResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, CurrentUserStrikeStatusResponseChannelDataSelfData]
	__typename: str

class CurrentUserStrikeStatusResponse(TypedDict):
	channel: CurrentUserStrikeStatusResponseChannelData

class DirectoryCollection_BrowsableCollectionRequest1OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class DirectoryCollection_BrowsableCollectionRequest1OptionsData(TypedDict):
	requestID: str
	recommendationsContext: DirectoryCollection_BrowsableCollectionRequest1OptionsDataRecommendationscontextData

class DirectoryCollection_BrowsableCollectionRequest1(TypedDict):
	limit: int
	imageWidth: int
	slug: str
	options: DirectoryCollection_BrowsableCollectionRequest1OptionsData
	includeIsDJ: bool

class DirectoryCollection_BrowsableCollectionRequest2OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class DirectoryCollection_BrowsableCollectionRequest2OptionsData(TypedDict):
	requestID: str
	recommendationsContext: DirectoryCollection_BrowsableCollectionRequest2OptionsDataRecommendationscontextData

class DirectoryCollection_BrowsableCollectionRequest2(TypedDict):
	limit: int
	imageWidth: int
	slug: str
	options: DirectoryCollection_BrowsableCollectionRequest2OptionsData
	includeIsDJ: bool
	cursor: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataNameData(TypedDict):
	fallbackLocalizedTitle: str
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataDescriptionData(TypedDict):
	fallbackLocalizedTitle: NoneType
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	roles: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataBroadcasterDataRolesData
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataFreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	slug: str
	boxArtURL: str
	name: str
	displayName: str
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	viewersCount: int
	previewImageURL: str
	broadcaster: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataBroadcasterData
	freeformTags: List[DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataFreeformtagsData]
	type: str
	game: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataGameData
	previewThumbnailProperties: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataPreviewthumbnailpropertiesData
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesData(TypedDict):
	cursor: str
	node: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeData
	trackingID: str
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsData(TypedDict):
	pageInfo: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataPageinfoData
	edges: List[DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesData]
	__typename: str

class DirectoryCollection_BrowsableCollectionResponseCollectionData(TypedDict):
	id: str
	slug: str
	name: DirectoryCollection_BrowsableCollectionResponseCollectionDataNameData
	description: DirectoryCollection_BrowsableCollectionResponseCollectionDataDescriptionData
	__typename: str
	streams: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsData

class DirectoryCollection_BrowsableCollectionResponse(TypedDict):
	collection: DirectoryCollection_BrowsableCollectionResponseCollectionData

class DropCurrentSessionContextRequest(TypedDict):
	channelLogin: str

class DropCurrentSessionContextResponseCurrentuserDataDropcurrentsessionData(TypedDict):
	channel: NoneType
	game: NoneType
	currentMinutesWatched: Falsy[int]
	requiredMinutesWatched: Falsy[int]
	dropID: Falsy[str]
	__typename: str

class DropCurrentSessionContextResponseCurrentuserData(TypedDict):
	id: str
	dropCurrentSession: DropCurrentSessionContextResponseCurrentuserDataDropcurrentsessionData
	__typename: str

class DropCurrentSessionContextResponse(TypedDict):
	currentUser: Union[NoneType, DropCurrentSessionContextResponseCurrentuserData]

class DropsHighlightService_AvailableDropsRequest(TypedDict):
	channelID: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataGameData(TypedDict):
	id: str
	name: str
	__typename: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitDataGameData(TypedDict):
	name: str
	id: str
	__typename: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitData(TypedDict):
	id: str
	name: str
	game: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitDataGameData
	imageAssetURL: str
	__typename: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesData(TypedDict):
	benefit: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitData
	entitlementLimit: int
	__typename: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsData(TypedDict):
	id: str
	name: str
	startAt: str
	endAt: str
	benefitEdges: List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesData]
	requiredMinutesWatched: int
	requiredSubs: Falsy[int]
	__typename: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataSummaryData(TypedDict):
	includesMWRequirement: bool
	includesSubRequirement: bool
	isSitewide: bool
	isRewardCampaign: bool
	isPermanentlyDismissible: bool
	__typename: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsData(TypedDict):
	id: str
	name: str
	game: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataGameData
	detailsURL: str
	endAt: str
	imageURL: str
	eventBasedDrops: Falsy[List[Any]]
	timeBasedDrops: List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsData]
	summary: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataSummaryData
	__typename: str

class DropsHighlightService_AvailableDropsResponseChannelData(TypedDict):
	id: str
	viewerDropCampaigns: Union[NoneType, List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsData]]
	__typename: str

class DropsHighlightService_AvailableDropsResponse(TypedDict):
	channel: DropsHighlightService_AvailableDropsResponseChannelData

class EmotesForChannelFollowStatusRequest(TypedDict):
	channelID: str

class EmotesForChannelFollowStatusResponseUserDataSelfDataFollowerData(TypedDict):
	followedAt: str
	__typename: str

class EmotesForChannelFollowStatusResponseUserDataSelfData(TypedDict):
	follower: Union[NoneType, EmotesForChannelFollowStatusResponseUserDataSelfDataFollowerData]
	__typename: str

class EmotesForChannelFollowStatusResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, EmotesForChannelFollowStatusResponseUserDataSelfData]
	__typename: str

class EmotesForChannelFollowStatusResponse(TypedDict):
	user: EmotesForChannelFollowStatusResponseUserData

class FeaturedClipsShelfCoverRequest(TypedDict):
	channelID: str

class FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsDataEmotesData(TypedDict):
	id: str
	assetType: str
	order: Falsy[int]
	subscriptionTier: str
	token: str
	__typename: str

class FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsData(TypedDict):
	id: str
	emotes: Falsy[List[FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsDataEmotesData]]
	__typename: str

class FeaturedClipsShelfCoverResponseUserData(TypedDict):
	id: str
	subscriptionProducts: List[FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsData]
	__typename: str

class FeaturedClipsShelfCoverResponse(TypedDict):
	user: FeaturedClipsShelfCoverResponseUserData

class FeaturedContentCarouselStreamsRequest(TypedDict):
	language: str
	first: int
	acceptedMature: bool

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataBroadcasterData(TypedDict):
	displayName: str
	id: str
	profileImageURL: str
	login: str
	__typename: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	__typename: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamData(TypedDict):
	broadcaster: FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataBroadcasterData
	game: FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataGameData
	id: str
	type: str
	viewersCount: int
	previewImageURL: str
	freeformTags: List[FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataFreeformtagsData]
	__typename: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsData(TypedDict):
	itemTrackingID: str
	isScheduled: bool
	isSponsored: bool
	priorityLevel: int
	description: Falsy[str]
	stream: FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamData
	title: Falsy[str]
	version: int
	__typename: str

class FeaturedContentCarouselStreamsResponse(TypedDict):
	featuredStreams: List[FeaturedContentCarouselStreamsResponseFeaturedstreamsData]

class FilterableVideoTower_VideosRequest1(TypedDict):
	includePreviewBlur: bool
	limit: int
	channelOwnerLogin: str
	broadcastType: Union[NoneType, str]
	videoSort: str

class FilterableVideoTower_VideosRequest2(TypedDict):
	includePreviewBlur: bool
	limit: int
	channelOwnerLogin: str
	broadcastType: Union[NoneType, str]
	videoSort: str
	cursor: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	roles: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataOwnerDataRolesData
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataSelfDataViewinghistoryData(TypedDict):
	position: Union[NoneType, int]
	updatedAt: Union[NoneType, str]
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: Union[NoneType, FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataSelfDataViewinghistoryData]
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeData(TypedDict):
	animatedPreviewURL: str
	game: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataGameData
	id: str
	lengthSeconds: int
	owner: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	self: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataSelfData
	title: str
	viewCount: int
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesData(TypedDict):
	cursor: Union[NoneType, str]
	node: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeData
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class FilterableVideoTower_VideosResponseUserDataVideosData(TypedDict):
	edges: List[FilterableVideoTower_VideosResponseUserDataVideosDataEdgesData]
	pageInfo: FilterableVideoTower_VideosResponseUserDataVideosDataPageinfoData
	__typename: str

class FilterableVideoTower_VideosResponseUserData(TypedDict):
	id: str
	videos: FilterableVideoTower_VideosResponseUserDataVideosData
	__typename: str

class FilterableVideoTower_VideosResponse(TypedDict):
	user: FilterableVideoTower_VideosResponseUserData

class FollowButton_FollowUserRequestInputData(TypedDict):
	disableNotifications: bool
	targetID: str

class FollowButton_FollowUserRequest(TypedDict):
	input: FollowButton_FollowUserRequestInputData

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool
	followedAt: str
	__typename: str

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfData(TypedDict):
	canFollow: bool
	follower: FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfDataFollowerData
	__typename: str

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfData
	__typename: str

class FollowButton_FollowUserResponseFollowuserDataFollowData(TypedDict):
	disableNotifications: bool
	user: FollowButton_FollowUserResponseFollowuserDataFollowDataUserData
	__typename: str

class FollowButton_FollowUserResponseFollowuserData(TypedDict):
	follow: FollowButton_FollowUserResponseFollowuserDataFollowData
	error: NoneType
	__typename: str

class FollowButton_FollowUserResponse(TypedDict):
	followUser: FollowButton_FollowUserResponseFollowuserData

class FollowButton_UnfollowUserRequestInputData(TypedDict):
	targetID: str

class FollowButton_UnfollowUserRequest(TypedDict):
	input: FollowButton_UnfollowUserRequestInputData

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserDataSelfData(TypedDict):
	canFollow: bool
	follower: NoneType
	__typename: str

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserDataSelfData
	__typename: str

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowData(TypedDict):
	disableNotifications: bool
	user: FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserData
	__typename: str

class FollowButton_UnfollowUserResponseUnfollowuserData(TypedDict):
	follow: FollowButton_UnfollowUserResponseUnfollowuserDataFollowData
	__typename: str

class FollowButton_UnfollowUserResponse(TypedDict):
	unfollowUser: FollowButton_UnfollowUserResponseUnfollowuserData

class FollowButton_UserRequest(TypedDict):
	login: str

class FollowButton_UserResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool
	followedAt: str
	__typename: str

class FollowButton_UserResponseUserDataSelfData(TypedDict):
	canFollow: bool
	follower: Union[NoneType, FollowButton_UserResponseUserDataSelfDataFollowerData]
	__typename: str

class FollowButton_UserResponseUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: Union[NoneType, FollowButton_UserResponseUserDataSelfData]
	__typename: str

class FollowButton_UserResponse(TypedDict):
	user: FollowButton_UserResponseUserData

class FollowedIndex_CurrentUserRequest(TypedDict):
	...

class FollowedIndex_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	__typename: str

class FollowedIndex_CurrentUserResponse(TypedDict):
	currentUser: FollowedIndex_CurrentUserResponseCurrentuserData

class FollowedIndex_FollowCountRequest(TypedDict):
	...

class FollowedIndex_FollowCountResponseCurrentuserDataFollowsData(TypedDict):
	totalCount: int
	__typename: str

class FollowedIndex_FollowCountResponseCurrentuserData(TypedDict):
	id: str
	follows: FollowedIndex_FollowCountResponseCurrentuserDataFollowsData
	__typename: str

class FollowedIndex_FollowCountResponse(TypedDict):
	currentUser: FollowedIndex_FollowCountResponseCurrentuserData

class FollowedStreamsRequest(TypedDict):
	userID: str
	limit: int

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerDataSubscriptionproductsDataEmotesData(TypedDict):
	id: str
	order: Falsy[int]
	subscriptionTier: str
	token: str
	assetType: str
	__typename: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerDataSubscriptionproductsData(TypedDict):
	id: str
	emotes: Falsy[List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerDataSubscriptionproductsDataEmotesData]]
	__typename: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerData(TypedDict):
	id: str
	displayName: str
	login: str
	isPartner: bool
	profileImageURL: str
	primaryColorHex: str
	bannerImageURL: str
	subscriptionProducts: List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerDataSubscriptionproductsData]
	__typename: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelData(TypedDict):
	id: str
	owner: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerData
	__typename: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	startAt: str
	categories: Falsy[List[Any]]
	hasReminder: bool
	baseSegmentID: str
	repeatEndsAfterCount: Falsy[int]
	channel: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelData
	__typename: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesData(TypedDict):
	node: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeData
	__typename: str

class FollowedStreamsResponseFollowedupcomingstreamsData(TypedDict):
	edges: List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesData]
	__typename: str

class FollowedStreamsResponse(TypedDict):
	followedUpcomingStreams: FollowedStreamsResponseFollowedupcomingstreamsData

class FollowedStreamsContinueWatchingRequest(TypedDict):
	includePreviewBlur: bool
	limit: int

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData(TypedDict):
	position: Falsy[int]
	updatedAt: str
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	roles: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataOwnerDataRolesData
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData(TypedDict):
	position: Falsy[int]
	updatedAt: str
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeData(TypedDict):
	animatedPreviewURL: str
	game: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataGameData
	id: str
	lengthSeconds: int
	owner: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	self: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataSelfData
	title: str
	viewCount: int
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesData(TypedDict):
	history: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData
	node: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeData
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosData(TypedDict):
	edges: List[FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesData]
	__typename: str

class FollowedStreamsContinueWatchingResponseCurrentuserData(TypedDict):
	id: str
	viewedVideos: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosData
	__typename: str

class FollowedStreamsContinueWatchingResponse(TypedDict):
	currentUser: FollowedStreamsContinueWatchingResponseCurrentuserData

class FollowedVideos_CurrentUserRequest(TypedDict):
	includePreviewBlur: bool
	limit: int

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowsData(TypedDict):
	totalCount: int
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	roles: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataOwnerDataRolesData
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData(TypedDict):
	position: Union[NoneType, int]
	updatedAt: Union[NoneType, str]
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeData(TypedDict):
	animatedPreviewURL: str
	game: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataGameData
	id: str
	lengthSeconds: int
	owner: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	self: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataSelfData
	title: str
	viewCount: int
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesData(TypedDict):
	cursor: str
	node: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeData
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosData(TypedDict):
	pageInfo: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataPageinfoData
	edges: List[FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesData]
	__typename: str

class FollowedVideos_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	follows: FollowedVideos_CurrentUserResponseCurrentuserDataFollowsData
	followedVideos: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosData
	__typename: str

class FollowedVideos_CurrentUserResponse(TypedDict):
	currentUser: FollowedVideos_CurrentUserResponseCurrentuserData

class FollowingGames_CurrentUserRequest(TypedDict):
	limit: int
	type: str

class FollowingGames_CurrentUserResponseCurrentuserDataFollowedgamesData(TypedDict):
	nodes: Falsy[List[Any]]
	__typename: str

class FollowingGames_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	followedGames: FollowingGames_CurrentUserResponseCurrentuserDataFollowedgamesData
	__typename: str

class FollowingGames_CurrentUserResponse(TypedDict):
	currentUser: FollowingGames_CurrentUserResponseCurrentuserData

class FollowingLive_CurrentUserRequest(TypedDict):
	imageWidth: int
	limit: int
	includeIsDJ: bool

class FollowingLive_CurrentUserResponseCurrentuserDataFollowsData(TypedDict):
	totalCount: int
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	boxArtURL: str
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelDataSelfData(TypedDict):
	isAuthorized: bool
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelData(TypedDict):
	id: str
	self: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelDataSelfData
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterData(TypedDict):
	id: str
	primaryColorHex: str
	roles: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataRolesData
	channel: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelData
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamData(TypedDict):
	id: str
	game: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataGameData
	viewersCount: int
	title: str
	type: str
	previewImageURL: str
	freeformTags: List[FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataFreeformtagsData]
	restriction: NoneType
	broadcaster: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterData
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	stream: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamData
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesData(TypedDict):
	node: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeData
	cursor: str
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersData(TypedDict):
	edges: List[FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesData]
	pageInfo: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataPageinfoData
	__typename: str

class FollowingLive_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	follows: FollowingLive_CurrentUserResponseCurrentuserDataFollowsData
	followedLiveUsers: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersData
	__typename: str

class FollowingLive_CurrentUserResponse(TypedDict):
	currentUser: FollowingLive_CurrentUserResponseCurrentuserData

class FollowingPage_RecommendedChannelsRequestContextData(TypedDict):
	platform: str

class FollowingPage_RecommendedChannelsRequest(TypedDict):
	imageWidth: int
	context: FollowingPage_RecommendedChannelsRequestContextData
	first: int
	language: Falsy[str]
	location: str
	recRequestID: str
	includeIsDJ: bool

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterData(TypedDict):
	id: str
	broadcastSettings: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterDataBroadcastsettingsData
	displayName: str
	login: str
	profileImageURL: str
	largeProfileImageURL: str
	primaryColorHex: Union[NoneType, str]
	roles: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterDataRolesData
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameDataGametagsData(TypedDict):
	id: str
	isLanguageTag: bool
	localizedName: str
	tagName: str
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	categorySlug: str
	name: str
	viewersCount: int
	displayName: str
	boxArtURL: str
	gameTags: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameDataGametagsData]
	originalReleaseDate: Union[NoneType, str]
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataFreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeData(TypedDict):
	id: str
	broadcaster: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterData
	game: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameData
	freeformTags: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataFreeformtagsData]
	viewersCount: int
	previewImageURL: str
	createdAt: str
	type: str
	__typename: str
	previewThumbnailProperties: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataPreviewthumbnailpropertiesData

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesData(TypedDict):
	node: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeData
	trackingID: str
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsData(TypedDict):
	edges: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesData]
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsData(TypedDict):
	liveRecommendations: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsData
	__typename: str

class FollowingPage_RecommendedChannelsResponseCurrentuserData(TypedDict):
	id: str
	recommendations: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsData
	__typename: str

class FollowingPage_RecommendedChannelsResponse(TypedDict):
	currentUser: FollowingPage_RecommendedChannelsResponseCurrentuserData

class FrontPageNew_UserRequest(TypedDict):
	limit: int

class FrontPageNew_UserResponseCurrentuserDataFollowedgamesData(TypedDict):
	nodes: Falsy[List[Any]]
	__typename: str

class FrontPageNew_UserResponseCurrentuserDataRolesData(TypedDict):
	isPartner: bool
	isStaff: NoneType
	__typename: str

class FrontPageNew_UserResponseCurrentuserData(TypedDict):
	id: str
	createdAt: str
	followedGames: FrontPageNew_UserResponseCurrentuserDataFollowedgamesData
	roles: FrontPageNew_UserResponseCurrentuserDataRolesData
	__typename: str

class FrontPageNew_UserResponse(TypedDict):
	currentUser: Union[NoneType, FrontPageNew_UserResponseCurrentuserData]

class GetDisplayNameRequest(TypedDict):
	login: Falsy[str]

class GetDisplayNameResponseUserData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class GetDisplayNameResponse(TypedDict):
	user: Union[NoneType, GetDisplayNameResponseUserData]

class GetGuestSessionBlocksAndBansRequestSessionoptionsData(TypedDict):
	channelID: str

class GetGuestSessionBlocksAndBansRequest(TypedDict):
	channelID: str
	sessionOptions: GetGuestSessionBlocksAndBansRequestSessionoptionsData

class GetGuestSessionBlocksAndBansResponseUserDataSelfData(TypedDict):
	canFollow: bool
	banStatus: NoneType
	__typename: str

class GetGuestSessionBlocksAndBansResponseUserData(TypedDict):
	id: str
	self: GetGuestSessionBlocksAndBansResponseUserDataSelfData
	__typename: str

class GetGuestSessionBlocksAndBansResponse(TypedDict):
	user: GetGuestSessionBlocksAndBansResponseUserData
	guestStarSession: NoneType

class GetIDFromLoginRequest(TypedDict):
	login: str

class GetIDFromLoginResponseUserData(TypedDict):
	id: str
	__typename: str

class GetIDFromLoginResponse(TypedDict):
	user: GetIDFromLoginResponseUserData

class GetPinnedChatRequest(TypedDict):
	channelID: str
	count: int

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsDataContentData(TypedDict):
	emoteID: str
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsData(TypedDict):
	content: Union[NoneType, GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsDataContentData]
	text: str
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentData(TypedDict):
	text: str
	fragments: List[GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsData]
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderDataDisplaybadgesData(TypedDict):
	id: str
	setID: str
	version: str
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderData(TypedDict):
	id: str
	chatColor: Union[NoneType, str]
	displayName: str
	displayBadges: List[GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderDataDisplaybadgesData]
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageData(TypedDict):
	id: str
	content: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentData
	parentMessage: NoneType
	threadParentMessage: NoneType
	sentAt: str
	sender: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderData
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedbyData(TypedDict):
	id: str
	displayName: str
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeData(TypedDict):
	id: str
	type: str
	pinnedMessage: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageData
	startsAt: str
	updatedAt: str
	endsAt: NoneType
	pinnedBy: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedbyData
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesData(TypedDict):
	node: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeData
	cursor: Falsy[str]
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesData(TypedDict):
	edges: Falsy[List[GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesData]]
	pageInfo: GetPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData
	__typename: str

class GetPinnedChatResponseChannelData(TypedDict):
	id: str
	pinnedChatMessages: GetPinnedChatResponseChannelDataPinnedchatmessagesData
	__typename: str

class GetPinnedChatResponse(TypedDict):
	channel: GetPinnedChatResponseChannelData

class GetUserIDRequest(TypedDict):
	login: str
	lookupType: str

class GetUserIDResponseUserData(TypedDict):
	id: str
	__typename: str

class GetUserIDResponse(TypedDict):
	user: GetUserIDResponseUserData

class GlobalBadgesRequest(TypedDict):
	...

class GlobalBadgesResponseBadgesData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: Union[NoneType, str]
	clickURL: Union[NoneType, str]
	__typename: str

class GlobalBadgesResponse(TypedDict):
	badges: List[GlobalBadgesResponseBadgesData]

class GuestListQueryRequest(TypedDict):
	channelID: str

class GuestListQueryResponseChannelData(TypedDict):
	id: str
	guestStarSessionCall: NoneType
	__typename: str

class GuestListQueryResponse(TypedDict):
	channel: GuestListQueryResponseChannelData

class GuestStarActiveJoinRequestRequest(TypedDict):
	...

class GuestStarActiveJoinRequestResponse(TypedDict):
	guestStarActiveJoinRequest: NoneType

class GuestStarBatchCollaborationQueryRequestOptionsData(TypedDict):
	channelIDs: Falsy[List[str]]

class GuestStarBatchCollaborationQueryRequest(TypedDict):
	options: GuestStarBatchCollaborationQueryRequestOptionsData
	canDropInFlagEnabled: bool
	openCallingFlagEnabled: bool

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: str
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: int
	viewersCount: int
	id: str
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: str
	description: str
	stream: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserData
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsData]
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionData]
	canJoinStatus: str
	isFavorite: bool
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: Union[NoneType, str]
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: Union[NoneType, int]
	viewersCount: int
	id: str
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: Union[NoneType, str]
	description: Falsy[str]
	stream: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserData
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsData]
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionData]
	canDropIn: bool
	canJoinStatus: str
	isFavorite: bool
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: str
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: int
	viewersCount: int
	id: str
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: str
	description: str
	stream: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserData
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsData]
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionData]
	canJoinStatus: str
	isFavorite: bool
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: Union[NoneType, str]
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: Union[NoneType, int]
	viewersCount: int
	id: str
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str
	primaryColorHex: Union[NoneType, str]
	description: Falsy[str]
	stream: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserData
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsData]
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionData]
	canDropIn: bool
	canJoinStatus: str
	isFavorite: bool
	__typename: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesData(TypedDict):
	shouldRefetch: bool
	shouldSubscribeToUpdates: bool
	channelCollabs: Falsy[List[Union[GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1, GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2]]]
	__typename: str

class GuestStarBatchCollaborationQueryResponse(TypedDict):
	guestStarChannelCollaboration: Falsy[List[Union[GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1, GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2]]]
	guestStarCollaborationStatuses: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesData

class GuestStarChannelPageCollaborationQueryRequestOptionsData(TypedDict):
	channelIDs: List[str]

class GuestStarChannelPageCollaborationQueryRequest(TypedDict):
	options: GuestStarChannelPageCollaborationQueryRequestOptionsData
	openCallingIsEnabled: bool

class GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData(TypedDict):
	id: str
	session: NoneType
	canJoinStatus: str
	isFavorite: bool
	__typename: str

class GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesData(TypedDict):
	shouldRefetch: bool
	shouldSubscribeToUpdates: bool
	channelCollabs: List[GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData]
	__typename: str

class GuestStarChannelPageCollaborationQueryResponse(TypedDict):
	guestStarCollaborationStatuses: GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesData

class HappeningNowSettingsRequest(TypedDict):
	...

class HappeningNowSettingsResponseCurrentuserData(TypedDict):
	id: str
	isChatHappeningNowEnabled: bool
	__typename: str

class HappeningNowSettingsResponse(TypedDict):
	currentUser: HappeningNowSettingsResponseCurrentuserData

class HomeOfflineCarouselRequest(TypedDict):
	channelLogin: str
	includeTrailerUpsell: bool
	trailerUpsellVideoID: str

class HomeOfflineCarouselResponseUserDataChannelDataHomeData(TypedDict):
	autohostCarouselCard: NoneType
	__typename: str

class HomeOfflineCarouselResponseUserDataChannelDataSocialmediasData(TypedDict):
	id: str
	name: str
	title: str
	url: str
	__typename: str

class HomeOfflineCarouselResponseUserDataChannelDataScheduleDataNextsegmentData(TypedDict):
	id: str
	startAt: str
	__typename: str

class HomeOfflineCarouselResponseUserDataChannelDataScheduleData(TypedDict):
	id: str
	nextSegment: Union[NoneType, HomeOfflineCarouselResponseUserDataChannelDataScheduleDataNextsegmentData]
	__typename: str

class HomeOfflineCarouselResponseUserDataChannelDataTrailerData(TypedDict):
	video: NoneType
	__typename: str

class HomeOfflineCarouselResponseUserDataChannelData(TypedDict):
	id: str
	home: HomeOfflineCarouselResponseUserDataChannelDataHomeData
	socialMedias: Falsy[List[HomeOfflineCarouselResponseUserDataChannelDataSocialmediasData]]
	schedule: Union[NoneType, HomeOfflineCarouselResponseUserDataChannelDataScheduleData]
	trailer: HomeOfflineCarouselResponseUserDataChannelDataTrailerData
	__typename: str

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str
	displayName: str
	__typename: str

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	description: NoneType
	previewThumbnailURL: str
	publishedAt: str
	owner: HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataOwnerData
	game: HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataGameData
	__typename: str

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesData(TypedDict):
	node: HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeData
	__typename: str

class HomeOfflineCarouselResponseUserDataArchivevideosData(TypedDict):
	edges: Falsy[List[HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesData]]
	__typename: str

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str
	displayName: str
	__typename: str

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	description: NoneType
	previewThumbnailURL: str
	publishedAt: str
	owner: HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataOwnerData
	game: HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataGameData
	__typename: str

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesData(TypedDict):
	node: HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeData
	__typename: str

class HomeOfflineCarouselResponseUserDataHighlightvideosData(TypedDict):
	edges: Falsy[List[HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesData]]
	__typename: str

class HomeOfflineCarouselResponseUserDataRolesData(TypedDict):
	isPartner: bool
	isAffiliate: bool
	isStaff: NoneType
	__typename: str

class HomeOfflineCarouselResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool
	__typename: str

class HomeOfflineCarouselResponseUserDataSelfData(TypedDict):
	isEditor: bool
	follower: Union[NoneType, HomeOfflineCarouselResponseUserDataSelfDataFollowerData]
	subscriptionBenefit: NoneType
	__typename: str

class HomeOfflineCarouselResponseUserData(TypedDict):
	id: str
	login: str
	displayName: str
	description: str
	channel: HomeOfflineCarouselResponseUserDataChannelData
	archiveVideos: HomeOfflineCarouselResponseUserDataArchivevideosData
	highlightVideos: HomeOfflineCarouselResponseUserDataHighlightvideosData
	roles: HomeOfflineCarouselResponseUserDataRolesData
	self: Union[NoneType, HomeOfflineCarouselResponseUserDataSelfData]
	__typename: str

class HomeOfflineCarouselResponse(TypedDict):
	user: HomeOfflineCarouselResponseUserData

class HomeShelfEditorRequest(TypedDict):
	channelLogin: str

class HomeShelfEditorResponseUserDataSelfData(TypedDict):
	isEditor: bool
	__typename: str

class HomeShelfEditorResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, HomeShelfEditorResponseUserDataSelfData]
	__typename: str

class HomeShelfEditorResponse(TypedDict):
	user: HomeShelfEditorResponseUserData

class HomeShelfGamesRequest(TypedDict):
	channelLogin: str

class HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfDataEdgesDataNodeData(TypedDict):
	id: str
	boxArtURL: str
	displayName: str
	name: str
	viewersCount: Union[NoneType, int]
	__typename: str

class HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfDataEdgesData(TypedDict):
	node: HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfDataEdgesDataNodeData
	__typename: str

class HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfData(TypedDict):
	edges: Falsy[List[HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfDataEdgesData]]
	__typename: str

class HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesData(TypedDict):
	categoryShelf: HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfData
	__typename: str

class HomeShelfGamesResponseUserDataChannelDataHomeData(TypedDict):
	shelves: HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesData
	__typename: str

class HomeShelfGamesResponseUserDataChannelData(TypedDict):
	id: str
	home: HomeShelfGamesResponseUserDataChannelDataHomeData
	__typename: str

class HomeShelfGamesResponseUserData(TypedDict):
	id: str
	primaryColorHex: Union[NoneType, str]
	channel: HomeShelfGamesResponseUserDataChannelData
	__typename: str

class HomeShelfGamesResponse(TypedDict):
	user: HomeShelfGamesResponseUserData

class HomeShelfUsersRequest(TypedDict):
	channelLogin: str

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesDataNodeData(TypedDict):
	id: str
	displayName: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	stream: NoneType
	__typename: str

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesData(TypedDict):
	trackingID: str
	node: HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesDataNodeData
	__typename: str

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfData(TypedDict):
	type: str
	edges: Falsy[List[HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesData]]
	__typename: str

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesData(TypedDict):
	streamerShelf: HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfData
	__typename: str

class HomeShelfUsersResponseUserDataChannelDataHomeData(TypedDict):
	shelves: HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesData
	__typename: str

class HomeShelfUsersResponseUserDataChannelData(TypedDict):
	id: str
	home: HomeShelfUsersResponseUserDataChannelDataHomeData
	__typename: str

class HomeShelfUsersResponseUserDataPrimaryteamData(TypedDict):
	id: str
	name: str
	displayName: str
	__typename: str

class HomeShelfUsersResponseUserData(TypedDict):
	id: str
	login: str
	displayName: str
	channel: HomeShelfUsersResponseUserDataChannelData
	primaryTeam: Union[NoneType, HomeShelfUsersResponseUserDataPrimaryteamData]
	__typename: str

class HomeShelfUsersResponse(TypedDict):
	user: HomeShelfUsersResponseUserData

class HomeShelfVideosRequest(TypedDict):
	channelLogin: str
	first: int

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1CuratorData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1ClipgameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	boxArtURL: str
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: str
	roles: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterDataRolesData
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1GueststarparticipantsDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: str
	description: str
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1GueststarparticipantsData(TypedDict):
	host: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1GueststarparticipantsDataHostData
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1(TypedDict):
	id: str
	slug: str
	clipTitle: str
	clipViewCount: int
	curator: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1CuratorData
	clipGame: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1ClipgameData
	broadcaster: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1BroadcasterData
	thumbnailURL: str
	createdAt: str
	durationSeconds: int
	isFeatured: bool
	guestStarParticipants: Union[NoneType, HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1GueststarparticipantsData]
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2SelfData(TypedDict):
	isRestricted: bool
	viewingHistory: NoneType
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2GameData(TypedDict):
	id: str
	slug: str
	boxArtURL: str
	displayName: str
	name: str
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2OwnerData(TypedDict):
	id: str
	displayName: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2(TypedDict):
	id: str
	title: str
	previewThumbnailURL: str
	publishedAt: str
	viewCount: int
	lengthSeconds: int
	animatedPreviewURL: str
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	self: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2SelfData
	game: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2GameData
	owner: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2OwnerData
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	description: NoneType
	type: str
	items: List[Union[HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData1, HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeDataItemsData2]]
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesData(TypedDict):
	node: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesDataNodeData
	__typename: str

class HomeShelfVideosResponseUserDataVideoshelvesData(TypedDict):
	edges: Falsy[List[HomeShelfVideosResponseUserDataVideoshelvesDataEdgesData]]
	__typename: str

class HomeShelfVideosResponseUserData(TypedDict):
	id: str
	videoShelves: HomeShelfVideosResponseUserDataVideoshelvesData
	__typename: str

class HomeShelfVideosResponse(TypedDict):
	user: HomeShelfVideosResponseUserData

class incrementClipViewCountRequestInputData(TypedDict):
	slug: str

class incrementClipViewCountRequest(TypedDict):
	input: incrementClipViewCountRequestInputData

class incrementClipViewCountResponseUpdateclipviewcountDataClipData(TypedDict):
	id: str
	__typename: str

class incrementClipViewCountResponseUpdateclipviewcountData(TypedDict):
	clip: incrementClipViewCountResponseUpdateclipviewcountDataClipData
	__typename: str

class incrementClipViewCountResponse(TypedDict):
	updateClipViewCount: incrementClipViewCountResponseUpdateclipviewcountData

class LastUnbanRequestRequest(TypedDict):
	channelID: str
	includeCanRequestUnban: bool

class LastUnbanRequestResponseChannelDataSelfData(TypedDict):
	lastUnbanRequest: NoneType
	__typename: str

class LastUnbanRequestResponseChannelData(TypedDict):
	id: str
	self: LastUnbanRequestResponseChannelDataSelfData
	__typename: str

class LastUnbanRequestResponse(TypedDict):
	channel: LastUnbanRequestResponseChannelData

class LowerHomeHeaderRequest(TypedDict):
	channelLogin: str

class LowerHomeHeaderResponseUserDataSelfData(TypedDict):
	isEditor: bool
	__typename: str

class LowerHomeHeaderResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, LowerHomeHeaderResponseUserDataSelfData]
	__typename: str

class LowerHomeHeaderResponse(TypedDict):
	user: LowerHomeHeaderResponseUserData

class MessageBuffer_ChannelRequest(TypedDict):
	channelLogin: str

class MessageBuffer_ChannelResponseUserDataChatsettingsData(TypedDict):
	chatDelayMs: Falsy[int]
	__typename: str

class MessageBuffer_ChannelResponseUserData(TypedDict):
	id: str
	chatSettings: MessageBuffer_ChannelResponseUserDataChatsettingsData
	__typename: str

class MessageBuffer_ChannelResponse(TypedDict):
	user: MessageBuffer_ChannelResponseUserData

class MessageBufferChatHistoryRequest1(TypedDict):
	channelLogin: str

class MessageBufferChatHistoryRequest2(TypedDict):
	channelID: str
	channelLogin: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData1(TypedDict):
	emoteID: str
	setID: str
	token: str
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData2(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData3(TypedDict):
	bitsAmount: int
	prefix: str
	tier: int
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsData(TypedDict):
	text: str
	content: Union[NoneType, Union[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData1, MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData2, MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData3]]
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentData(TypedDict):
	text: str
	fragments: List[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsData]
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataContentData(TypedDict):
	text: str
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataSenderData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageData(TypedDict):
	id: str
	content: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataContentData
	deletedAt: NoneType
	sender: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataSenderData
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataThreadparentmessageDataSenderData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataThreadparentmessageData(TypedDict):
	id: str
	deletedAt: NoneType
	sender: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataThreadparentmessageDataSenderData
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataSenderData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataSenderbadgesData(TypedDict):
	setID: str
	version: str
	id: str
	__typename: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesData(TypedDict):
	id: str
	deletedAt: NoneType
	sentAt: str
	content: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentData
	parentMessage: Union[NoneType, MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageData]
	threadParentMessage: Union[NoneType, MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataThreadparentmessageData]
	sender: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataSenderData
	senderBadges: Falsy[List[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataSenderbadgesData]]
	senderChatColor: Union[str, NoneType]
	sourceChannel: NoneType
	sourceSenderBadges: NoneType
	__typename: str

class MessageBufferChatHistoryResponseChannelData(TypedDict):
	id: str
	recentChatMessages: Falsy[List[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesData]]
	__typename: str

class MessageBufferChatHistoryResponse(TypedDict):
	channel: MessageBufferChatHistoryResponseChannelData

class NielsenContentMetadataRequest(TypedDict):
	isCollectionContent: bool
	isLiveContent: bool
	isVODContent: bool
	collectionID: Falsy[str]
	login: Falsy[str]
	vodID: Falsy[str]

class NielsenContentMetadataResponse1UserDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class NielsenContentMetadataResponse1UserDataStreamDataGameData(TypedDict):
	id: str
	displayName: str
	__typename: str

class NielsenContentMetadataResponse1UserDataStreamData(TypedDict):
	id: str
	createdAt: str
	game: NielsenContentMetadataResponse1UserDataStreamDataGameData
	__typename: str

class NielsenContentMetadataResponse1UserData(TypedDict):
	id: str
	broadcastSettings: NielsenContentMetadataResponse1UserDataBroadcastsettingsData
	stream: Union[NoneType, NielsenContentMetadataResponse1UserDataStreamData]
	__typename: str

class NielsenContentMetadataResponse1(TypedDict):
	user: NielsenContentMetadataResponse1UserData

class NielsenContentMetadataResponse2VideoDataGameData(TypedDict):
	id: str
	displayName: str
	__typename: str

class NielsenContentMetadataResponse2VideoDataOwnerData(TypedDict):
	id: str
	login: str
	__typename: str

class NielsenContentMetadataResponse2VideoData(TypedDict):
	id: str
	createdAt: str
	title: str
	game: NielsenContentMetadataResponse2VideoDataGameData
	owner: NielsenContentMetadataResponse2VideoDataOwnerData
	__typename: str

class NielsenContentMetadataResponse2(TypedDict):
	video: NielsenContentMetadataResponse2VideoData

class OneClickEligibilityRequest(TypedDict):
	walletType: str

class OneClickEligibilityResponseRequestinfoData(TypedDict):
	countryCode: str
	__typename: str

class OneClickEligibilityResponseCurrentuserDataPaymentmethodsData(TypedDict):
	chargeInstrumentID: Falsy[str]
	provider: str
	paymentType: str
	billingCountry: NoneType
	billingEmail: NoneType
	billingUsername: NoneType
	cardType: NoneType
	lastFour: NoneType
	expirationMonth: NoneType
	expirationYear: NoneType
	paymentScheme: NoneType
	__typename: str

class OneClickEligibilityResponseCurrentuserDataWalletbalancesDataAllbalancesData(TypedDict):
	amount: Falsy[int]
	currency: str
	expiresAt: NoneType
	exponent: int
	__typename: str

class OneClickEligibilityResponseCurrentuserDataWalletbalancesData(TypedDict):
	allBalances: List[OneClickEligibilityResponseCurrentuserDataWalletbalancesDataAllbalancesData]
	__typename: str

class OneClickEligibilityResponseCurrentuserData(TypedDict):
	id: str
	paymentMethods: List[OneClickEligibilityResponseCurrentuserDataPaymentmethodsData]
	walletBalances: OneClickEligibilityResponseCurrentuserDataWalletbalancesData
	residence: NoneType
	__typename: str

class OneClickEligibilityResponseRecurlyconfigsDataPaywithamazonconfigsData(TypedDict):
	clientID: str
	isProduction: bool
	sellerID: str
	__typename: str

class OneClickEligibilityResponseRecurlyconfigsData(TypedDict):
	payWithAmazonConfigs: OneClickEligibilityResponseRecurlyconfigsDataPaywithamazonconfigsData
	braintreeClientAuthorization: str
	publicKey: str
	__typename: str

class OneClickEligibilityResponse(TypedDict):
	requestInfo: OneClickEligibilityResponseRequestinfoData
	currentUser: OneClickEligibilityResponseCurrentuserData
	recurlyConfigs: OneClickEligibilityResponseRecurlyconfigsData

class OneTapFeedRequest(TypedDict):
	channelID: str

class OneTapFeedResponseOnetapfeedData(TypedDict):
	items: Falsy[List[Any]]
	__typename: str

class OneTapFeedResponse(TypedDict):
	oneTapFeed: OneTapFeedResponseOnetapfeedData

class OnsiteNotifications_SummaryRequest(TypedDict):
	...

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataViewerunreadsummaryData(TypedDict):
	unreadCount: Falsy[int]
	lastReadAllAt: NoneType
	__typename: str

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataCreatorunreadsummaryData(TypedDict):
	unreadCount: Falsy[int]
	__typename: str

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryData(TypedDict):
	unseenCount: Falsy[int]
	lastSeenAt: NoneType
	viewerUnreadSummary: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataViewerunreadsummaryData
	creatorUnreadSummary: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataCreatorunreadsummaryData
	__typename: str

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsData(TypedDict):
	summary: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryData
	__typename: str

class OnsiteNotifications_SummaryResponseCurrentuserData(TypedDict):
	id: str
	notifications: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsData
	__typename: str

class OnsiteNotifications_SummaryResponse(TypedDict):
	currentUser: OnsiteNotifications_SummaryResponseCurrentuserData

class PaidPinnedChatRequest(TypedDict):
	channelID: str
	count: int
	messageType: str

class PaidPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class PaidPinnedChatResponseChannelDataPinnedchatmessagesData(TypedDict):
	edges: Falsy[List[Any]]
	pageInfo: PaidPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData
	__typename: str

class PaidPinnedChatResponseChannelData(TypedDict):
	id: str
	pinnedChatMessages: PaidPinnedChatResponseChannelDataPinnedchatmessagesData
	__typename: str

class PaidPinnedChatResponse(TypedDict):
	channel: PaidPinnedChatResponseChannelData

class PbyPGameRequest(TypedDict):
	channelLogin: str
	tagType: str

class PbyPGameResponseUserDataStreamDataGameDataTagsData(TypedDict):
	id: str
	tagName: str
	__typename: str

class PbyPGameResponseUserDataStreamDataGameData(TypedDict):
	id: str
	name: str
	tags: List[PbyPGameResponseUserDataStreamDataGameDataTagsData]
	__typename: str

class PbyPGameResponseUserDataStreamData(TypedDict):
	id: str
	game: PbyPGameResponseUserDataStreamDataGameData
	__typename: str

class PbyPGameResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, PbyPGameResponseUserDataStreamData]
	__typename: str

class PbyPGameResponse(TypedDict):
	user: PbyPGameResponseUserData

class PersistentGoalFollowButton_UserRequest(TypedDict):
	login: str

class PersistentGoalFollowButton_UserResponseUserDataSelfData(TypedDict):
	canFollow: bool
	follower: NoneType
	__typename: str

class PersistentGoalFollowButton_UserResponseUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: Union[NoneType, PersistentGoalFollowButton_UserResponseUserDataSelfData]
	__typename: str

class PersistentGoalFollowButton_UserResponse(TypedDict):
	user: PersistentGoalFollowButton_UserResponseUserData

class PinnedChatSettingsRequest(TypedDict):
	channelID: str

class PinnedChatSettingsResponseChannelDataPinnedchatsettingsData(TypedDict):
	isModAccessEnabled: bool
	__typename: str

class PinnedChatSettingsResponseChannelData(TypedDict):
	id: str
	pinnedChatSettings: Union[NoneType, PinnedChatSettingsResponseChannelDataPinnedchatsettingsData]
	__typename: str

class PinnedChatSettingsResponse(TypedDict):
	channel: PinnedChatSettingsResponseChannelData

class PinnedCheersSettingsRequest(TypedDict):
	login: str

class PinnedCheersSettingsResponseUserDataCheerDataSettingsData(TypedDict):
	id: str
	isPinnedCheersEnabled: bool
	__typename: str

class PinnedCheersSettingsResponseUserDataCheerData(TypedDict):
	id: str
	settings: PinnedCheersSettingsResponseUserDataCheerDataSettingsData
	__typename: str

class PinnedCheersSettingsResponseUserData(TypedDict):
	id: str
	cheer: PinnedCheersSettingsResponseUserDataCheerData
	__typename: str

class PinnedCheersSettingsResponse(TypedDict):
	user: PinnedCheersSettingsResponseUserData

class PlaybackAccessTokenRequest(TypedDict):
	isLive: bool
	login: Falsy[str]
	isVod: bool
	vodID: Falsy[str]
	playerType: str
	platform: str

class PlaybackAccessTokenResponse1StreamplaybackaccesstokenDataAuthorizationData(TypedDict):
	isForbidden: bool
	forbiddenReasonCode: str
	__typename: str

class PlaybackAccessTokenResponse1StreamplaybackaccesstokenData(TypedDict):
	value: str
	signature: str
	authorization: PlaybackAccessTokenResponse1StreamplaybackaccesstokenDataAuthorizationData
	__typename: str

class PlaybackAccessTokenResponse1(TypedDict):
	streamPlaybackAccessToken: PlaybackAccessTokenResponse1StreamplaybackaccesstokenData

class PlaybackAccessTokenResponse2VideoplaybackaccesstokenData(TypedDict):
	value: str
	signature: str
	__typename: str

class PlaybackAccessTokenResponse2(TypedDict):
	videoPlaybackAccessToken: PlaybackAccessTokenResponse2VideoplaybackaccesstokenData

class PrefetchPlaybackAccessTokenRequest(TypedDict):
	login: str
	playerType: str
	platform: str

class PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenDataAuthorizationData(TypedDict):
	isForbidden: bool
	forbiddenReasonCode: str
	__typename: str

class PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenData(TypedDict):
	value: str
	signature: str
	expiresAt: str
	authorization: PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenDataAuthorizationData
	__typename: str

class PrefetchPlaybackAccessTokenResponse(TypedDict):
	streamPlaybackAccessToken: PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenData

class queryUserViewedVideoRequest(TypedDict):
	...

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataNodeData(TypedDict):
	id: str
	__typename: str

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData(TypedDict):
	position: Falsy[int]
	__typename: str

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesData(TypedDict):
	node: queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataNodeData
	history: queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData
	__typename: str

class queryUserViewedVideoResponseCurrentuserDataViewedvideosData(TypedDict):
	edges: List[queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesData]
	__typename: str

class queryUserViewedVideoResponseCurrentuserData(TypedDict):
	id: str
	viewedVideos: queryUserViewedVideoResponseCurrentuserDataViewedvideosData
	__typename: str

class queryUserViewedVideoResponse(TypedDict):
	currentUser: queryUserViewedVideoResponseCurrentuserData

class RealtimeStreamTagListRequest(TypedDict):
	channelLogin: str

class RealtimeStreamTagListResponseUserDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class RealtimeStreamTagListResponseUserDataStreamData(TypedDict):
	id: str
	freeformTags: List[RealtimeStreamTagListResponseUserDataStreamDataFreeformtagsData]
	__typename: str

class RealtimeStreamTagListResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, RealtimeStreamTagListResponseUserDataStreamData]
	__typename: str

class RealtimeStreamTagListResponse(TypedDict):
	user: RealtimeStreamTagListResponseUserData

class RecapEligibilityQueryRequest(TypedDict):
	channelLogin: str

class RecapEligibilityQueryResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType
	banStatus: NoneType
	__typename: str

class RecapEligibilityQueryResponseUserDataRolesData(TypedDict):
	isAffiliate: bool
	isPartner: bool
	__typename: str

class RecapEligibilityQueryResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, RecapEligibilityQueryResponseUserDataSelfData]
	roles: RecapEligibilityQueryResponseUserDataRolesData
	__typename: str

class RecapEligibilityQueryResponse(TypedDict):
	user: RecapEligibilityQueryResponseUserData

class ReportMenuItemRequest(TypedDict):
	channelID: str

class ReportMenuItemResponseRequestinfoData(TypedDict):
	countryCode: str
	__typename: str

class ReportMenuItemResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str
	__typename: str

class ReportMenuItemResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, ReportMenuItemResponseUserDataStreamData]
	__typename: str

class ReportMenuItemResponse(TypedDict):
	requestInfo: ReportMenuItemResponseRequestinfoData
	user: ReportMenuItemResponseUserData

class RoleRestrictedRequest(TypedDict):
	contentOwnerLogin: str

class RoleRestrictedResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType
	__typename: str

class RoleRestrictedResponseCurrentuserData(TypedDict):
	id: str
	roles: RoleRestrictedResponseCurrentuserDataRolesData
	__typename: str

class RoleRestrictedResponseUserDataSelfData(TypedDict):
	isEditor: bool
	__typename: str

class RoleRestrictedResponseUserData(TypedDict):
	id: str
	self: RoleRestrictedResponseUserDataSelfData
	__typename: str

class RoleRestrictedResponse(TypedDict):
	currentUser: RoleRestrictedResponseCurrentuserData
	user: RoleRestrictedResponseUserData

class SearchResultsPage_SearchResultsRequestOptionsData(TypedDict):
	targets: NoneType
	shouldSkipDiscoveryControl: bool

class SearchResultsPage_SearchResultsRequest(TypedDict):
	platform: str
	query: str
	options: SearchResultsPage_SearchResultsRequestOptionsData
	requestID: str
	includeIsDJ: bool

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataFollowersData(TypedDict):
	totalCount: int
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelDataScheduleDataNextsegmentDataCategoriesData(TypedDict):
	id: str
	name: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelDataScheduleDataNextsegmentData(TypedDict):
	id: str
	startAt: str
	endAt: Union[str, NoneType]
	title: str
	hasReminder: bool
	categories: Falsy[List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelDataScheduleDataNextsegmentDataCategoriesData]]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelDataScheduleData(TypedDict):
	id: str
	nextSegment: Union[NoneType, SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelDataScheduleDataNextsegmentData]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelData(TypedDict):
	id: str
	schedule: Union[NoneType, SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelDataScheduleData]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoDataEdgesDataNodeData(TypedDict):
	id: str
	lengthSeconds: int
	title: str
	previewThumbnailURL: str
	templatePreviewThumbnailURL: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoDataEdgesDataNodeDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoDataEdgesData(TypedDict):
	node: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoDataEdgesDataNodeData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoData(TypedDict):
	edges: Falsy[List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoDataEdgesData]]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	durationSeconds: int
	thumbnailURL: str
	slug: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipDataEdgesDataNodeDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipDataEdgesData(TypedDict):
	node: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipDataEdgesDataNodeData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipData(TypedDict):
	edges: Falsy[List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipDataEdgesData]]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamData(TypedDict):
	game: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamDataGameData
	id: str
	previewImageURL: str
	templatePreviewImageURL: str
	freeformTags: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamDataFreeformtagsData]
	type: str
	viewersCount: int
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemData(TypedDict):
	broadcastSettings: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataBroadcastsettingsData
	displayName: str
	followers: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataFollowersData
	id: str
	lastBroadcast: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLastbroadcastData
	login: str
	profileImageURL: str
	description: str
	channel: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataChannelData
	self: NoneType
	latestVideo: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataLatestvideoData
	topClip: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataTopclipData
	roles: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataRolesData
	stream: Union[NoneType, SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemDataStreamData]
	watchParty: NoneType
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesData(TypedDict):
	trackingID: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesDataItemData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsData(TypedDict):
	cursor: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesData]
	score: int
	totalMatches: int
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataFollowersData(TypedDict):
	totalCount: int
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataChannelDataScheduleDataNextsegmentData(TypedDict):
	id: str
	startAt: str
	endAt: str
	title: Falsy[str]
	hasReminder: bool
	categories: Falsy[List[Any]]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataChannelDataScheduleData(TypedDict):
	id: str
	nextSegment: Union[NoneType, SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataChannelDataScheduleDataNextsegmentData]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataChannelData(TypedDict):
	id: str
	schedule: Union[NoneType, SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataChannelDataScheduleData]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoDataEdgesDataNodeData(TypedDict):
	id: str
	lengthSeconds: int
	title: str
	previewThumbnailURL: str
	templatePreviewThumbnailURL: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoDataEdgesDataNodeDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoDataEdgesData(TypedDict):
	node: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoDataEdgesDataNodeData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoData(TypedDict):
	edges: Falsy[List[SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoDataEdgesData]]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	durationSeconds: int
	thumbnailURL: str
	slug: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipDataEdgesDataNodeDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipDataEdgesData(TypedDict):
	node: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipDataEdgesDataNodeData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipData(TypedDict):
	edges: Falsy[List[SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipDataEdgesData]]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamData(TypedDict):
	game: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamDataGameData
	id: str
	previewImageURL: str
	templatePreviewImageURL: str
	freeformTags: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamDataFreeformtagsData]
	type: str
	viewersCount: int
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemData(TypedDict):
	broadcastSettings: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataBroadcastsettingsData
	displayName: str
	followers: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataFollowersData
	id: str
	lastBroadcast: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLastbroadcastData
	login: str
	profileImageURL: str
	description: str
	channel: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataChannelData
	self: NoneType
	latestVideo: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataLatestvideoData
	topClip: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataTopclipData
	roles: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataRolesData
	stream: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemDataStreamData
	watchParty: NoneType
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesData(TypedDict):
	trackingID: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesDataItemData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagData(TypedDict):
	cursor: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesData]
	score: int
	totalMatches: int
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataGamesData(TypedDict):
	cursor: Falsy[str]
	edges: Falsy[List[Any]]
	score: int
	totalMatches: Falsy[int]
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataOwnerDataRolesData(TypedDict):
	isPartner: bool
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataOwnerData(TypedDict):
	id: str
	displayName: str
	login: str
	roles: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataOwnerDataRolesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemData(TypedDict):
	createdAt: str
	owner: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataOwnerData
	id: str
	game: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataGameData
	lengthSeconds: int
	previewThumbnailURL: str
	templatePreviewThumbnailURL: str
	title: str
	viewCount: int
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesData(TypedDict):
	trackingID: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesDataItemData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosData(TypedDict):
	cursor: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesData]
	score: int
	totalMatches: int
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataGameData(TypedDict):
	name: str
	id: str
	slug: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataBroadcasterDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataBroadcasterData(TypedDict):
	id: str
	primaryColorHex: str
	login: str
	displayName: str
	broadcastSettings: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataBroadcasterDataBroadcastsettingsData
	roles: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataBroadcasterDataRolesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamData(TypedDict):
	id: str
	viewersCount: int
	previewImageURL: str
	templatePreviewImageURL: str
	game: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataGameData
	broadcaster: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataBroadcasterData
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamDataPreviewthumbnailpropertiesData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemData(TypedDict):
	id: str
	stream: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemDataStreamData
	watchParty: NoneType
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesData(TypedDict):
	trackingID: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesDataItemData
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsData(TypedDict):
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesData]
	score: int
	__typename: str

class SearchResultsPage_SearchResultsResponseSearchforData(TypedDict):
	banners: NoneType
	channels: SearchResultsPage_SearchResultsResponseSearchforDataChannelsData
	channelsWithTag: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagData
	games: SearchResultsPage_SearchResultsResponseSearchforDataGamesData
	videos: SearchResultsPage_SearchResultsResponseSearchforDataVideosData
	relatedLiveChannels: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsData
	__typename: str

class SearchResultsPage_SearchResultsResponse(TypedDict):
	searchFor: SearchResultsPage_SearchResultsResponseSearchforData

class ShareClipRenderStatusRequest(TypedDict):
	slug: str

class ShareClipRenderStatusResponseClipDataAssetsDataCuratorData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataVideoqualitiesData(TypedDict):
	frameRate: Union[float, int]
	quality: str
	sourceURL: str
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataTopleftData(TypedDict):
	xPercentage: float
	yPercentage: float
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: float
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataBottomrightData
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataTopleftData(TypedDict):
	xPercentage: float
	yPercentage: Falsy[int]
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: float
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataBottomrightData
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataData(TypedDict):
	topFrame: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeData
	bottomFrame: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeData
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataData(TypedDict):
	portraitClipLayout: str
	fullTemplateMetadata: NoneType
	stackedTemplateMetadata: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataData
	__typename: str

class ShareClipRenderStatusResponseClipDataAssetsData(TypedDict):
	id: str
	aspectRatio: float
	type: str
	createdAt: str
	creationState: str
	curator: ShareClipRenderStatusResponseClipDataAssetsDataCuratorData
	thumbnailURL: str
	videoQualities: List[ShareClipRenderStatusResponseClipDataAssetsDataVideoqualitiesData]
	portraitMetadata: Union[NoneType, ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataData]
	__typename: str

class ShareClipRenderStatusResponseClipDataCuratorData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	__typename: str

class ShareClipRenderStatusResponseClipDataGameData(TypedDict):
	id: str
	name: str
	boxArtURL: str
	displayName: str
	slug: str
	__typename: str

class ShareClipRenderStatusResponseClipDataBroadcastData(TypedDict):
	id: str
	title: NoneType
	__typename: str

class ShareClipRenderStatusResponseClipDataBroadcasterDataFollowersData(TypedDict):
	totalCount: int
	__typename: str

class ShareClipRenderStatusResponseClipDataBroadcasterDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str
	__typename: str

class ShareClipRenderStatusResponseClipDataBroadcasterDataSelfData(TypedDict):
	isEditor: bool
	__typename: str

class ShareClipRenderStatusResponseClipDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: str
	isPartner: bool
	profileImageURL: str
	followers: ShareClipRenderStatusResponseClipDataBroadcasterDataFollowersData
	stream: NoneType
	lastBroadcast: ShareClipRenderStatusResponseClipDataBroadcasterDataLastbroadcastData
	self: Union[NoneType, ShareClipRenderStatusResponseClipDataBroadcasterDataSelfData]
	__typename: str

class ShareClipRenderStatusResponseClipDataPlaybackaccesstokenData(TypedDict):
	signature: str
	value: str
	__typename: str

class ShareClipRenderStatusResponseClipDataVideoData(TypedDict):
	id: str
	broadcastType: str
	title: str
	__typename: str

class ShareClipRenderStatusResponseClipDataVideoqualitiesData(TypedDict):
	sourceURL: str
	__typename: str

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData(TypedDict):
	xPercentage: float
	yPercentage: Falsy[int]
	__typename: str

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: int
	__typename: str

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData
	__typename: str

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataData(TypedDict):
	mainFrame: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData
	__typename: str

class ShareClipRenderStatusResponseClipDataSuggestedcroppingData(TypedDict):
	portraitClipLayout: str
	fullTemplateMetadata: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataData
	stackedTemplateMetadata: NoneType
	__typename: str

class ShareClipRenderStatusResponseClipData(TypedDict):
	id: str
	slug: str
	url: str
	embedURL: str
	title: str
	viewCount: int
	language: str
	isFeatured: bool
	assets: List[ShareClipRenderStatusResponseClipDataAssetsData]
	curator: ShareClipRenderStatusResponseClipDataCuratorData
	game: ShareClipRenderStatusResponseClipDataGameData
	broadcast: ShareClipRenderStatusResponseClipDataBroadcastData
	broadcaster: ShareClipRenderStatusResponseClipDataBroadcasterData
	thumbnailURL: str
	createdAt: str
	isPublished: bool
	durationSeconds: int
	champBadge: NoneType
	playbackAccessToken: ShareClipRenderStatusResponseClipDataPlaybackaccesstokenData
	video: Union[NoneType, ShareClipRenderStatusResponseClipDataVideoData]
	videoOffsetSeconds: Union[int, NoneType]
	videoQualities: List[ShareClipRenderStatusResponseClipDataVideoqualitiesData]
	isViewerEditRestricted: bool
	suggestedCropping: Union[NoneType, ShareClipRenderStatusResponseClipDataSuggestedcroppingData]
	__typename: str

class ShareClipRenderStatusResponse(TypedDict):
	clip: ShareClipRenderStatusResponseClipData

class SharedChatModeratorStrikesRequest(TypedDict):
	channelIDs: Falsy[List[Any]]

class SharedChatModeratorStrikesResponse(TypedDict):
	users: Falsy[List[Any]]

class SharedChatSessionRequest(TypedDict):
	channelID: str

class SharedChatSessionResponse(TypedDict):
	sharedChatSession: NoneType

class ShelvesRequest1ContextData(TypedDict):
	clientApp: str
	location: str
	referrerDomain: Falsy[str]
	viewportHeight: int
	viewportWidth: int

class ShelvesRequest1(TypedDict):
	imageWidth: int
	itemsPerRow: int
	platform: str
	limit: int
	requestID: Falsy[str]
	includeIsDJ: bool
	context: ShelvesRequest1ContextData
	verbose: bool

class ShelvesRequest2ContextData(TypedDict):
	clientApp: str
	location: str
	referrerDomain: str
	viewportHeight: int
	viewportWidth: int

class ShelvesRequest2(TypedDict):
	imageWidth: int
	after: str
	itemsPerRow: int
	limit: int
	platform: str
	requestID: Falsy[str]
	includeIsDJ: bool
	context: ShelvesRequest2ContextData
	verbose: bool

class ShelvesRequest3ContextData(TypedDict):
	clientApp: str
	location: str
	referrerDomain: Falsy[str]
	viewportHeight: int
	viewportWidth: int

class ShelvesRequest3(TypedDict):
	imageWidth: int
	itemsPerRow: int
	langWeightedCCU: bool
	platform: str
	limit: int
	requestID: Falsy[str]
	includeIsDJ: bool
	context: ShelvesRequest3ContextData
	verbose: bool

class ShelvesRequest4ContextData(TypedDict):
	clientApp: str
	location: str
	referrerDomain: Falsy[str]
	viewportHeight: int
	viewportWidth: int

class ShelvesRequest4(TypedDict):
	imageWidth: int
	after: str
	itemsPerRow: int
	limit: int
	langWeightedCCU: bool
	platform: str
	requestID: Falsy[str]
	includeIsDJ: bool
	context: ShelvesRequest4ContextData
	verbose: bool

class ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData1(TypedDict):
	text: str
	hasEmphasis: bool
	location: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData2CollectionnameData(TypedDict):
	fallbackLocalizedTitle: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData2(TypedDict):
	id: str
	slug: str
	collectionName: ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData2CollectionnameData
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData3(TypedDict):
	id: str
	categorySlug: str
	name: str
	displayName: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensData(TypedDict):
	node: Union[ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData1, ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData2, ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensDataNodeData3]
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataTitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[ShelvesResponseShelvesDataEdgesDataNodeDataTitleDataLocalizedtitletokensData]
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1BroadcasterDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1BroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1BroadcasterData(TypedDict):
	id: str
	broadcastSettings: ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1BroadcasterDataBroadcastsettingsData
	displayName: str
	login: str
	profileImageURL: str
	largeProfileImageURL: str
	primaryColorHex: Union[NoneType, str]
	roles: ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1BroadcasterDataRolesData
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1GameDataGametagsData(TypedDict):
	id: str
	isLanguageTag: bool
	localizedName: str
	tagName: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1GameData(TypedDict):
	id: str
	categorySlug: str
	name: str
	viewersCount: int
	displayName: str
	boxArtURL: str
	gameTags: List[ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1GameDataGametagsData]
	originalReleaseDate: Union[NoneType, str]
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1FreeformtagsData(TypedDict):
	id: str
	name: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1(TypedDict):
	id: str
	broadcaster: ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1BroadcasterData
	game: ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1GameData
	freeformTags: Falsy[List[ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1FreeformtagsData]]
	viewersCount: int
	previewImageURL: str
	createdAt: str
	type: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData2GametagsData(TypedDict):
	id: str
	isLanguageTag: bool
	localizedName: str
	tagName: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData2(TypedDict):
	id: str
	categorySlug: str
	name: str
	viewersCount: int
	displayName: str
	boxArtURL: str
	gameTags: List[ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData2GametagsData]
	originalReleaseDate: Union[str, NoneType]
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: Union[ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData1, ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesDataNodeData2]
	trackingID: str
	promotionsCampaignID: Falsy[str]
	sourceType: str
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataContentData(TypedDict):
	edges: List[ShelvesResponseShelvesDataEdgesDataNodeDataContentDataEdgesData]
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeDataTrackinginfoData(TypedDict):
	rowName: str
	reasonType: Falsy[str]
	reasonTarget: NoneType
	reasonTargetType: NoneType
	__typename: str

class ShelvesResponseShelvesDataEdgesDataNodeData(TypedDict):
	id: str
	title: ShelvesResponseShelvesDataEdgesDataNodeDataTitleData
	content: ShelvesResponseShelvesDataEdgesDataNodeDataContentData
	trackingInfo: ShelvesResponseShelvesDataEdgesDataNodeDataTrackinginfoData
	__typename: str

class ShelvesResponseShelvesDataEdgesData(TypedDict):
	node: ShelvesResponseShelvesDataEdgesDataNodeData
	cursor: str
	__typename: str

class ShelvesResponseShelvesDataPageinfoData(TypedDict):
	hasNextPage: bool
	__typename: str

class ShelvesResponseShelvesData(TypedDict):
	edges: List[ShelvesResponseShelvesDataEdgesData]
	pageInfo: ShelvesResponseShelvesDataPageinfoData
	verboseResults: NoneType
	__typename: str

class ShelvesResponse(TypedDict):
	shelves: ShelvesResponseShelvesData

class ShoutoutHighlightServiceQueryRequest(TypedDict):
	targetLogin: Falsy[str]
	isLoggedOut: bool

class ShoutoutHighlightServiceQueryResponse1(TypedDict):
	user: NoneType

class ShoutoutHighlightServiceQueryResponse2(TypedDict):
	...

class StoryChannelQueryRequest(TypedDict):
	channelLogin: str

class StoryChannelQueryResponseUserData(TypedDict):
	id: str
	__typename: str

class StoryChannelQueryResponse(TypedDict):
	user: StoryChannelQueryResponseUserData

class StreamChatRequest(TypedDict):
	login: str

class StreamChatResponseChannelDataRolesData(TypedDict):
	isPartner: bool
	isAffiliate: bool
	__typename: str

class StreamChatResponseChannelDataSelfData(TypedDict):
	banStatus: NoneType
	isChannelMember: bool
	isModerator: bool
	subscriptionBenefit: NoneType
	__typename: str

class StreamChatResponseChannelDataStreamData(TypedDict):
	id: str
	__typename: str

class StreamChatResponseChannelData(TypedDict):
	id: str
	displayName: str
	roles: StreamChatResponseChannelDataRolesData
	self: Union[NoneType, StreamChatResponseChannelDataSelfData]
	stream: Union[NoneType, StreamChatResponseChannelDataStreamData]
	__typename: str

class StreamChatResponse(TypedDict):
	channel: StreamChatResponseChannelData

class StreamMetadataRequest(TypedDict):
	channelLogin: str
	includeIsDJ: bool

class StreamMetadataResponseUserDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool
	__typename: str

class StreamMetadataResponseUserDataPrimaryteamData(TypedDict):
	id: str
	name: str
	displayName: str
	__typename: str

class StreamMetadataResponseUserDataChannelData(TypedDict):
	id: str
	__typename: str

class StreamMetadataResponseUserDataLastbroadcastData(TypedDict):
	id: str
	title: str
	__typename: str

class StreamMetadataResponseUserDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	__typename: str

class StreamMetadataResponseUserDataStreamData(TypedDict):
	id: str
	type: str
	createdAt: str
	game: StreamMetadataResponseUserDataStreamDataGameData
	__typename: str

class StreamMetadataResponseUserData(TypedDict):
	id: str
	primaryColorHex: Union[str, NoneType]
	roles: StreamMetadataResponseUserDataRolesData
	profileImageURL: str
	primaryTeam: Union[NoneType, StreamMetadataResponseUserDataPrimaryteamData]
	channel: StreamMetadataResponseUserDataChannelData
	lastBroadcast: StreamMetadataResponseUserDataLastbroadcastData
	stream: Union[NoneType, StreamMetadataResponseUserDataStreamData]
	__typename: str

class StreamMetadataResponse(TypedDict):
	user: StreamMetadataResponseUserData

class StreamRefetchManagerRequest(TypedDict):
	channel: str

class StreamRefetchManagerResponseUserDataStreamData(TypedDict):
	id: str
	isEncrypted: bool
	__typename: str

class StreamRefetchManagerResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, StreamRefetchManagerResponseUserDataStreamData]
	__typename: str

class StreamRefetchManagerResponse(TypedDict):
	user: StreamRefetchManagerResponseUserData

class StreamScheduleRequest(TypedDict):
	login: str
	startingWeekday: str
	utcOffsetMinutes: int
	startAt: str
	endAt: str

class StreamScheduleResponseCurrentuserData(TypedDict):
	id: str
	login: str
	__typename: str

class StreamScheduleResponseUserDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str
	__typename: str

class StreamScheduleResponseUserDataBroadcastsettingsData(TypedDict):
	id: str
	title: str
	__typename: str

class StreamScheduleResponseUserDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	__typename: str

class StreamScheduleResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str
	viewersCount: int
	previewImageURL: str
	game: StreamScheduleResponseUserDataStreamDataGameData
	__typename: str

class StreamScheduleResponseUserDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	__typename: str

class StreamScheduleResponseUserDataVideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	createdAt: str
	lengthSeconds: int
	viewCount: int
	previewThumbnailURL: str
	game: StreamScheduleResponseUserDataVideosDataEdgesDataNodeDataGameData
	__typename: str

class StreamScheduleResponseUserDataVideosDataEdgesData(TypedDict):
	node: StreamScheduleResponseUserDataVideosDataEdgesDataNodeData
	__typename: str

class StreamScheduleResponseUserDataVideosData(TypedDict):
	edges: Falsy[List[StreamScheduleResponseUserDataVideosDataEdgesData]]
	__typename: str

class StreamScheduleResponseUserDataChannelDataScheduleDataNextsegmentData(TypedDict):
	id: str
	startAt: str
	__typename: str

class StreamScheduleResponseUserDataChannelDataScheduleDataSegmentsData(TypedDict):
	id: str
	baseSegmentID: str
	title: str
	startAt: str
	endAt: NoneType
	isCancelled: bool
	cancelledUntil: NoneType
	hasReminder: bool
	repeatEndsAfterCount: Falsy[int]
	categories: Falsy[List[Any]]
	__typename: str

class StreamScheduleResponseUserDataChannelDataScheduleData(TypedDict):
	id: str
	nextSegment: Union[NoneType, StreamScheduleResponseUserDataChannelDataScheduleDataNextsegmentData]
	interruption: NoneType
	segments: Union[NoneType, List[StreamScheduleResponseUserDataChannelDataScheduleDataSegmentsData]]
	__typename: str

class StreamScheduleResponseUserDataChannelData(TypedDict):
	id: str
	schedule: Union[NoneType, StreamScheduleResponseUserDataChannelDataScheduleData]
	__typename: str

class StreamScheduleResponseUserData(TypedDict):
	id: str
	primaryColorHex: str
	lastBroadcast: StreamScheduleResponseUserDataLastbroadcastData
	broadcastSettings: StreamScheduleResponseUserDataBroadcastsettingsData
	stream: Union[NoneType, StreamScheduleResponseUserDataStreamData]
	videos: StreamScheduleResponseUserDataVideosData
	channel: StreamScheduleResponseUserDataChannelData
	__typename: str

class StreamScheduleResponse(TypedDict):
	currentUser: Union[NoneType, StreamScheduleResponseCurrentuserData]
	user: StreamScheduleResponseUserData

class SubscribedContextRequest(TypedDict):
	login: str

class SubscribedContextResponseUserData(TypedDict):
	id: str
	self: NoneType
	__typename: str

class SubscribedContextResponse(TypedDict):
	user: SubscribedContextResponseUserData

class SyncedSettingsChatPauseSettingRequest(TypedDict):
	...

class SyncedSettingsChatPauseSettingResponseCurrentuserDataChatuisettingsData(TypedDict):
	chatPauseSetting: NoneType
	__typename: str

class SyncedSettingsChatPauseSettingResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsChatPauseSettingResponseCurrentuserDataChatuisettingsData
	__typename: str

class SyncedSettingsChatPauseSettingResponse(TypedDict):
	currentUser: SyncedSettingsChatPauseSettingResponseCurrentuserData

class SyncedSettingsDeletedMessageDisplaySettingRequest(TypedDict):
	...

class SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserDataChatuisettingsData(TypedDict):
	deletedMessageDisplaySetting: NoneType
	__typename: str

class SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserDataChatuisettingsData
	__typename: str

class SyncedSettingsDeletedMessageDisplaySettingResponse(TypedDict):
	currentUser: SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserData

class SyncedSettingsEmoteAnimationsRequest(TypedDict):
	...

class SyncedSettingsEmoteAnimationsResponseCurrentuserDataChatuisettingsData(TypedDict):
	isEmoteAnimationsEnabled: bool
	__typename: str

class SyncedSettingsEmoteAnimationsResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsEmoteAnimationsResponseCurrentuserDataChatuisettingsData
	__typename: str

class SyncedSettingsEmoteAnimationsResponse(TypedDict):
	currentUser: SyncedSettingsEmoteAnimationsResponseCurrentuserData

class SyncedSettingsReadableChatColorsRequest(TypedDict):
	...

class SyncedSettingsReadableChatColorsResponseCurrentuserDataChatuisettingsData(TypedDict):
	isReadableChatColorsEnabled: bool
	__typename: str

class SyncedSettingsReadableChatColorsResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsReadableChatColorsResponseCurrentuserDataChatuisettingsData
	__typename: str

class SyncedSettingsReadableChatColorsResponse(TypedDict):
	currentUser: SyncedSettingsReadableChatColorsResponseCurrentuserData

class TitleMentionsRequest(TypedDict):
	logins: Falsy[List[str]]

class TitleMentionsResponseUsersData(TypedDict):
	id: str
	login: str
	displayName: str
	description: str
	primaryColorHex: str
	profileImageURL: str
	__typename: str

class TitleMentionsResponseCurrentuserDataRolesData(TypedDict):
	isSiteAdmin: NoneType
	isStaff: NoneType
	isGlobalMod: NoneType
	__typename: str

class TitleMentionsResponseCurrentuserData(TypedDict):
	id: str
	login: str
	roles: TitleMentionsResponseCurrentuserDataRolesData
	blockedUsers: Falsy[List[Any]]
	__typename: str

class TitleMentionsResponse(TypedDict):
	users: Falsy[List[TitleMentionsResponseUsersData]]
	currentUser: Union[NoneType, TitleMentionsResponseCurrentuserData]

class UpdateConsentMutationRequestInputDataVendorstatusData(TypedDict):
	name: str
	consentStatus: str

class UpdateConsentMutationRequestInputDataGdpruserpreferencesDataPurposestatusData(TypedDict):
	id: str
	consentStatus: str

class UpdateConsentMutationRequestInputDataGdpruserpreferencesDataSpecialfeatureoptinstatusData(TypedDict):
	id: str
	consentStatus: str

class UpdateConsentMutationRequestInputDataGdpruserpreferencesData(TypedDict):
	purposeStatus: List[UpdateConsentMutationRequestInputDataGdpruserpreferencesDataPurposestatusData]
	specialFeatureOptInStatus: List[UpdateConsentMutationRequestInputDataGdpruserpreferencesDataSpecialfeatureoptinstatusData]
	hasUserSetPurposeConsent: bool
	consentScreen: str
	language: str

class UpdateConsentMutationRequestInputData(TypedDict):
	consentSessionID: str
	privacyLawName: str
	vendorStatus: List[UpdateConsentMutationRequestInputDataVendorstatusData]
	gdprUserPreferences: UpdateConsentMutationRequestInputDataGdpruserpreferencesData

class UpdateConsentMutationRequest(TypedDict):
	input: UpdateConsentMutationRequestInputData
	includeNewCookieConsentFields: bool
	includeTCData: bool

class UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorstatusData(TypedDict):
	name: str
	consentStatus: str
	hasUserSetConsent: bool
	isVisible: bool
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorconsentstatusDataStatusData1(TypedDict):
	name: str
	consentStatus: str
	hasUserSetConsent: bool
	isVisible: bool
	cookieVendorType: str
	features: Union[NoneType, List[str]]
	purposes: Union[NoneType, List[str]]
	flexiblePurposes: Union[NoneType, List[str]]
	specialFeatures: Union[NoneType, List[str]]
	specialPurposes: Union[NoneType, List[str]]
	policyURL: str
	cookieMaxAgeSeconds: Falsy[int]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorconsentstatusDataStatusData2(TypedDict):
	name: str
	consentStatus: str
	hasUserSetConsent: bool
	isVisible: bool
	cookieVendorType: str
	policyURL: str
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorconsentstatusData(TypedDict):
	status: List[Union[UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorconsentstatusDataStatusData1, UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorconsentstatusDataStatusData2]]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataTcdataDataPurposeData(TypedDict):
	consents: str
	legitimateInterests: Falsy[str]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataTcdataDataVendorData(TypedDict):
	consents: str
	legitimateInterests: Falsy[str]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataTcdataData(TypedDict):
	tcString: str
	tcfPolicyVersion: int
	cmpID: str
	cmpVersion: Falsy[int]
	ifGDPRApplies: bool
	isServiceSpecific: bool
	hasNonStandardStacks: bool
	publisherCountryCode: str
	hasPurposeOneTreatment: bool
	purpose: UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataTcdataDataPurposeData
	vendor: UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataTcdataDataVendorData
	specialFeatureOptins: str
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataPurposeDataIabinformationData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: List[str]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataPurposeData(TypedDict):
	iabInformation: UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataPurposeDataIabinformationData
	consentStatus: str
	hasUserSetConsent: bool
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataSpecialpurposeData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: List[str]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataFeaturesData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: Falsy[List[Any]]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataSpecialfeatureoptinsDataIabinformationData(TypedDict):
	id: str
	name: str
	description: str
	illustrations: Falsy[List[Any]]
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataSpecialfeatureoptinsData(TypedDict):
	iabInformation: UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataSpecialfeatureoptinsDataIabinformationData
	consentStatus: str
	hasUserSetConsent: bool
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesData(TypedDict):
	tcData: UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataTcdataData
	purpose: List[UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataPurposeData]
	specialPurpose: List[UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataSpecialpurposeData]
	features: List[UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataFeaturesData]
	specialFeatureOptIns: List[UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesDataSpecialfeatureoptinsData]
	hasUserSetPurposeConsent: bool
	__typename: str

class UpdateConsentMutationResponseUpdateconsentDataConsentData(TypedDict):
	id: str
	isDeniedUnderage: bool
	privacyLawName: str
	shouldShowNotification: bool
	shouldShowSettingsPage: bool
	shouldShowDismissButton: bool
	shouldSkipDmaBanner: bool
	vendorStatus: List[UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorstatusData]
	vendorConsentStatus: UpdateConsentMutationResponseUpdateconsentDataConsentDataVendorconsentstatusData
	gdprUserPreferences: UpdateConsentMutationResponseUpdateconsentDataConsentDataGdpruserpreferencesData
	dmaUserPreferences: NoneType
	__typename: str

class UpdateConsentMutationResponseUpdateconsentData(TypedDict):
	consent: UpdateConsentMutationResponseUpdateconsentDataConsentData
	__typename: str

class UpdateConsentMutationResponse(TypedDict):
	updateConsent: UpdateConsentMutationResponseUpdateconsentData

class updateUserViewedVideoRequestInputData(TypedDict):
	userID: str
	position: Falsy[int]
	videoID: str
	videoType: str

class updateUserViewedVideoRequest(TypedDict):
	input: updateUserViewedVideoRequestInputData

class updateUserViewedVideoResponseUpdateuserviewedvideoDataVideoData(TypedDict):
	id: str
	__typename: str

class updateUserViewedVideoResponseUpdateuserviewedvideoData(TypedDict):
	video: Union[NoneType, updateUserViewedVideoResponseUpdateuserviewedvideoDataVideoData]
	__typename: str

class updateUserViewedVideoResponse(TypedDict):
	updateUserViewedVideo: Union[NoneType, updateUserViewedVideoResponseUpdateuserviewedvideoData]

class UseLiveRequest(TypedDict):
	channelLogin: str

class UseLiveResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str
	__typename: str

class UseLiveResponseUserData(TypedDict):
	id: str
	login: str
	stream: Union[NoneType, UseLiveResponseUserDataStreamData]
	__typename: str

class UseLiveResponse(TypedDict):
	user: UseLiveResponseUserData

class UseLiveBroadcastRequest(TypedDict):
	channelLogin: str

class UseLiveBroadcastResponseUserDataLastbroadcastDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	__typename: str

class UseLiveBroadcastResponseUserDataLastbroadcastData(TypedDict):
	id: str
	title: str
	game: UseLiveBroadcastResponseUserDataLastbroadcastDataGameData
	__typename: str

class UseLiveBroadcastResponseUserData(TypedDict):
	id: str
	lastBroadcast: UseLiveBroadcastResponseUserDataLastbroadcastData
	__typename: str

class UseLiveBroadcastResponse(TypedDict):
	user: UseLiveBroadcastResponseUserData

class UserMenuCurrentUserRequest(TypedDict):
	...

class UserMenuCurrentUserResponseCurrentuserDataSettingsData(TypedDict):
	isSharingActivity: bool
	visibility: str
	__typename: str

class UserMenuCurrentUserResponseCurrentuserData(TypedDict):
	id: str
	availability: NoneType
	profileImageURL: str
	settings: UserMenuCurrentUserResponseCurrentuserDataSettingsData
	__typename: str

class UserMenuCurrentUserResponse(TypedDict):
	currentUser: UserMenuCurrentUserResponseCurrentuserData

class UserModStatusRequest(TypedDict):
	channelID: str
	userID: str

class UserModStatusResponseUserData(TypedDict):
	id: str
	login: str
	isModerator: bool
	__typename: str

class UserModStatusResponse(TypedDict):
	user: UserModStatusResponseUserData

class UseViewCountRequest(TypedDict):
	channelLogin: Falsy[str]

class UseViewCountResponseUserDataStreamData(TypedDict):
	id: str
	viewersCount: int
	collaborationViewersCount: NoneType
	__typename: str

class UseViewCountResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, UseViewCountResponseUserDataStreamData]
	__typename: str

class UseViewCountResponse(TypedDict):
	user: Union[NoneType, UseViewCountResponseUserData]

class VerifyEmail_CurrentUserRequest(TypedDict):
	...

class VerifyEmail_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	hasPrime: bool
	displayName: str
	email: str
	isEmailVerified: bool
	__typename: str

class VerifyEmail_CurrentUserResponseRequestinfoData(TypedDict):
	countryCode: str
	__typename: str

class VerifyEmail_CurrentUserResponse(TypedDict):
	currentUser: VerifyEmail_CurrentUserResponseCurrentuserData
	requestInfo: VerifyEmail_CurrentUserResponseRequestinfoData

class VideoAccessToken_ClipRequest(TypedDict):
	platform: str
	slug: str

class VideoAccessToken_ClipResponseClipDataPlaybackaccesstokenData(TypedDict):
	signature: str
	value: str
	__typename: str

class VideoAccessToken_ClipResponseClipDataVideoqualitiesData(TypedDict):
	frameRate: Union[float, int]
	quality: str
	sourceURL: str
	__typename: str

class VideoAccessToken_ClipResponseClipData(TypedDict):
	id: str
	playbackAccessToken: VideoAccessToken_ClipResponseClipDataPlaybackaccesstokenData
	videoQualities: List[VideoAccessToken_ClipResponseClipDataVideoqualitiesData]
	__typename: str

class VideoAccessToken_ClipResponse(TypedDict):
	clip: VideoAccessToken_ClipResponseClipData

class VideoCommentsRequest(TypedDict):
	videoID: str
	hasVideoID: bool

class VideoCommentsResponseBadgesData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: Union[NoneType, str]
	clickURL: Union[NoneType, str]
	__typename: str

class VideoCommentsResponseCheerconfigDataDisplayconfigDataColorsData(TypedDict):
	bits: int
	color: str
	__typename: str

class VideoCommentsResponseCheerconfigDataDisplayconfigDataTypesData(TypedDict):
	animation: str
	extension: str
	__typename: str

class VideoCommentsResponseCheerconfigDataDisplayconfigData(TypedDict):
	backgrounds: List[str]
	colors: List[VideoCommentsResponseCheerconfigDataDisplayconfigDataColorsData]
	order: List[str]
	scales: List[str]
	types: List[VideoCommentsResponseCheerconfigDataDisplayconfigDataTypesData]
	__typename: str

class VideoCommentsResponseCheerconfigDataGroupsDataNodesDataTiersData(TypedDict):
	id: str
	bits: int
	canShowInBitsCard: bool
	__typename: str

class VideoCommentsResponseCheerconfigDataGroupsDataNodesData(TypedDict):
	id: str
	prefix: str
	type: str
	campaign: NoneType
	tiers: List[VideoCommentsResponseCheerconfigDataGroupsDataNodesDataTiersData]
	__typename: str

class VideoCommentsResponseCheerconfigDataGroupsData(TypedDict):
	templateURL: str
	nodes: List[VideoCommentsResponseCheerconfigDataGroupsDataNodesData]
	__typename: str

class VideoCommentsResponseCheerconfigData(TypedDict):
	displayConfig: VideoCommentsResponseCheerconfigDataDisplayconfigData
	groups: List[VideoCommentsResponseCheerconfigDataGroupsData]
	__typename: str

class VideoCommentsResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType
	isSiteAdmin: NoneType
	isGlobalMod: NoneType
	__typename: str

class VideoCommentsResponseCurrentuserData(TypedDict):
	id: str
	roles: VideoCommentsResponseCurrentuserDataRolesData
	blockedUsers: Falsy[List[Any]]
	__typename: str

class VideoCommentsResponseVideoDataOwnerDataBroadcastbadgesData(TypedDict):
	id: str
	setID: str
	version: str
	title: str
	image1x: str
	image2x: str
	image4x: str
	clickAction: str
	clickURL: Union[NoneType, str]
	__typename: str

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesDataTiersData(TypedDict):
	id: str
	bits: int
	canShowInBitsCard: bool
	__typename: str

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesData(TypedDict):
	id: str
	prefix: str
	type: str
	campaign: NoneType
	tiers: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesDataTiersData]
	__typename: str

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsData(TypedDict):
	templateURL: str
	nodes: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesData]
	__typename: str

class VideoCommentsResponseVideoDataOwnerDataCheerData(TypedDict):
	id: str
	cheerGroups: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsData]
	__typename: str

class VideoCommentsResponseVideoDataOwnerDataSelfData(TypedDict):
	isModerator: bool
	__typename: str

class VideoCommentsResponseVideoDataOwnerData(TypedDict):
	id: str
	login: str
	broadcastBadges: List[VideoCommentsResponseVideoDataOwnerDataBroadcastbadgesData]
	cheer: VideoCommentsResponseVideoDataOwnerDataCheerData
	__typename: str
	self: Union[NoneType, VideoCommentsResponseVideoDataOwnerDataSelfData]

class VideoCommentsResponseVideoData(TypedDict):
	id: str
	broadcastType: str
	lengthSeconds: int
	owner: VideoCommentsResponseVideoDataOwnerData
	__typename: str

class VideoCommentsResponseRequestinfoData(TypedDict):
	countryCode: str
	__typename: str

class VideoCommentsResponse(TypedDict):
	badges: List[VideoCommentsResponseBadgesData]
	cheerConfig: VideoCommentsResponseCheerconfigData
	__typename: str
	currentUser: Union[NoneType, VideoCommentsResponseCurrentuserData]
	video: VideoCommentsResponseVideoData
	requestInfo: VideoCommentsResponseRequestinfoData

class VideoCommentsByOffsetOrCursorRequest1(TypedDict):
	videoID: str
	contentOffsetSeconds: Falsy[int]

class VideoCommentsByOffsetOrCursorRequest2(TypedDict):
	videoID: str
	cursor: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCreatorDataChannelData(TypedDict):
	id: str
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCreatorData(TypedDict):
	id: str
	channel: VideoCommentsByOffsetOrCursorResponseVideoDataCreatorDataChannelData
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataCommenterData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsDataEmoteData(TypedDict):
	id: str
	emoteID: str
	from_: Falsy[int] # WARNING: ADDED UNDERSCORE
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsData(TypedDict):
	emote: Union[NoneType, VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsDataEmoteData]
	text: str
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataUserbadgesData(TypedDict):
	id: str
	setID: Falsy[str]
	version: Falsy[str]
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageData(TypedDict):
	fragments: Falsy[List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsData]]
	userBadges: Falsy[List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataUserbadgesData]]
	userColor: Union[NoneType, str]
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeData(TypedDict):
	id: str
	commenter: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataCommenterData
	contentOffsetSeconds: Falsy[int]
	createdAt: str
	message: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageData
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesData(TypedDict):
	cursor: str
	node: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeData
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataPageinfoData(TypedDict):
	hasNextPage: bool
	hasPreviousPage: bool
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsData(TypedDict):
	edges: List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesData]
	pageInfo: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataPageinfoData
	__typename: str

class VideoCommentsByOffsetOrCursorResponseVideoData(TypedDict):
	id: str
	creator: VideoCommentsByOffsetOrCursorResponseVideoDataCreatorData
	comments: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsData
	__typename: str

class VideoCommentsByOffsetOrCursorResponse(TypedDict):
	video: VideoCommentsByOffsetOrCursorResponseVideoData

class VideoMarkersChatCommandRequest(TypedDict):
	channelLogin: str

class VideoMarkersChatCommandResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str
	__typename: str

class VideoMarkersChatCommandResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoMarkersChatCommandResponseUserDataStreamData]
	__typename: str

class VideoMarkersChatCommandResponse(TypedDict):
	user: VideoMarkersChatCommandResponseUserData

class VideoMetadataRequest(TypedDict):
	channelLogin: str
	videoID: str

class VideoMetadataResponseUserDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str
	__typename: str

class VideoMetadataResponseUserDataStreamData(TypedDict):
	id: str
	viewersCount: int
	__typename: str

class VideoMetadataResponseUserDataFollowersData(TypedDict):
	totalCount: int
	__typename: str

class VideoMetadataResponseUserData(TypedDict):
	id: str
	primaryColorHex: str
	isPartner: bool
	profileImageURL: str
	lastBroadcast: VideoMetadataResponseUserDataLastbroadcastData
	stream: Union[NoneType, VideoMetadataResponseUserDataStreamData]
	followers: VideoMetadataResponseUserDataFollowersData
	__typename: str

class VideoMetadataResponseCurrentuserData(TypedDict):
	id: str
	__typename: str

class VideoMetadataResponseVideoDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str
	__typename: str

class VideoMetadataResponseVideoDataGameData(TypedDict):
	id: str
	slug: str
	boxArtURL: str
	name: str
	displayName: str
	__typename: str

class VideoMetadataResponseVideoData(TypedDict):
	id: str
	title: str
	description: NoneType
	previewThumbnailURL: str
	createdAt: str
	viewCount: int
	publishedAt: str
	lengthSeconds: int
	broadcastType: str
	owner: VideoMetadataResponseVideoDataOwnerData
	game: VideoMetadataResponseVideoDataGameData
	__typename: str

class VideoMetadataResponse(TypedDict):
	user: VideoMetadataResponseUserData
	currentUser: Union[NoneType, VideoMetadataResponseCurrentuserData]
	video: VideoMetadataResponseVideoData

class VideoPlayer_AgeGateOverlayBroadcasterRequestInputData(TypedDict):
	login: Union[NoneType, str]
	ownsVideoID: Union[str, NoneType]

class VideoPlayer_AgeGateOverlayBroadcasterRequest(TypedDict):
	input: VideoPlayer_AgeGateOverlayBroadcasterRequestInputData

class VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeDataAdpropertiesData(TypedDict):
	requiredAge: Falsy[int]
	__typename: str

class VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeData(TypedDict):
	id: str
	login: str
	adProperties: VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeDataAdpropertiesData
	__typename: str

class VideoPlayer_AgeGateOverlayBroadcasterResponse(TypedDict):
	userByAttribute: VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeData

class VideoPlayer_ChapterSelectButtonVideoRequest(TypedDict):
	includePrivate: bool
	videoID: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataMomentsData(TypedDict):
	edges: Falsy[List[Any]]
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData(TypedDict):
	id: str
	displayName: str
	boxArtURL: str
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataDetailsData(TypedDict):
	game: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataVideoData(TypedDict):
	id: str
	lengthSeconds: int
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeData(TypedDict):
	moments: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataMomentsData
	id: str
	durationMilliseconds: int
	positionMilliseconds: Falsy[int]
	type: str
	description: str
	subDescription: Falsy[str]
	thumbnailURL: Falsy[str]
	details: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataDetailsData
	video: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataVideoData
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesData(TypedDict):
	node: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeData
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsData(TypedDict):
	edges: Falsy[List[VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesData]]
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoData(TypedDict):
	id: str
	moments: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsData
	__typename: str

class VideoPlayer_ChapterSelectButtonVideoResponse(TypedDict):
	video: VideoPlayer_ChapterSelectButtonVideoResponseVideoData

class VideoPlayer_MutedSegmentsAlertOverlayRequest(TypedDict):
	includePrivate: bool
	vodID: str

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData(TypedDict):
	duration: int
	offset: Falsy[int]
	__typename: str

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionData(TypedDict):
	nodes: List[VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData]
	__typename: str

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoData(TypedDict):
	mutedSegmentConnection: Union[NoneType, VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionData]
	__typename: str

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoData(TypedDict):
	id: str
	muteInfo: VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoData
	__typename: str

class VideoPlayer_MutedSegmentsAlertOverlayResponse(TypedDict):
	video: VideoPlayer_MutedSegmentsAlertOverlayResponseVideoData

class VideoPlayer_VideoSourceManagerRequestInputData(TypedDict):
	login: Union[NoneType, str]
	ownsVideoID: Union[str, NoneType]
	ownsCollectionID: NoneType
	broadcasterOfClipSlug: Union[str, NoneType]

class VideoPlayer_VideoSourceManagerRequest(TypedDict):
	input: VideoPlayer_VideoSourceManagerRequestInputData

class VideoPlayer_VideoSourceManagerResponseUserbyattributeData(TypedDict):
	id: str
	__typename: str

class VideoPlayer_VideoSourceManagerResponse(TypedDict):
	userByAttribute: Union[NoneType, VideoPlayer_VideoSourceManagerResponseUserbyattributeData]

class VideoPlayer_VODSeekbarRequest(TypedDict):
	includePrivate: bool
	vodID: str

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData(TypedDict):
	duration: int
	offset: Falsy[int]
	__typename: str

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionData(TypedDict):
	nodes: List[VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData]
	__typename: str

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoData(TypedDict):
	mutedSegmentConnection: Union[NoneType, VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionData]
	__typename: str

class VideoPlayer_VODSeekbarResponseVideoData(TypedDict):
	id: str
	lengthSeconds: int
	muteInfo: VideoPlayer_VODSeekbarResponseVideoDataMuteinfoData
	__typename: str

class VideoPlayer_VODSeekbarResponse(TypedDict):
	video: VideoPlayer_VODSeekbarResponseVideoData

class VideoPlayer_VODSeekbarPreviewVideoRequest(TypedDict):
	includePrivate: bool
	videoID: str

class VideoPlayer_VODSeekbarPreviewVideoResponseVideoData(TypedDict):
	id: str
	seekPreviewsURL: str
	__typename: str

class VideoPlayer_VODSeekbarPreviewVideoResponse(TypedDict):
	video: VideoPlayer_VODSeekbarPreviewVideoResponseVideoData

class VideoPlayerClipPostplayRecommendationsOverlayRequest(TypedDict):
	slug: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str
	__typename: str
	stream: NoneType

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataGameData(TypedDict):
	id: str
	displayName: str
	name: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataGameData(TypedDict):
	id: str
	displayName: str
	name: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	title: str
	thumbnailURL: str
	viewCount: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataGameData
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataGameData(TypedDict):
	id: str
	displayName: str
	name: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	title: str
	thumbnailURL: str
	viewCount: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataGameData
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataGameData(TypedDict):
	id: str
	displayName: str
	name: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	title: str
	thumbnailURL: str
	viewCount: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataGameData
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsData(TypedDict):
	broadcaster: List[VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterData]
	game: List[VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameData]
	top: List[VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopData]
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoDataGameData(TypedDict):
	id: str
	displayName: str
	name: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoData(TypedDict):
	id: str
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoDataGameData
	lengthSeconds: int
	previewThumbnailURL: str
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	videoOffsetSeconds: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataGameData
	relatedClips: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsData
	video: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoData
	__typename: str

class VideoPlayerClipPostplayRecommendationsOverlayResponse(TypedDict):
	clip: VideoPlayerClipPostplayRecommendationsOverlayResponseClipData

class VideoPlayerClipsButtonBroadcasterRequestInputData(TypedDict):
	login: Union[NoneType, str]
	ownsVideoID: Union[str, NoneType]

class VideoPlayerClipsButtonBroadcasterRequest(TypedDict):
	input: VideoPlayerClipsButtonBroadcasterRequestInputData

class VideoPlayerClipsButtonBroadcasterResponseUserbyattributeDataStreamData(TypedDict):
	id: str
	isEncrypted: bool
	__typename: str

class VideoPlayerClipsButtonBroadcasterResponseUserbyattributeData(TypedDict):
	id: str
	login: str
	stream: Union[NoneType, VideoPlayerClipsButtonBroadcasterResponseUserbyattributeDataStreamData]
	__typename: str

class VideoPlayerClipsButtonBroadcasterResponse(TypedDict):
	userByAttribute: VideoPlayerClipsButtonBroadcasterResponseUserbyattributeData

class VideoPlayerOfflineRecommendationsOverlayRequest(TypedDict):
	login: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str
	__typename: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	previewThumbnailURL: str
	game: VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeDataGameData
	__typename: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesData(TypedDict):
	node: VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeData
	__typename: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosData(TypedDict):
	edges: Falsy[List[VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesData]]
	__typename: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserData(TypedDict):
	id: str
	videos: VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosData
	__typename: str

class VideoPlayerOfflineRecommendationsOverlayResponse(TypedDict):
	user: VideoPlayerOfflineRecommendationsOverlayResponseUserData

class VideoPlayerStatusOverlayChannelRequest(TypedDict):
	channel: str

class VideoPlayerStatusOverlayChannelResponseUserDataStreamData(TypedDict):
	id: str
	type: str
	__typename: str

class VideoPlayerStatusOverlayChannelResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoPlayerStatusOverlayChannelResponseUserDataStreamData]
	__typename: str

class VideoPlayerStatusOverlayChannelResponse(TypedDict):
	user: VideoPlayerStatusOverlayChannelResponseUserData

class VideoPlayerStreamMetadataRequest(TypedDict):
	channel: str

class VideoPlayerStreamMetadataResponseUserDataStreamData(TypedDict):
	id: str
	isEncrypted: bool
	__typename: str

class VideoPlayerStreamMetadataResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoPlayerStreamMetadataResponseUserDataStreamData]
	__typename: str

class VideoPlayerStreamMetadataResponse(TypedDict):
	user: VideoPlayerStreamMetadataResponseUserData

class VideoPlayerVODPostplayRecommendationsRequest(TypedDict):
	videoID: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str
	__typename: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataSelfData(TypedDict):
	viewingHistory: NoneType
	__typename: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeData(TypedDict):
	id: str
	createdAt: str
	lengthSeconds: int
	title: str
	previewThumbnailURL: str
	game: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataGameData
	self: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataSelfData
	__typename: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesData(TypedDict):
	node: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeData
	__typename: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosData(TypedDict):
	edges: List[VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesData]
	__typename: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerData(TypedDict):
	id: str
	displayName: str
	videos: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosData
	__typename: str

class VideoPlayerVODPostplayRecommendationsResponseVideoData(TypedDict):
	id: str
	owner: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerData
	__typename: str

class VideoPlayerVODPostplayRecommendationsResponse(TypedDict):
	video: VideoPlayerVODPostplayRecommendationsResponseVideoData

class VideoPreviewCard__VideoMomentsRequest(TypedDict):
	videoId: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData(TypedDict):
	id: str
	slug: str
	displayName: str
	boxArtURL: str
	__typename: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsData(TypedDict):
	game: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData
	__typename: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataVideoData(TypedDict):
	id: str
	lengthSeconds: int
	__typename: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeData(TypedDict):
	id: str
	durationMilliseconds: int
	positionMilliseconds: Falsy[int]
	type: str
	description: str
	thumbnailURL: Falsy[str]
	details: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsData
	__typename: str
	video: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataVideoData

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeData
	__typename: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsData(TypedDict):
	edges: Falsy[List[VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesData]]
	__typename: str

class VideoPreviewCard__VideoMomentsResponseVideoData(TypedDict):
	id: str
	moments: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsData
	__typename: str

class VideoPreviewCard__VideoMomentsResponse(TypedDict):
	video: VideoPreviewCard__VideoMomentsResponseVideoData

class VideoPreviewOverlayRequest(TypedDict):
	login: str

class VideoPreviewOverlayResponseUserDataStreamData(TypedDict):
	id: str
	previewImageURL: str
	restrictionType: NoneType
	__typename: str

class VideoPreviewOverlayResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoPreviewOverlayResponseUserDataStreamData]
	__typename: str

class VideoPreviewOverlayResponse(TypedDict):
	user: VideoPreviewOverlayResponseUserData

class VODMidrollManagerRequest(TypedDict):
	isVOD: bool
	vodID: str
	isCollection: bool
	collectionID: Falsy[str]

class VODMidrollManagerResponseVideoDataOwnerDataAdpropertiesData(TypedDict):
	hasVodAdsEnabled: bool
	vodArchiveMidrolls: str
	vodArchiveMidrollsBreakLength: int
	vodArchiveMidrollsFrequency: int
	__typename: str

class VODMidrollManagerResponseVideoDataOwnerData(TypedDict):
	id: str
	adProperties: VODMidrollManagerResponseVideoDataOwnerDataAdpropertiesData
	__typename: str

class VODMidrollManagerResponseVideoData(TypedDict):
	id: str
	broadcastType: str
	owner: VODMidrollManagerResponseVideoDataOwnerData
	__typename: str

class VODMidrollManagerResponse(TypedDict):
	video: VODMidrollManagerResponseVideoData

class WatchStreakExperimentRequest(TypedDict):
	channelID: Falsy[str]

class WatchStreakExperimentResponseChannelviewermilestonesettingsData(TypedDict):
	id: str
	isWatchStreakOptOut: bool
	isInWatchStreakProgressExperiment: bool
	__typename: str

class WatchStreakExperimentResponse(TypedDict):
	channelViewerMilestoneSettings: Union[NoneType, WatchStreakExperimentResponseChannelviewermilestonesettingsData]

class Whispers_Whispers_UserWhisperThreadsRequest(TypedDict):
	...

class Whispers_Whispers_UserWhisperThreadsResponseCurrentuserDataWhisperthreadsData(TypedDict):
	edges: Falsy[List[Any]]
	__typename: str

class Whispers_Whispers_UserWhisperThreadsResponseCurrentuserData(TypedDict):
	id: str
	login: str
	whisperThreads: Whispers_Whispers_UserWhisperThreadsResponseCurrentuserDataWhisperthreadsData
	__typename: str

class Whispers_Whispers_UserWhisperThreadsResponse(TypedDict):
	currentUser: Whispers_Whispers_UserWhisperThreadsResponseCurrentuserData

class WithIsStreamLiveQueryRequest(TypedDict):
	id: str

class WithIsStreamLiveQueryResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str
	__typename: str

class WithIsStreamLiveQueryResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, WithIsStreamLiveQueryResponseUserDataStreamData]
	__typename: str

class WithIsStreamLiveQueryResponse(TypedDict):
	user: WithIsStreamLiveQueryResponseUserData

class AccessGetFeatureClipRestrictionsQuery(Endpoint):
	sha256Hash = '14ae9c701ed1113c7c16a0cb613e7ba7eca000bc1b907c2969f2756e8af5a05b'
	operation_name = 'AccessGetFeatureClipRestrictionsQuery'
	def build_query(self, variables: AccessGetFeatureClipRestrictionsQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AcknowledgeUnbanRequestPrompt(Endpoint):
	sha256Hash = '814210afb9c7c392ce35028f3a3aebfff446c3be2925af8c9ff4c04a34fe8c5f'
	operation_name = 'AcknowledgeUnbanRequestPrompt'
	def build_query(self, variables: AcknowledgeUnbanRequestPromptRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AvailableEmotesForChannelPaginated(Endpoint):
	sha256Hash = '6c45e0ecaa823cc7db3ecdd1502af2223c775bdcfb0f18a3a0ce9a0b7db8ef6c'
	operation_name = 'AvailableEmotesForChannelPaginated'
	def build_query(self, variables: AvailableEmotesForChannelPaginatedRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BlockedUsers(Endpoint):
	sha256Hash = '8044e3fd61f8158a39e07b38f5d1a279d1fdb748faa9889fde046feae640f76b'
	operation_name = 'BlockedUsers'
	def build_query(self, variables: BlockedUsersRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BrowsePage_AllDirectories(Endpoint):
	sha256Hash = '2f67f71ba89f3c0ed26a141ec00da1defecb2303595f5cda4298169549783d9e'
	operation_name = 'BrowsePage_AllDirectories'
	def build_query(self, variables: Union[BrowsePage_AllDirectoriesRequest1, BrowsePage_AllDirectoriesRequest2] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BrowseVerticalDirectory(Endpoint):
	sha256Hash = 'd27ea34dd3c0a4c183deb152c1223b44794e7fd3c336bdc15aa61abc65cc2b76'
	operation_name = 'BrowseVerticalDirectory'
	def build_query(self, variables: BrowseVerticalDirectoryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CanCreateClip(Endpoint):
	sha256Hash = 'ea1796b7893cd9ab447c989967e8441ea230ea54091f63e71d4b189b72d17215'
	operation_name = 'CanCreateClip'
	def build_query(self, variables: CanCreateClipRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CanViewersExportQuery(Endpoint):
	sha256Hash = '8f5d5163e711a884a88079cbcd24d68adc6a90a7fcb4030a5aef266372c33fd0'
	operation_name = 'CanViewersExportQuery'
	def build_query(self, variables: CanViewersExportQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelAvatar(Endpoint):
	sha256Hash = '12575ab92ea9444d8bade6de529b288a05073617f319c87078b3a89e74cd783a'
	operation_name = 'ChannelAvatar'
	def build_query(self, variables: ChannelAvatarRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelClipCore(Endpoint):
	sha256Hash = 'a33067cdf92191dccfb53aa86f878a2c271e6a3587a6731dc8275e5751dd133f'
	operation_name = 'ChannelClipCore'
	def build_query(self, variables: ChannelClipCoreRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelCollaborationEligibilityQuery(Endpoint):
	sha256Hash = 'f32cb49f6bc54a4dc182b54c6e247d8344f8a16cc255acbc2e18fbd145df4cb2'
	operation_name = 'ChannelCollaborationEligibilityQuery'
	def build_query(self, variables: ChannelCollaborationEligibilityQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelLeaderboards(Endpoint):
	sha256Hash = 'ccc0fe65d86216ca35fae890e29e53e508dc3ff6bbe4fd893ca9b5b87dffbe5e'
	operation_name = 'ChannelLeaderboards'
	def build_query(self, variables: ChannelLeaderboardsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPage_SetSessionStatus(Endpoint):
	sha256Hash = '8521e08af74c8cb5128e4bb99fa53b591391cb19492e65fb0489aeee2f96947f'
	operation_name = 'ChannelPage_SetSessionStatus'
	def build_query(self, variables: ChannelPage_SetSessionStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPage_SubscribeButton_User(Endpoint):
	sha256Hash = '53b7d2bfc430935ea80f813edba87f2447d5401acae5b6d8c885534997c3ca15'
	operation_name = 'ChannelPage_SubscribeButton_User'
	def build_query(self, variables: Union[ChannelPage_SubscribeButton_UserRequest1, ChannelPage_SubscribeButton_UserRequest2] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPointsContext(Endpoint):
	sha256Hash = '374314de591e69925fce3ddc2bcf085796f56ebb8cad67a0daa3165c03adc345'
	operation_name = 'ChannelPointsContext'
	def build_query(self, variables: ChannelPointsContextRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPointsGlobalContext(Endpoint):
	sha256Hash = 'd3fa3a96e78a3e62bdd3ef3c4effafeda52442906cec41a9440e609a388679e2'
	operation_name = 'ChannelPointsGlobalContext'
	def build_query(self, variables: ChannelPointsGlobalContextRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPointsPredictionContext(Endpoint):
	sha256Hash = 'beb846598256b75bd7c1fe54a80431335996153e358ca9c7837ce7bb83d7d383'
	operation_name = 'ChannelPointsPredictionContext'
	def build_query(self, variables: ChannelPointsPredictionContextRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelShell(Endpoint):
	sha256Hash = '580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe'
	operation_name = 'ChannelShell'
	def build_query(self, variables: ChannelShellRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelSkins(Endpoint):
	sha256Hash = 'b035de8611dc0bfbea6d0ce43af3f95319220fb5d23fc7a1448c16e1d83fed1c'
	operation_name = 'ChannelSkins'
	def build_query(self, variables: ChannelSkinsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelSocialButtons(Endpoint):
	sha256Hash = '597b4ee27086064ccd59bef5c02775e9963cc3354f2095159484e816ccc1aec2'
	operation_name = 'ChannelSocialButtons'
	def build_query(self, variables: ChannelSocialButtonsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelSupportButtons(Endpoint):
	sha256Hash = '834a75e1c06cffada00f0900664a5033e392f6fb655fae8d2e25b21b340545a9'
	operation_name = 'ChannelSupportButtons'
	def build_query(self, variables: ChannelSupportButtonsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelVideoCore(Endpoint):
	sha256Hash = 'cf1ccf6f5b94c94d662efec5223dfb260c9f8bf053239a76125a58118769e8e2'
	operation_name = 'ChannelVideoCore'
	def build_query(self, variables: ChannelVideoCoreRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelVideoShelvesQuery(Endpoint):
	sha256Hash = 'eea6c7a6baaa6ee60825f469c943cfda7e7c2415c01c64d7fd1407d172e82a7b'
	operation_name = 'ChannelVideoShelvesQuery'
	def build_query(self, variables: ChannelVideoShelvesQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_ChannelData(Endpoint):
	sha256Hash = '3c445f9a8315fa164f2d3fb12c2f932754c2f2c129f952605b9ec6cf026dd362'
	operation_name = 'Chat_ChannelData'
	def build_query(self, variables: Chat_ChannelDataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_EarnedBadges_InitialSubStatus(Endpoint):
	sha256Hash = '85a95b95a12628668eaac4d2862b53bb376dba0325c80eae8f26539cedc5f1a3'
	operation_name = 'Chat_EarnedBadges_InitialSubStatus'
	def build_query(self, variables: Chat_EarnedBadges_InitialSubStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_OrbisPresetText(Endpoint):
	sha256Hash = '960bf1fac4adb3f4e99b0c67627180d5f5ebb6e46139b1149fbdeab68f7f62e1'
	operation_name = 'Chat_OrbisPresetText'
	def build_query(self, variables: Chat_OrbisPresetTextRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_ShareResub_ChannelData(Endpoint):
	sha256Hash = '1cef2e84b602f767839e5ffd489e81536e9d11e0be250bb85a17974cedad8f54'
	operation_name = 'Chat_ShareResub_ChannelData'
	def build_query(self, variables: Chat_ShareResub_ChannelDataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_UserData(Endpoint):
	sha256Hash = '39985d1ff9324442a3a5df1be212e1bc4f358a31100e5025c4e61a07d7e70743'
	operation_name = 'Chat_UserData'
	def build_query(self, variables: Chat_UserDataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatClip(Endpoint):
	sha256Hash = '9aa558e066a22227c5ef2c0a8fded3aaa57d35181ad15f63df25bff516253a90'
	operation_name = 'ChatClip'
	def build_query(self, variables: ChatClipRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatFilterContextManager_User(Endpoint):
	sha256Hash = '98821224809f26e3f3a627a0e30134b00c4db33b602b4249cec518a8c21fe902'
	operation_name = 'ChatFilterContextManager_User'
	def build_query(self, variables: ChatFilterContextManager_UserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatInput(Endpoint):
	sha256Hash = 'd8ab574eb44e3e82aabc96fc9c59af6eafead3e96262910a6396c007e7a11e05'
	operation_name = 'ChatInput'
	def build_query(self, variables: ChatInputRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatInput_Badges(Endpoint):
	sha256Hash = '8cb0eae66555ad6dc76aaa111d191ea6174c743f996d506f530e479f28e6b37c'
	operation_name = 'ChatInput_Badges'
	def build_query(self, variables: ChatInput_BadgesRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatList_Badges(Endpoint):
	sha256Hash = '838a7e0b47c09cac05f93ff081a9ff4f876b68f7624f0fc465fe30031e372fc2'
	operation_name = 'ChatList_Badges'
	def build_query(self, variables: ChatList_BadgesRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatModeratorStrikeStatus(Endpoint):
	sha256Hash = '7f50f7190a840cd9fe9a91398f34ebb690eeba7cb28bce70e4cbf7ed1d06f268'
	operation_name = 'ChatModeratorStrikeStatus'
	def build_query(self, variables: ChatModeratorStrikeStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatRestrictions(Endpoint):
	sha256Hash = '7514aeb3d2c203087b83e920f8d36eb18a5ca1bfa96a554ed431255ecbbbc089'
	operation_name = 'ChatRestrictions'
	def build_query(self, variables: ChatRestrictionsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatRoomBanStatus(Endpoint):
	sha256Hash = '319f2a9a3ac7ddecd7925944416c14b818b65676ab69da604460b68938d22bea'
	operation_name = 'ChatRoomBanStatus'
	def build_query(self, variables: ChatRoomBanStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatRoomState(Endpoint):
	sha256Hash = '9e0f79669e31950c658459564bc4cff236ac9c03e534cc32769ac58bc0cdd708'
	operation_name = 'ChatRoomState'
	def build_query(self, variables: ChatRoomStateRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatScreenReaderAutoAnnounce(Endpoint):
	sha256Hash = '3ddf79c5dd411106eae1d44801f1a123ecf82cad7e973575b18367b2c5d63a0c'
	operation_name = 'ChatScreenReaderAutoAnnounce'
	def build_query(self, variables: ChatScreenReaderAutoAnnounceRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClaimCommunityPoints(Endpoint):
	sha256Hash = '46aaeebe02c99afdf4fc97c7c0cba964124bf6b0af229395f1f6d1feed05b3d0'
	operation_name = 'ClaimCommunityPoints'
	def build_query(self, variables: ClaimCommunityPointsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipMetadata(Endpoint):
	sha256Hash = '49817470e0129051cd93c86069aee755795f1a952688f0111bac71a49841ece7'
	operation_name = 'ClipMetadata'
	def build_query(self, variables: ClipMetadataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipsCards__User(Endpoint):
	sha256Hash = '4eb8f85fc41a36c481d809e8e99b2a32127fdb7647c336d27743ec4a88c4ea44'
	operation_name = 'ClipsCards__User'
	def build_query(self, variables: ClipsCards__UserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipsExperimentEnrollmentStatus(Endpoint):
	sha256Hash = '0575e09a580d3a30bffe06b09ebda047ebebf57ab86a4d7329527d312e8dea22'
	operation_name = 'ClipsExperimentEnrollmentStatus'
	def build_query(self, variables: ClipsExperimentEnrollmentStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CollectionCarouselQuery(Endpoint):
	sha256Hash = '0ca5b673f0a160f85267d7c5fbfe797f1d7b8129025aedc353cb5c99f2c94fec'
	operation_name = 'CollectionCarouselQuery'
	def build_query(self, variables: CollectionCarouselQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommercialCommandHandler_ChannelData(Endpoint):
	sha256Hash = 'ec415677f12d805693445931552fbbbf60f44f96826019578e15a8171dcd4cbb'
	operation_name = 'CommercialCommandHandler_ChannelData'
	def build_query(self, variables: CommercialCommandHandler_ChannelDataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommonHooks_BlockedUsers(Endpoint):
	sha256Hash = '7c87171d7497df41f9938d2bc18a26f7a97f32f11b7f28c4826950c4ebe000b2'
	operation_name = 'CommonHooks_BlockedUsers'
	def build_query(self, variables: CommonHooks_BlockedUsersRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunityOnboardingAllowlist(Endpoint):
	sha256Hash = 'b9119d11f5d434ed5482a7598000066f49dccbcb2395ae11105e28469370d110'
	operation_name = 'CommunityOnboardingAllowlist'
	def build_query(self, variables: CommunityOnboardingAllowlistRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunityPointsAvailableClaim(Endpoint):
	sha256Hash = '3a4ca75d2a784eea5c40f38a60fe9f6ab8c565c030de06c561398ee5099f818c'
	operation_name = 'CommunityPointsAvailableClaim'
	def build_query(self, variables: CommunityPointsAvailableClaimRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunityPointsChatPrivateCalloutUser(Endpoint):
	sha256Hash = '15b66a0a6b743c72a63c273f2bfc4155c4209c1a85c29b6847474717877c3507'
	operation_name = 'CommunityPointsChatPrivateCalloutUser'
	def build_query(self, variables: CommunityPointsChatPrivateCalloutUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunitySupportSettings(Endpoint):
	sha256Hash = '11b3e9eeff8190e1fa7b97cafbcb2427e3a54289676b030fc16a7ae125702da0'
	operation_name = 'CommunitySupportSettings'
	def build_query(self, variables: CommunitySupportSettingsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Consent(Endpoint):
	sha256Hash = '012157dd34a0fb2f401124cd5a66b3f333a6ea572f75ba0db91a69bae0c3bd13'
	operation_name = 'Consent'
	def build_query(self, variables: ConsentRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ContentClassificationContext(Endpoint):
	sha256Hash = '57bb6c1aca3631b2b3e74b1c3c8adbecbbcc3becb70ec52d7c5ef0f90d7c3b02'
	operation_name = 'ContentClassificationContext'
	def build_query(self, variables: Union[ContentClassificationContextRequest1, ContentClassificationContextRequest2, ContentClassificationContextRequest3] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ContentPolicyPropertiesQuery(Endpoint):
	sha256Hash = 'e2c1cb362a9b601440d764b2db98eaf4fc21b9091973b158c8b702716419545a'
	operation_name = 'ContentPolicyPropertiesQuery'
	def build_query(self, variables: ContentPolicyPropertiesQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CoreActionsCurrentUser(Endpoint):
	sha256Hash = '6b5b63a013cf66a995d61f71a508ab5c8e4473350c5d4136f846ba65e8101e95'
	operation_name = 'CoreActionsCurrentUser'
	def build_query(self, variables: CoreActionsCurrentUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CurrentUserBannedStatus(Endpoint):
	sha256Hash = 'dede147839ea4a357639f1dc3d3eb978556e82eefb7abdefce8911d0e23a63ad'
	operation_name = 'CurrentUserBannedStatus'
	def build_query(self, variables: CurrentUserBannedStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CurrentUserModeratorStatus(Endpoint):
	sha256Hash = '1684c97f8b9f49bbeff32bfd6fcc08bd4e631f16b4fca43bdcc7e14e20eff110'
	operation_name = 'CurrentUserModeratorStatus'
	def build_query(self, variables: Union[CurrentUserModeratorStatusRequest1, CurrentUserModeratorStatusRequest2] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CurrentUserStrikeStatus(Endpoint):
	sha256Hash = '954bb138c800c581b291b7068a9225f7e139eb2b5066bc5840a9b251f5eaf11b'
	operation_name = 'CurrentUserStrikeStatus'
	def build_query(self, variables: CurrentUserStrikeStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DirectoryCollection_BrowsableCollection(Endpoint):
	sha256Hash = '459f2a65ca11d3765450546a68980ac5868a6b4cce1a9e10bccb9a6e52d2c30d'
	operation_name = 'DirectoryCollection_BrowsableCollection'
	def build_query(self, variables: Union[DirectoryCollection_BrowsableCollectionRequest1, DirectoryCollection_BrowsableCollectionRequest2] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DropCurrentSessionContext(Endpoint):
	sha256Hash = '4d06b702d25d652afb9ef835d2a550031f1cf762b193523a92166f40ea3d142b'
	operation_name = 'DropCurrentSessionContext'
	def build_query(self, variables: DropCurrentSessionContextRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DropsHighlightService_AvailableDrops(Endpoint):
	sha256Hash = '19e0b383db0be3dc917379fddcbf9dfa7c49f1fcc543d920f39f4efd054bc636'
	operation_name = 'DropsHighlightService_AvailableDrops'
	def build_query(self, variables: DropsHighlightService_AvailableDropsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class EmotesForChannelFollowStatus(Endpoint):
	sha256Hash = '40cf0bf434717c70fa192e8a7805ae8651fae53a410d609f02ad853e3af94e78'
	operation_name = 'EmotesForChannelFollowStatus'
	def build_query(self, variables: EmotesForChannelFollowStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FeaturedClipsShelfCover(Endpoint):
	sha256Hash = '90e7b62983b247aea06aafc7e20699889914e331daec97f68fd33d714cc17738'
	operation_name = 'FeaturedClipsShelfCover'
	def build_query(self, variables: FeaturedClipsShelfCoverRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FeaturedContentCarouselStreams(Endpoint):
	sha256Hash = '663a12a5bcf38aa3f6f566e328e9e7de44986746101c0ad10b50186f768b41b7'
	operation_name = 'FeaturedContentCarouselStreams'
	def build_query(self, variables: FeaturedContentCarouselStreamsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FilterableVideoTower_Videos(Endpoint):
	sha256Hash = 'acea7539a293dfd30f0b0b81a263134bb5d9a7175592e14ac3f7c77b192de416'
	operation_name = 'FilterableVideoTower_Videos'
	def build_query(self, variables: Union[FilterableVideoTower_VideosRequest1, FilterableVideoTower_VideosRequest2] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowButton_FollowUser(Endpoint):
	sha256Hash = '800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08'
	operation_name = 'FollowButton_FollowUser'
	def build_query(self, variables: FollowButton_FollowUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowButton_UnfollowUser(Endpoint):
	sha256Hash = 'f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880'
	operation_name = 'FollowButton_UnfollowUser'
	def build_query(self, variables: FollowButton_UnfollowUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowButton_User(Endpoint):
	sha256Hash = '870906a2de25d7488239dbeb947dafe3e5697f1fef2e8bce6601555a17e4d86d'
	operation_name = 'FollowButton_User'
	def build_query(self, variables: FollowButton_UserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedIndex_CurrentUser(Endpoint):
	sha256Hash = '740647c696400dad6767b9407089fc2d52e88c4227dbb1f5cd763e015cc61df2'
	operation_name = 'FollowedIndex_CurrentUser'
	def build_query(self, variables: FollowedIndex_CurrentUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedIndex_FollowCount(Endpoint):
	sha256Hash = '8945379bb5b05b905ba4e3669d02b863a3089fae81befc9f2a82dbd45ae6efc5'
	operation_name = 'FollowedIndex_FollowCount'
	def build_query(self, variables: FollowedIndex_FollowCountRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedStreams(Endpoint):
	sha256Hash = '10fbb27d9260e3688cd9febdbdd3e21e3331d698ca282dc5f0cf0d29bb468fdd'
	operation_name = 'FollowedStreams'
	def build_query(self, variables: FollowedStreamsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedStreamsContinueWatching(Endpoint):
	sha256Hash = 'c689d0645defdd63aaab322166a570c785cefa97b6e97c1a1e7fb66ccdfcad82'
	operation_name = 'FollowedStreamsContinueWatching'
	def build_query(self, variables: FollowedStreamsContinueWatchingRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedVideos_CurrentUser(Endpoint):
	sha256Hash = '11d0ddb94121afab8fa8b641e01f038db35892f95b4e4b9e5380eaa33d5e4a8c'
	operation_name = 'FollowedVideos_CurrentUser'
	def build_query(self, variables: FollowedVideos_CurrentUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowingGames_CurrentUser(Endpoint):
	sha256Hash = 'f3c5d45175d623ed3d5ff4ca4c7de379ea6a1a4852236087dc1b81b7dbfd3114'
	operation_name = 'FollowingGames_CurrentUser'
	def build_query(self, variables: FollowingGames_CurrentUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowingLive_CurrentUser(Endpoint):
	sha256Hash = 'ecadcf350272dde399a63385cf888903d7fcd4c8fc6809a8469fe3753579d1c6'
	operation_name = 'FollowingLive_CurrentUser'
	def build_query(self, variables: FollowingLive_CurrentUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowingPage_RecommendedChannels(Endpoint):
	sha256Hash = '39c731d90e41de782e21c370c6e43bd23757fcaf98051e865016faef05c080b4'
	operation_name = 'FollowingPage_RecommendedChannels'
	def build_query(self, variables: FollowingPage_RecommendedChannelsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FrontPageNew_User(Endpoint):
	sha256Hash = '64bd07a2cbaca80699d62636d966cf6395a5d14a1f0a14282067dcb28b13eb11'
	operation_name = 'FrontPageNew_User'
	def build_query(self, variables: FrontPageNew_UserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetDisplayName(Endpoint):
	sha256Hash = 'ba351b3d3018c3779fcaa398507e41579ae6cf12ad123a04f090943c21dedb8a'
	operation_name = 'GetDisplayName'
	def build_query(self, variables: GetDisplayNameRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetGuestSessionBlocksAndBans(Endpoint):
	sha256Hash = '4a96b8e893624487d7eaf212f61e756e00354e969a19b0e01d2e863021d75974'
	operation_name = 'GetGuestSessionBlocksAndBans'
	def build_query(self, variables: GetGuestSessionBlocksAndBansRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetIDFromLogin(Endpoint):
	sha256Hash = '94e82a7b1e3c21e186daa73ee2afc4b8f23bade1fbbff6fe8ac133f50a2f58ca'
	operation_name = 'GetIDFromLogin'
	def build_query(self, variables: GetIDFromLoginRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetPinnedChat(Endpoint):
	sha256Hash = '2d099d4c9b6af80a07d8440140c4f3dbb04d516b35c401aab7ce8f60765308d5'
	operation_name = 'GetPinnedChat'
	def build_query(self, variables: GetPinnedChatRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetUserID(Endpoint):
	sha256Hash = 'bf6c594605caa0c63522f690156aa04bd434870bf963deb76668c381d16fcaa5'
	operation_name = 'GetUserID'
	def build_query(self, variables: GetUserIDRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GlobalBadges(Endpoint):
	sha256Hash = '9db27e18d61ee393ccfdec8c7d90f14f9a11266298c2e5eb808550b77d7bcdf6'
	operation_name = 'GlobalBadges'
	def build_query(self, variables: GlobalBadgesRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestListQuery(Endpoint):
	sha256Hash = '7a2267973bdd74b9ddd5d07ceabd73b5b5d13eae83b54d4436fb5a3fa26c3bc8'
	operation_name = 'GuestListQuery'
	def build_query(self, variables: GuestListQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestStarActiveJoinRequest(Endpoint):
	sha256Hash = 'ee299efe4c857e2ab673e57c0c29ff3171671dc4980ca3834f63d6e66ed16a8b'
	operation_name = 'GuestStarActiveJoinRequest'
	def build_query(self, variables: GuestStarActiveJoinRequestRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestStarBatchCollaborationQuery(Endpoint):
	sha256Hash = '096d50357df5e938f4fa83fe2acf25cb0f4886149aa81ddb9754eae98c05f2dd'
	operation_name = 'GuestStarBatchCollaborationQuery'
	def build_query(self, variables: GuestStarBatchCollaborationQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestStarChannelPageCollaborationQuery(Endpoint):
	sha256Hash = 'adb54eefd172fc9d310040afe5c158e2e41ec93dfe030067afa365178243ffa3'
	operation_name = 'GuestStarChannelPageCollaborationQuery'
	def build_query(self, variables: GuestStarChannelPageCollaborationQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HappeningNowSettings(Endpoint):
	sha256Hash = '6945ce7f7df91e52f21edc98ea04f63e5ab38f4e6f4b5699bdd652171f9a7b48'
	operation_name = 'HappeningNowSettings'
	def build_query(self, variables: HappeningNowSettingsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeOfflineCarousel(Endpoint):
	sha256Hash = '84e25789b04ac4dcaefd673cfb4259d39d03c6422838d09a4ed2aaf9b67054d8'
	operation_name = 'HomeOfflineCarousel'
	def build_query(self, variables: HomeOfflineCarouselRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfEditor(Endpoint):
	sha256Hash = '1079fccbb422d5bd48594cd8fdbfe4998f2ac4f331e3db93cba1cf2203f9901d'
	operation_name = 'HomeShelfEditor'
	def build_query(self, variables: HomeShelfEditorRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfGames(Endpoint):
	sha256Hash = 'cb7711739c2b520ebf89f3027863c0f985e8094df91cc5ef28896d57375a9700'
	operation_name = 'HomeShelfGames'
	def build_query(self, variables: HomeShelfGamesRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfUsers(Endpoint):
	sha256Hash = '3d9e1494fe4b426aa3ea81ff63dc87e784529a150bdc362c01cdb2c30373440f'
	operation_name = 'HomeShelfUsers'
	def build_query(self, variables: HomeShelfUsersRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfVideos(Endpoint):
	sha256Hash = '951c268434dc36a482c6f854215df953cf180fc2757f1e0e47aa9821258debf7'
	operation_name = 'HomeShelfVideos'
	def build_query(self, variables: HomeShelfVideosRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class incrementClipViewCount(Endpoint):
	sha256Hash = '6b2f169f994f2b93ff68774f6928de66a1e8cdb70a42f4af3a5a1ecc68ee759b'
	operation_name = 'incrementClipViewCount'
	def build_query(self, variables: incrementClipViewCountRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class LastUnbanRequest(Endpoint):
	sha256Hash = 'ff196f08b09d9f9f977610f676cfc56bc5e2f679ad773c1acc4f889defb9aebd'
	operation_name = 'LastUnbanRequest'
	def build_query(self, variables: LastUnbanRequestRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class LowerHomeHeader(Endpoint):
	sha256Hash = '08af264bf5d5231cadb05acaddce0992622f86a0d3d7f6f59955316564d3c008'
	operation_name = 'LowerHomeHeader'
	def build_query(self, variables: LowerHomeHeaderRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class MessageBuffer_Channel(Endpoint):
	sha256Hash = 'bfc959904f55b5003ae4674d4bea83ebdcd8867ad76e12f38957d433902d2fcc'
	operation_name = 'MessageBuffer_Channel'
	def build_query(self, variables: MessageBuffer_ChannelRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class MessageBufferChatHistory(Endpoint):
	sha256Hash = '33dba0e0c249135052e930cbd6c4a66daa32249ba00d1c8def75857fa3f3431d'
	operation_name = 'MessageBufferChatHistory'
	def build_query(self, variables: Union[MessageBufferChatHistoryRequest1, MessageBufferChatHistoryRequest2] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class NielsenContentMetadata(Endpoint):
	sha256Hash = '2dbf505ee929438369e68e72319d1106bb3c142e295332fac157c90638968586'
	operation_name = 'NielsenContentMetadata'
	def build_query(self, variables: NielsenContentMetadataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OneClickEligibility(Endpoint):
	sha256Hash = 'ab0d03b2c38e3a570ca5f8fb4d0884bc7764c6f25a05345dc2014c611fa02de9'
	operation_name = 'OneClickEligibility'
	def build_query(self, variables: OneClickEligibilityRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OneTapFeed(Endpoint):
	sha256Hash = '287ce6226da1b78e05e5024b99a3e3190a3e57e1bd1a95ae16d0eef33edc1547'
	operation_name = 'OneTapFeed'
	def build_query(self, variables: OneTapFeedRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OnsiteNotifications_Summary(Endpoint):
	sha256Hash = '4d07584aeb25d8fec753ea232935ab2c18ec2b85e80a6e4a5ef89d46cf9193b1'
	operation_name = 'OnsiteNotifications_Summary'
	def build_query(self, variables: OnsiteNotifications_SummaryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PaidPinnedChat(Endpoint):
	sha256Hash = '888056ddc92e62a7d2fd7a8e0afae5d61fab767ba621ed1006ba8628f6de8e41'
	operation_name = 'PaidPinnedChat'
	def build_query(self, variables: PaidPinnedChatRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PbyPGame(Endpoint):
	sha256Hash = 'f7444c6e187868a7b82e7659e59bb8ccd177cb4deca277e3a951fb2ef66c2389'
	operation_name = 'PbyPGame'
	def build_query(self, variables: PbyPGameRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PersistentGoalFollowButton_User(Endpoint):
	sha256Hash = '88f5b0d6e9d13d6751b07b5e9cc175e3f7f6f7cedb07b033e1b548ba2323f015'
	operation_name = 'PersistentGoalFollowButton_User'
	def build_query(self, variables: PersistentGoalFollowButton_UserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PinnedChatSettings(Endpoint):
	sha256Hash = 'ff555546ff83a3034dee18a6d764123717b6f68553e082dea6b77a66b7b2672e'
	operation_name = 'PinnedChatSettings'
	def build_query(self, variables: PinnedChatSettingsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PinnedCheersSettings(Endpoint):
	sha256Hash = 'ca73cb0396fe5bcbe05c906fd472622e4b873eeb07699c2664026a079aeec631'
	operation_name = 'PinnedCheersSettings'
	def build_query(self, variables: PinnedCheersSettingsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PlaybackAccessToken(Endpoint):
	sha256Hash = 'ed230aa1e33e07eebb8928504583da78a5173989fadfb1ac94be06a04f3cdbe9'
	operation_name = 'PlaybackAccessToken'
	def build_query(self, variables: PlaybackAccessTokenRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PrefetchPlaybackAccessToken(Endpoint):
	sha256Hash = 'c101f277c6ab7de34f64e63c90d698edae0d83ed5fad8efe198596b472ef3337'
	operation_name = 'PrefetchPlaybackAccessToken'
	def build_query(self, variables: PrefetchPlaybackAccessTokenRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class queryUserViewedVideo(Endpoint):
	sha256Hash = 'e249447c070b095eb599cceec239bbca567e30080795789f85bc25db3f7a27ad'
	operation_name = 'queryUserViewedVideo'
	def build_query(self, variables: queryUserViewedVideoRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RealtimeStreamTagList(Endpoint):
	sha256Hash = 'a4747cac9d8e8bf6cf80969f6da6363ca1bdbd80fe136797e71504eb404313fd'
	operation_name = 'RealtimeStreamTagList'
	def build_query(self, variables: RealtimeStreamTagListRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RecapEligibilityQuery(Endpoint):
	sha256Hash = 'caf047b3d39c4ab74d0ae590e4a24530f531e1a33945058a4526d75cd86eb3fc'
	operation_name = 'RecapEligibilityQuery'
	def build_query(self, variables: RecapEligibilityQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ReportMenuItem(Endpoint):
	sha256Hash = '784bde9b3aa7638b3d2a99da0b1e1cf2ade81a8a7423410bd165e5d860913195'
	operation_name = 'ReportMenuItem'
	def build_query(self, variables: ReportMenuItemRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RoleRestricted(Endpoint):
	sha256Hash = '7f57264e30ae6d9daa154bb62c8b0bcb1b38fc0b53a7b3cdecd60a060ff8332b'
	operation_name = 'RoleRestricted'
	def build_query(self, variables: RoleRestrictedRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SearchResultsPage_SearchResults(Endpoint):
	sha256Hash = 'f6c2575aee4418e8a616e03364d8bcdbf0b10a5c87b59f523569dacc963e8da5'
	operation_name = 'SearchResultsPage_SearchResults'
	def build_query(self, variables: SearchResultsPage_SearchResultsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ShareClipRenderStatus(Endpoint):
	sha256Hash = 'f130048a462a0ac86bb54d653c968c514e9ab9ca94db52368c1179e97b0f16eb'
	operation_name = 'ShareClipRenderStatus'
	def build_query(self, variables: ShareClipRenderStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SharedChatModeratorStrikes(Endpoint):
	sha256Hash = '846b72652391105f0cd30ff586c807dfb4d4815f768ec13462d7b4d2e0d75d52'
	operation_name = 'SharedChatModeratorStrikes'
	def build_query(self, variables: SharedChatModeratorStrikesRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SharedChatSession(Endpoint):
	sha256Hash = '0ff9562b30cfa2b41ab1738485ced6f8f1e725a93abe732c396be5f4f1d13694'
	operation_name = 'SharedChatSession'
	def build_query(self, variables: SharedChatSessionRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Shelves(Endpoint):
	sha256Hash = 'c04cbfe9d604367b6ea4ea3fe4c9695046561ef44c9af2af3e0e3c0c20f563b1'
	operation_name = 'Shelves'
	def build_query(self, variables: Union[ShelvesRequest1, ShelvesRequest2, ShelvesRequest3, ShelvesRequest4] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ShoutoutHighlightServiceQuery(Endpoint):
	sha256Hash = 'da377690d61c9f2923af148efb8b79b29674e4195c0230a4037a567ce8d40825'
	operation_name = 'ShoutoutHighlightServiceQuery'
	def build_query(self, variables: ShoutoutHighlightServiceQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StoryChannelQuery(Endpoint):
	sha256Hash = 'efa575524a7a86bf6172801278301584a366e59a8049c667fd4abea01522b8a2'
	operation_name = 'StoryChannelQuery'
	def build_query(self, variables: StoryChannelQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamChat(Endpoint):
	sha256Hash = 'fed5f3ae0f569dc9d6faf768475456715b853ef737873ed5cb2bb45b3e28e67f'
	operation_name = 'StreamChat'
	def build_query(self, variables: StreamChatRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamMetadata(Endpoint):
	sha256Hash = 'b57f9b910f8cd1a4659d894fe7550ccc81ec9052c01e438b290fd66a040b9b93'
	operation_name = 'StreamMetadata'
	def build_query(self, variables: StreamMetadataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamRefetchManager(Endpoint):
	sha256Hash = 'ecdcb724b0559d49689e6a32795e6a43bba4b2071b5e762a4d1edf2bb42a6789'
	operation_name = 'StreamRefetchManager'
	def build_query(self, variables: StreamRefetchManagerRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamSchedule(Endpoint):
	sha256Hash = '83552f5614707fd3e897495c18875b6fa9c83d8cf11e73b9f158f3173b4f3b75'
	operation_name = 'StreamSchedule'
	def build_query(self, variables: StreamScheduleRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SubscribedContext(Endpoint):
	sha256Hash = '56f8d2d143e1045284432c96830b3fdb811876efb03f9b5c8504a0cee4fd1bbb'
	operation_name = 'SubscribedContext'
	def build_query(self, variables: SubscribedContextRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsChatPauseSetting(Endpoint):
	sha256Hash = '922f2a23e49da4ce2660f7fbfeefeefab19f7651196f9b54f03555590f173627'
	operation_name = 'SyncedSettingsChatPauseSetting'
	def build_query(self, variables: SyncedSettingsChatPauseSettingRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsDeletedMessageDisplaySetting(Endpoint):
	sha256Hash = '79fbdf86e8ee5fa4ca27cad96c292702eed8a8cc14faedc874a577f6e8fe4004'
	operation_name = 'SyncedSettingsDeletedMessageDisplaySetting'
	def build_query(self, variables: SyncedSettingsDeletedMessageDisplaySettingRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsEmoteAnimations(Endpoint):
	sha256Hash = '64ac5d385b316fd889f8c46942a7c7463a1429452ef20ffc5d0cd23fcc4ecf30'
	operation_name = 'SyncedSettingsEmoteAnimations'
	def build_query(self, variables: SyncedSettingsEmoteAnimationsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsReadableChatColors(Endpoint):
	sha256Hash = 'cd9c43ab3cb4c04515a879bbd618055aab18c6ac4081ed9de333945ca91247ba'
	operation_name = 'SyncedSettingsReadableChatColors'
	def build_query(self, variables: SyncedSettingsReadableChatColorsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class TitleMentions(Endpoint):
	sha256Hash = '79439ae721a6f24f9d761ceae3a5c91097929fc59f5072a3b505e675bb3d432f'
	operation_name = 'TitleMentions'
	def build_query(self, variables: TitleMentionsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UpdateConsentMutation(Endpoint):
	sha256Hash = '292c17ca8ca80f9362d16e3f0a936be6c329f98dcd1f858b604b256c4adf42d5'
	operation_name = 'UpdateConsentMutation'
	def build_query(self, variables: UpdateConsentMutationRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class updateUserViewedVideo(Endpoint):
	sha256Hash = 'bb58b1bd08a4ca0c61f2b8d323381a5f4cd39d763da8698f680ef1dfaea89ca1'
	operation_name = 'updateUserViewedVideo'
	def build_query(self, variables: updateUserViewedVideoRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UseLive(Endpoint):
	sha256Hash = '639d5f11bfb8bf3053b424d9ef650d04c4ebb7d94711d644afb08fe9a0fad5d9'
	operation_name = 'UseLive'
	def build_query(self, variables: UseLiveRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UseLiveBroadcast(Endpoint):
	sha256Hash = '0b47cc6d8c182acd2e78b81c8ba5414a5a38057f2089b1bbcfa6046aae248bd2'
	operation_name = 'UseLiveBroadcast'
	def build_query(self, variables: UseLiveBroadcastRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UserMenuCurrentUser(Endpoint):
	sha256Hash = '3cff634f43c5c78830907a662b315b1847cfc0dce32e6a9752e7f5d70b37f8c0'
	operation_name = 'UserMenuCurrentUser'
	def build_query(self, variables: UserMenuCurrentUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UserModStatus(Endpoint):
	sha256Hash = '511b58faf547070bc95b7d32e7b5cdedf8c289a3aeabfc3c5d3ece2de01ae06f'
	operation_name = 'UserModStatus'
	def build_query(self, variables: UserModStatusRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UseViewCount(Endpoint):
	sha256Hash = '95e6bd7acfbb2f220c17e387805141b77b43b18e5b27b4f702713e9ddbe6b907'
	operation_name = 'UseViewCount'
	def build_query(self, variables: UseViewCountRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VerifyEmail_CurrentUser(Endpoint):
	sha256Hash = 'f9e7dcdf7e99c314c82d8f7f725fab5f99d1df3d7359b53c9ae122deec590198'
	operation_name = 'VerifyEmail_CurrentUser'
	def build_query(self, variables: VerifyEmail_CurrentUserRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoAccessToken_Clip(Endpoint):
	sha256Hash = '6fd3af2b22989506269b9ac02dd87eb4a6688392d67d94e41a6886f1e9f5c00f'
	operation_name = 'VideoAccessToken_Clip'
	def build_query(self, variables: VideoAccessToken_ClipRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoComments(Endpoint):
	sha256Hash = 'be06407e8d7cda72f2ee086ebb11abb6b062a7deb8985738e648090904d2f0eb'
	operation_name = 'VideoComments'
	def build_query(self, variables: VideoCommentsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoCommentsByOffsetOrCursor(Endpoint):
	sha256Hash = 'b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a'
	operation_name = 'VideoCommentsByOffsetOrCursor'
	def build_query(self, variables: Union[VideoCommentsByOffsetOrCursorRequest1, VideoCommentsByOffsetOrCursorRequest2] = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoMarkersChatCommand(Endpoint):
	sha256Hash = 'c65f8b33e3bcccf2b16057e8f445311d213ecf8729f842ccdc71908231fa9a78'
	operation_name = 'VideoMarkersChatCommand'
	def build_query(self, variables: VideoMarkersChatCommandRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoMetadata(Endpoint):
	sha256Hash = '45111672eea2e507f8ba44d101a61862f9c56b11dee09a15634cb75cb9b9084d'
	operation_name = 'VideoMetadata'
	def build_query(self, variables: VideoMetadataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_AgeGateOverlayBroadcaster(Endpoint):
	sha256Hash = 'ab175a77fb908cd5dfe25d6d23da0765b3fc187e3d3461d1c7b157c354e917ee'
	operation_name = 'VideoPlayer_AgeGateOverlayBroadcaster'
	def build_query(self, variables: VideoPlayer_AgeGateOverlayBroadcasterRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_ChapterSelectButtonVideo(Endpoint):
	sha256Hash = '71835d5ef425e154bf282453a926d99b328cdc5e32f36d3a209d0f4778b41203'
	operation_name = 'VideoPlayer_ChapterSelectButtonVideo'
	def build_query(self, variables: VideoPlayer_ChapterSelectButtonVideoRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_MutedSegmentsAlertOverlay(Endpoint):
	sha256Hash = 'c36e7400657815f4704e6063d265dff766ed8fc1590361c6d71e4368805e0b49'
	operation_name = 'VideoPlayer_MutedSegmentsAlertOverlay'
	def build_query(self, variables: VideoPlayer_MutedSegmentsAlertOverlayRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_VideoSourceManager(Endpoint):
	sha256Hash = 'f5e1b35d6f5a40348c6476fea36945d0931ba50621e1701b6c31252ee498cc3e'
	operation_name = 'VideoPlayer_VideoSourceManager'
	def build_query(self, variables: VideoPlayer_VideoSourceManagerRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_VODSeekbar(Endpoint):
	sha256Hash = 'c67d32eba8f1c93b02e7efa6a278be46009e390ed5195c02dd0621e4c7ca14ac'
	operation_name = 'VideoPlayer_VODSeekbar'
	def build_query(self, variables: VideoPlayer_VODSeekbarRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_VODSeekbarPreviewVideo(Endpoint):
	sha256Hash = '07e99e4d56c5a7c67117a154777b0baf85a5ffefa393b213f4bc712ccaf85dd6'
	operation_name = 'VideoPlayer_VODSeekbarPreviewVideo'
	def build_query(self, variables: VideoPlayer_VODSeekbarPreviewVideoRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerClipPostplayRecommendationsOverlay(Endpoint):
	sha256Hash = '4261232b81ad1b4dde3bbf8ada53b8c236bf035fcd18842ec327f631ba4a3870'
	operation_name = 'VideoPlayerClipPostplayRecommendationsOverlay'
	def build_query(self, variables: VideoPlayerClipPostplayRecommendationsOverlayRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerClipsButtonBroadcaster(Endpoint):
	sha256Hash = '784065d408671ee105d64241cc6f461b1c32684d837734fa2f4c761229a7efcd'
	operation_name = 'VideoPlayerClipsButtonBroadcaster'
	def build_query(self, variables: VideoPlayerClipsButtonBroadcasterRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerOfflineRecommendationsOverlay(Endpoint):
	sha256Hash = '73794e55fa4149d5a17b31105f74e625f291ca68a4c034076053be0f647ba5ee'
	operation_name = 'VideoPlayerOfflineRecommendationsOverlay'
	def build_query(self, variables: VideoPlayerOfflineRecommendationsOverlayRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerStatusOverlayChannel(Endpoint):
	sha256Hash = '938d155c890df88b5da53592e327d36ae9b851d2ee38bdb13342a1402fc24ad2'
	operation_name = 'VideoPlayerStatusOverlayChannel'
	def build_query(self, variables: VideoPlayerStatusOverlayChannelRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerStreamMetadata(Endpoint):
	sha256Hash = '248fee6868e983c4e7b69074e888960f77735bd21a1d4a1d882b55f45d30a420'
	operation_name = 'VideoPlayerStreamMetadata'
	def build_query(self, variables: VideoPlayerStreamMetadataRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerVODPostplayRecommendations(Endpoint):
	sha256Hash = '2e29be981ae55ea4cf78cda648afa156928508c3cb03c6ca5c1726fdef1183d8'
	operation_name = 'VideoPlayerVODPostplayRecommendations'
	def build_query(self, variables: VideoPlayerVODPostplayRecommendationsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPreviewCard__VideoMoments(Endpoint):
	sha256Hash = '7399051b2d46f528d5f0eedf8b0db8d485bb1bb4c0a2c6707be6f1290cdcb31a'
	operation_name = 'VideoPreviewCard__VideoMoments'
	def build_query(self, variables: VideoPreviewCard__VideoMomentsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPreviewOverlay(Endpoint):
	sha256Hash = '9515480dee68a77e667cb19de634739d33f243572b007e98e67184b1a5d8369f'
	operation_name = 'VideoPreviewOverlay'
	def build_query(self, variables: VideoPreviewOverlayRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VODMidrollManager(Endpoint):
	sha256Hash = 'dcfb8c8cd3b721da5720fda11b9a20a3ab94be85ec04e8c2ac48ff69f300e959'
	operation_name = 'VODMidrollManager'
	def build_query(self, variables: VODMidrollManagerRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class WatchStreakExperiment(Endpoint):
	sha256Hash = 'ec1ad3e0e7a2c3c3c762652f7a42b12da8b4db074fe99f0d29b2febd330465db'
	operation_name = 'WatchStreakExperiment'
	def build_query(self, variables: WatchStreakExperimentRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Whispers_Whispers_UserWhisperThreads(Endpoint):
	sha256Hash = '9d4bf15288a0b4d96492c97dafa17222aa000528adcad4f8d1652441d9132d62'
	operation_name = 'Whispers_Whispers_UserWhisperThreads'
	def build_query(self, variables: Whispers_Whispers_UserWhisperThreadsRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class WithIsStreamLiveQuery(Endpoint):
	sha256Hash = '04e46329a6786ff3a81c01c50bfa5d725902507a0deb83b0edbf7abe7a3716ea'
	operation_name = 'WithIsStreamLiveQuery'
	def build_query(self, variables: WithIsStreamLiveQueryRequest = {}) -> Dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft


class videoPlaybackAccessToken(Endpoint):
	def __init__(self):
		self.draft = '''{{"query": "{{\\n              videoPlaybackAccessToken(\\n                id: \\"{}\\",\\n                params: {{\\n                  platform: \\"web\\",\\n                  playerBackend: \\"mediaplayer\\",\\n                  playerType: \\"site\\"\\n                }}\\n              )\\n              {{\\n                value\\n                signature\\n              }}\\n            }}"}}'''

	def build_query(self, vod_id: str):
		return self.draft.format(vod_id)

class Endpoints:
	"""Placeholder for all endpoints in current module"""
	amount = 161
	AccessGetFeatureClipRestrictionsQuery = AccessGetFeatureClipRestrictionsQuery()
	AcknowledgeUnbanRequestPrompt = AcknowledgeUnbanRequestPrompt()
	AvailableEmotesForChannelPaginated = AvailableEmotesForChannelPaginated()
	BlockedUsers = BlockedUsers()
	BrowsePage_AllDirectories = BrowsePage_AllDirectories()
	BrowseVerticalDirectory = BrowseVerticalDirectory()
	CanCreateClip = CanCreateClip()
	CanViewersExportQuery = CanViewersExportQuery()
	ChannelAvatar = ChannelAvatar()
	ChannelClipCore = ChannelClipCore()
	ChannelCollaborationEligibilityQuery = ChannelCollaborationEligibilityQuery()
	ChannelLeaderboards = ChannelLeaderboards()
	ChannelPage_SetSessionStatus = ChannelPage_SetSessionStatus()
	ChannelPage_SubscribeButton_User = ChannelPage_SubscribeButton_User()
	ChannelPointsContext = ChannelPointsContext()
	ChannelPointsGlobalContext = ChannelPointsGlobalContext()
	ChannelPointsPredictionContext = ChannelPointsPredictionContext()
	ChannelShell = ChannelShell()
	ChannelSkins = ChannelSkins()
	ChannelSocialButtons = ChannelSocialButtons()
	ChannelSupportButtons = ChannelSupportButtons()
	ChannelVideoCore = ChannelVideoCore()
	ChannelVideoShelvesQuery = ChannelVideoShelvesQuery()
	Chat_ChannelData = Chat_ChannelData()
	Chat_EarnedBadges_InitialSubStatus = Chat_EarnedBadges_InitialSubStatus()
	Chat_OrbisPresetText = Chat_OrbisPresetText()
	Chat_ShareResub_ChannelData = Chat_ShareResub_ChannelData()
	Chat_UserData = Chat_UserData()
	ChatClip = ChatClip()
	ChatFilterContextManager_User = ChatFilterContextManager_User()
	ChatInput = ChatInput()
	ChatInput_Badges = ChatInput_Badges()
	ChatList_Badges = ChatList_Badges()
	ChatModeratorStrikeStatus = ChatModeratorStrikeStatus()
	ChatRestrictions = ChatRestrictions()
	ChatRoomBanStatus = ChatRoomBanStatus()
	ChatRoomState = ChatRoomState()
	ChatScreenReaderAutoAnnounce = ChatScreenReaderAutoAnnounce()
	ClaimCommunityPoints = ClaimCommunityPoints()
	ClipMetadata = ClipMetadata()
	ClipsCards__User = ClipsCards__User()
	ClipsExperimentEnrollmentStatus = ClipsExperimentEnrollmentStatus()
	CollectionCarouselQuery = CollectionCarouselQuery()
	CommercialCommandHandler_ChannelData = CommercialCommandHandler_ChannelData()
	CommonHooks_BlockedUsers = CommonHooks_BlockedUsers()
	CommunityOnboardingAllowlist = CommunityOnboardingAllowlist()
	CommunityPointsAvailableClaim = CommunityPointsAvailableClaim()
	CommunityPointsChatPrivateCalloutUser = CommunityPointsChatPrivateCalloutUser()
	CommunitySupportSettings = CommunitySupportSettings()
	Consent = Consent()
	ContentClassificationContext = ContentClassificationContext()
	ContentPolicyPropertiesQuery = ContentPolicyPropertiesQuery()
	CoreActionsCurrentUser = CoreActionsCurrentUser()
	CurrentUserBannedStatus = CurrentUserBannedStatus()
	CurrentUserModeratorStatus = CurrentUserModeratorStatus()
	CurrentUserStrikeStatus = CurrentUserStrikeStatus()
	DirectoryCollection_BrowsableCollection = DirectoryCollection_BrowsableCollection()
	DropCurrentSessionContext = DropCurrentSessionContext()
	DropsHighlightService_AvailableDrops = DropsHighlightService_AvailableDrops()
	EmotesForChannelFollowStatus = EmotesForChannelFollowStatus()
	FeaturedClipsShelfCover = FeaturedClipsShelfCover()
	FeaturedContentCarouselStreams = FeaturedContentCarouselStreams()
	FilterableVideoTower_Videos = FilterableVideoTower_Videos()
	FollowButton_FollowUser = FollowButton_FollowUser()
	FollowButton_UnfollowUser = FollowButton_UnfollowUser()
	FollowButton_User = FollowButton_User()
	FollowedIndex_CurrentUser = FollowedIndex_CurrentUser()
	FollowedIndex_FollowCount = FollowedIndex_FollowCount()
	FollowedStreams = FollowedStreams()
	FollowedStreamsContinueWatching = FollowedStreamsContinueWatching()
	FollowedVideos_CurrentUser = FollowedVideos_CurrentUser()
	FollowingGames_CurrentUser = FollowingGames_CurrentUser()
	FollowingLive_CurrentUser = FollowingLive_CurrentUser()
	FollowingPage_RecommendedChannels = FollowingPage_RecommendedChannels()
	FrontPageNew_User = FrontPageNew_User()
	GetDisplayName = GetDisplayName()
	GetGuestSessionBlocksAndBans = GetGuestSessionBlocksAndBans()
	GetIDFromLogin = GetIDFromLogin()
	GetPinnedChat = GetPinnedChat()
	GetUserID = GetUserID()
	GlobalBadges = GlobalBadges()
	GuestListQuery = GuestListQuery()
	GuestStarActiveJoinRequest = GuestStarActiveJoinRequest()
	GuestStarBatchCollaborationQuery = GuestStarBatchCollaborationQuery()
	GuestStarChannelPageCollaborationQuery = GuestStarChannelPageCollaborationQuery()
	HappeningNowSettings = HappeningNowSettings()
	HomeOfflineCarousel = HomeOfflineCarousel()
	HomeShelfEditor = HomeShelfEditor()
	HomeShelfGames = HomeShelfGames()
	HomeShelfUsers = HomeShelfUsers()
	HomeShelfVideos = HomeShelfVideos()
	incrementClipViewCount = incrementClipViewCount()
	LastUnbanRequest = LastUnbanRequest()
	LowerHomeHeader = LowerHomeHeader()
	MessageBuffer_Channel = MessageBuffer_Channel()
	MessageBufferChatHistory = MessageBufferChatHistory()
	NielsenContentMetadata = NielsenContentMetadata()
	OneClickEligibility = OneClickEligibility()
	OneTapFeed = OneTapFeed()
	OnsiteNotifications_Summary = OnsiteNotifications_Summary()
	PaidPinnedChat = PaidPinnedChat()
	PbyPGame = PbyPGame()
	PersistentGoalFollowButton_User = PersistentGoalFollowButton_User()
	PinnedChatSettings = PinnedChatSettings()
	PinnedCheersSettings = PinnedCheersSettings()
	PlaybackAccessToken = PlaybackAccessToken()
	PrefetchPlaybackAccessToken = PrefetchPlaybackAccessToken()
	queryUserViewedVideo = queryUserViewedVideo()
	RealtimeStreamTagList = RealtimeStreamTagList()
	RecapEligibilityQuery = RecapEligibilityQuery()
	ReportMenuItem = ReportMenuItem()
	RoleRestricted = RoleRestricted()
	SearchResultsPage_SearchResults = SearchResultsPage_SearchResults()
	ShareClipRenderStatus = ShareClipRenderStatus()
	SharedChatModeratorStrikes = SharedChatModeratorStrikes()
	SharedChatSession = SharedChatSession()
	Shelves = Shelves()
	ShoutoutHighlightServiceQuery = ShoutoutHighlightServiceQuery()
	StoryChannelQuery = StoryChannelQuery()
	StreamChat = StreamChat()
	StreamMetadata = StreamMetadata()
	StreamRefetchManager = StreamRefetchManager()
	StreamSchedule = StreamSchedule()
	SubscribedContext = SubscribedContext()
	SyncedSettingsChatPauseSetting = SyncedSettingsChatPauseSetting()
	SyncedSettingsDeletedMessageDisplaySetting = SyncedSettingsDeletedMessageDisplaySetting()
	SyncedSettingsEmoteAnimations = SyncedSettingsEmoteAnimations()
	SyncedSettingsReadableChatColors = SyncedSettingsReadableChatColors()
	TitleMentions = TitleMentions()
	UpdateConsentMutation = UpdateConsentMutation()
	updateUserViewedVideo = updateUserViewedVideo()
	UseLive = UseLive()
	UseLiveBroadcast = UseLiveBroadcast()
	UserMenuCurrentUser = UserMenuCurrentUser()
	UserModStatus = UserModStatus()
	UseViewCount = UseViewCount()
	VerifyEmail_CurrentUser = VerifyEmail_CurrentUser()
	VideoAccessToken_Clip = VideoAccessToken_Clip()
	VideoComments = VideoComments()
	VideoCommentsByOffsetOrCursor = VideoCommentsByOffsetOrCursor()
	VideoMarkersChatCommand = VideoMarkersChatCommand()
	VideoMetadata = VideoMetadata()
	VideoPlayer_AgeGateOverlayBroadcaster = VideoPlayer_AgeGateOverlayBroadcaster()
	VideoPlayer_ChapterSelectButtonVideo = VideoPlayer_ChapterSelectButtonVideo()
	VideoPlayer_MutedSegmentsAlertOverlay = VideoPlayer_MutedSegmentsAlertOverlay()
	VideoPlayer_VideoSourceManager = VideoPlayer_VideoSourceManager()
	VideoPlayer_VODSeekbar = VideoPlayer_VODSeekbar()
	VideoPlayer_VODSeekbarPreviewVideo = VideoPlayer_VODSeekbarPreviewVideo()
	VideoPlayerClipPostplayRecommendationsOverlay = VideoPlayerClipPostplayRecommendationsOverlay()
	VideoPlayerClipsButtonBroadcaster = VideoPlayerClipsButtonBroadcaster()
	VideoPlayerOfflineRecommendationsOverlay = VideoPlayerOfflineRecommendationsOverlay()
	VideoPlayerStatusOverlayChannel = VideoPlayerStatusOverlayChannel()
	VideoPlayerStreamMetadata = VideoPlayerStreamMetadata()
	VideoPlayerVODPostplayRecommendations = VideoPlayerVODPostplayRecommendations()
	VideoPreviewCard__VideoMoments = VideoPreviewCard__VideoMoments()
	VideoPreviewOverlay = VideoPreviewOverlay()
	VODMidrollManager = VODMidrollManager()
	WatchStreakExperiment = WatchStreakExperiment()
	Whispers_Whispers_UserWhisperThreads = Whispers_Whispers_UserWhisperThreads()
	WithIsStreamLiveQuery = WithIsStreamLiveQuery()
	videoPlaybackAccessToken = videoPlaybackAccessToken()
	...
