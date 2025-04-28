from typing import Dict, TypedDict, List, Any, Union, TypeVar, Generic
from types import NoneType
from sptz import Falsy


__all__ = [
	"Endpoint",
	"Endpoints",

	"AccessGetFeatureClipRestrictionsQueryRequest",
	"AccessGetFeatureClipRestrictionsQueryResponse",
	"AcknowledgeUnbanRequestPromptRequest",
	"AcknowledgeUnbanRequestPromptResponse",
	"ActiveGoalsRequest",
	"ActiveGoalsResponse",
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
	"ChannelPollContext_GetViewablePollRequest",
	"ChannelPollContext_GetViewablePollResponse",
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
	"ChannelVideosContent_GameRequest",
	"ChannelVideosContent_GameResponse",
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
	"DirectoryPage_GameRequest1",
	"DirectoryPage_GameRequest2",
	"DirectoryPage_GameResponse",
	"DirectoryRoot_DirectoryRequest",
	"DirectoryRoot_DirectoryResponse",
	"DirectoryVideos_GameRequest1",
	"DirectoryVideos_GameRequest2",
	"DirectoryVideos_GameResponse",
	"DiscoveryPreferenceMutationRequest",
	"DiscoveryPreferenceMutationResponse",
	"DiscoveryPreferenceQueryRequest",
	"DiscoveryPreferenceQueryResponse",
	"DropCurrentSessionContextRequest",
	"DropCurrentSessionContextResponse",
	"DropsHighlightService_AvailableDropsRequest",
	"DropsHighlightService_AvailableDropsResponse",
	"EmotesForChannelFollowStatusRequest",
	"EmotesForChannelFollowStatusResponse",
	"FeaturedContentCarouselStreamsRequest",
	"FeaturedContentCarouselStreamsResponse",
	"FilterableVideoTower_VideosRequest1",
	"FilterableVideoTower_VideosRequest2",
	"FilterableVideoTower_VideosRequest3",
	"FilterableVideoTower_VideosResponse",
	"FollowButton_FollowUserRequest",
	"FollowButton_FollowUserResponse",
	"FollowButton_UnfollowUserRequest",
	"FollowButton_UnfollowUserResponse",
	"FollowButton_UserRequest",
	"FollowButton_UserResponse",
	"FollowGameButton_GameRequest",
	"FollowGameButton_GameResponse",
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
	"GetHypeTrainExecutionV2Request",
	"GetHypeTrainExecutionV2Response",
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
	"PaidPinnedChatRequest",
	"PaidPinnedChatResponse",
	"PbyPGameRequest",
	"PbyPGameResponse",
	"PersistentGoalFollowButton_UserRequest",
	"PersistentGoalFollowButton_UserResponse",
	"PersonalSectionsHypeTrainsRequest",
	"PersonalSectionsHypeTrainsResponse",
	"PinnedChatSettingsRequest",
	"PinnedChatSettingsResponse",
	"PinnedCheersSettingsRequest",
	"PinnedCheersSettingsResponse",
	"PlaybackAccessTokenRequest",
	"PlaybackAccessTokenResponse1",
	"PlaybackAccessTokenResponse2",
	"PollChannelSettingsRequest",
	"PollChannelSettingsResponse",
	"PrefetchPlaybackAccessTokenRequest",
	"PrefetchPlaybackAccessTokenResponse",
	"ProfileImageSettingRequest",
	"ProfileImageSettingResponse",
	"RealtimeStreamTagListRequest",
	"RealtimeStreamTagListResponse",
	"RecapEligibilityQueryRequest",
	"RecapEligibilityQueryResponse",
	"RoleRestrictedRequest",
	"RoleRestrictedResponse",
	"Settings_ProfilePage_AccountInfoSettingsRequest",
	"Settings_ProfilePage_AccountInfoSettingsResponse",
	"ShareClipRenderStatusRequest",
	"ShareClipRenderStatusResponse",
	"SharedChatModeratorStrikesRequest",
	"SharedChatModeratorStrikesResponse",
	"SharedChatSessionRequest",
	"SharedChatSessionResponse",
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
	"UseLiveBroadcastRequest",
	"UseLiveBroadcastResponse",
	"UseLiveRequest",
	"UseLiveResponse",
	"UseViewCountRequest",
	"UseViewCountResponse",
	"UserEmoticonPrefix_QueryRequest",
	"UserEmoticonPrefix_QueryResponse",
	"UserModStatusRequest",
	"UserModStatusResponse",
	"UsernameRenameStatusRequest",
	"UsernameRenameStatusResponse",
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
	"ViewerCardRequest",
	"ViewerCardResponse",
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


T = TypeVar('T')
class Endpoint(Generic[T]):

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

	def build_query(self, variables: T = {}) -> Dict:
		"""Build query for the endpoint."""
		draft = self.draft.copy()
		draft['variables'] = variables
		return draft

class AccessGetFeatureClipRestrictionsQueryRequest(TypedDict):
	channelLogin: str

class AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsDataFeaturingrestrictedtoData(TypedDict):
	shouldAllowMods: bool

class AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsData(TypedDict):
	featuringRestrictedTo: Union[NoneType, AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsDataFeaturingrestrictedtoData]

class AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelData(TypedDict):
	id: str
	clipsSettings: AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsData

class AccessGetFeatureClipRestrictionsQueryResponseUserData(TypedDict):
	id: str
	channel: AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelData

class AccessGetFeatureClipRestrictionsQueryResponse(TypedDict):
	user: AccessGetFeatureClipRestrictionsQueryResponseUserData

class AcknowledgeUnbanRequestPromptRequest(TypedDict):
	channelLogin: str

class AcknowledgeUnbanRequestPromptResponseChannelData(TypedDict):
	id: str
	profileImageURL: str

class AcknowledgeUnbanRequestPromptResponse(TypedDict):
	channel: AcknowledgeUnbanRequestPromptResponseChannelData

class ActiveGoalsRequest(TypedDict):
	channelLogin: str

class ActiveGoalsResponseChannelDataGoalsDataEdgesDataNodeDataCustomizationsData(TypedDict):
	progressBarAccentColor: Union[str, NoneType]
	progressBarBackgroundColor: Union[str, NoneType]

class ActiveGoalsResponseChannelDataGoalsDataEdgesDataNodeData(TypedDict):
	id: str
	contributionType: str
	state: str
	currentContributions: int
	targetContributions: int
	description: Union[str, NoneType]
	createdAt: str
	customizations: ActiveGoalsResponseChannelDataGoalsDataEdgesDataNodeDataCustomizationsData
	shouldAutoIncrement: Union[NoneType, bool]

class ActiveGoalsResponseChannelDataGoalsDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: ActiveGoalsResponseChannelDataGoalsDataEdgesDataNodeData

class ActiveGoalsResponseChannelDataGoalsDataPageinfoData(TypedDict):
	hasNextPage: bool

class ActiveGoalsResponseChannelDataGoalsData(TypedDict):
	edges: Falsy[List[ActiveGoalsResponseChannelDataGoalsDataEdgesData]]
	pageInfo: ActiveGoalsResponseChannelDataGoalsDataPageinfoData

class ActiveGoalsResponseChannelData(TypedDict):
	id: str
	goals: ActiveGoalsResponseChannelDataGoalsData

class ActiveGoalsResponse(TypedDict):
	channel: ActiveGoalsResponseChannelData

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

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeData(TypedDict):
	id: str
	emotes: List[AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeDataEmotesData]
	owner: Union[NoneType, AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeDataOwnerData]

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesDataNodeData

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataPageinfoData(TypedDict):
	hasNextPage: bool

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedData(TypedDict):
	edges: List[AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesData]
	pageInfo: AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataPageinfoData

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfData(TypedDict):
	availableEmoteSetsPaginated: Union[NoneType, AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedData]

class AvailableEmotesForChannelPaginatedResponseChannelData(TypedDict):
	id: str
	self: AvailableEmotesForChannelPaginatedResponseChannelDataSelfData

class AvailableEmotesForChannelPaginatedResponse(TypedDict):
	channel: AvailableEmotesForChannelPaginatedResponseChannelData

class BlockedUsersRequest(TypedDict):
	...

class BlockedUsersResponseCurrentuserData(TypedDict):
	id: str
	blockedUsers: Falsy[List[Any]]

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

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesDataNodeData(TypedDict):
	id: str
	slug: str
	displayName: str
	name: str
	avatarURL: str
	viewersCount: int
	tags: Falsy[List[BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesDataNodeDataTagsData]]
	originalReleaseDate: Union[str, NoneType]

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesData(TypedDict):
	cursor: str
	trackingID: str
	node: BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesDataNodeData

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataPageinfoData(TypedDict):
	hasNextPage: bool

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsData(TypedDict):
	edges: List[BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesData]
	pageInfo: BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataPageinfoData

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

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensDataNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensData]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensDataNodeData(TypedDict):
	text: str
	hasEmphasis: bool
	location: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensDataNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensData]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1GametagsData(TypedDict):
	id: str
	isLanguageTag: bool
	localizedName: str
	tagName: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1(TypedDict):
	id: str
	slug: str
	name: str
	viewersCount: int
	displayName: str
	boxArtURL: str
	gameTags: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1GametagsData]
	originalReleaseDate: Union[NoneType, str]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataBroadcastsettingsData(TypedDict):
	id: str
	title: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterData(TypedDict):
	id: str
	broadcastSettings: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataBroadcastsettingsData
	profileImageURL: str
	displayName: str
	login: str
	primaryColorHex: Union[NoneType, str]
	roles: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterDataRolesData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2GameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2FreeformtagsData(TypedDict):
	id: str
	name: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2PreviewthumbnailpropertiesData(TypedDict):
	blurReason: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2(TypedDict):
	id: str
	broadcaster: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2BroadcasterData
	game: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2GameData
	freeformTags: Falsy[List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2FreeformtagsData]]
	viewersCount: Falsy[int]
	previewImageURL: str
	createdAt: str
	type: str
	previewThumbnailProperties: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2PreviewthumbnailpropertiesData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: Union[NoneType, Union[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData1, BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesDataNodeData2]]
	trackingID: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentData(TypedDict):
	edges: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentDataEdgesData]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData1(TypedDict):
	text: str
	hasEmphasis: bool
	location: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2CollectionnameData(TypedDict):
	fallbackLocalizedTitle: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2(TypedDict):
	id: str
	slug: str
	collectionName: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2CollectionnameData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensData(TypedDict):
	node: Union[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData1, BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensDataNodeData2]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleDataLocalizedtitletokensData]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData1(TypedDict):
	text: str
	hasEmphasis: bool
	location: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2CollectionnameData(TypedDict):
	fallbackLocalizedTitle: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2(TypedDict):
	id: str
	slug: str
	collectionName: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2CollectionnameData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensData(TypedDict):
	node: Union[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData1, BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensDataNodeData2]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleDataLocalizedtitletokensData]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesData(TypedDict):
	content: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataContentData
	id: str
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataTitleData
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesDataSubtitleData
	type: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensDataNodeData(TypedDict):
	text: str
	hasEmphasis: bool
	location: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensDataNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleDataLocalizedtitletokensData]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensDataNodeData(TypedDict):
	text: str
	hasEmphasis: bool
	location: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensData(TypedDict):
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensDataNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleData(TypedDict):
	key: str
	fallbackLocalizedTitle: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleDataLocalizedtitletokensData]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsData(TypedDict):
	id: str
	shelves: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataShelvesData]
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataSubtitleData
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsDataTitleData
	trackingID: str

class BrowseVerticalDirectoryResponseVerticaldirectoryData(TypedDict):
	id: str
	trackingID: Falsy[str]
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleData
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleData
	shelfGroups: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsData]

class BrowseVerticalDirectoryResponse(TypedDict):
	verticalDirectory: BrowseVerticalDirectoryResponseVerticaldirectoryData

class CanCreateClipRequest(TypedDict):
	broadcasterID: Union[NoneType, str]
	vodID: Union[str, NoneType]

class CanCreateClipResponseCancreateclipData(TypedDict):
	isAllowed: bool
	errorCode: Union[str, NoneType]
	requiredFollowingLengthMinutes: Falsy[int]

class CanCreateClipResponse(TypedDict):
	canCreateClip: CanCreateClipResponseCancreateclipData

class CanViewersExportQueryRequest(TypedDict):
	channelLogin: str

class CanViewersExportQueryResponseUserDataChannelDataClipssettingsData(TypedDict):
	isClipsCreationEnabled: bool
	isViewerExportsEnabled: bool

class CanViewersExportQueryResponseUserDataChannelData(TypedDict):
	id: str
	clipsSettings: CanViewersExportQueryResponseUserDataChannelDataClipssettingsData

class CanViewersExportQueryResponseUserData(TypedDict):
	id: str
	channel: CanViewersExportQueryResponseUserDataChannelData

class CanViewersExportQueryResponse(TypedDict):
	user: CanViewersExportQueryResponseUserData

class ChannelAvatarRequest(TypedDict):
	channelLogin: str
	includeIsDJ: bool

class ChannelAvatarResponseUserDataFollowersData(TypedDict):
	totalCount: int

class ChannelAvatarResponseUserDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool

class ChannelAvatarResponseUserData(TypedDict):
	id: str
	followers: ChannelAvatarResponseUserDataFollowersData
	roles: ChannelAvatarResponseUserDataRolesData
	primaryColorHex: Union[NoneType, str]

class ChannelAvatarResponse(TypedDict):
	user: ChannelAvatarResponseUserData

class ChannelClipCoreRequest(TypedDict):
	clipSlug: str

class ChannelClipCoreResponseClipDataBroadcasterDataChannelDataSelfData(TypedDict):
	isAuthorized: bool
	restrictionType: NoneType

class ChannelClipCoreResponseClipDataBroadcasterDataChannelDataTrailerData(TypedDict):
	video: NoneType

class ChannelClipCoreResponseClipDataBroadcasterDataChannelData(TypedDict):
	id: str
	self: ChannelClipCoreResponseClipDataBroadcasterDataChannelDataSelfData
	trailer: ChannelClipCoreResponseClipDataBroadcasterDataChannelDataTrailerData

class ChannelClipCoreResponseClipDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: Union[NoneType, str]
	profileImageURL: str
	stream: NoneType
	channel: ChannelClipCoreResponseClipDataBroadcasterDataChannelData

class ChannelClipCoreResponseClipDataGueststarparticipantsData(TypedDict):
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]

class ChannelClipCoreResponseClipData(TypedDict):
	id: str
	videoOffsetSeconds: Union[int, NoneType]
	broadcaster: ChannelClipCoreResponseClipDataBroadcasterData
	isFeatured: bool
	guestStarParticipants: ChannelClipCoreResponseClipDataGueststarparticipantsData

class ChannelClipCoreResponse(TypedDict):
	clip: ChannelClipCoreResponseClipData

class ChannelCollaborationEligibilityQueryRequestOptionsData(TypedDict):
	channelIDs: List[str]

class ChannelCollaborationEligibilityQueryRequest(TypedDict):
	options: ChannelCollaborationEligibilityQueryRequestOptionsData

class ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesDataChannelcollabsData(TypedDict):
	id: str
	canJoinStatus: str

class ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesData(TypedDict):
	channelCollabs: List[ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesDataChannelcollabsData]

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

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesDataNodeData(TypedDict):
	id: str
	score: int
	rank: int
	user: Union[NoneType, ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesDataNodeDataUserData]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesData(TypedDict):
	cursor: str
	node: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesDataNodeData

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsData(TypedDict):
	edges: Falsy[List[ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesData]]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsData(TypedDict):
	id: str
	items: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsData
	myPosition: NoneType
	secondsRemaining: Falsy[int]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeDataUserData(TypedDict):
	id: str
	login: str
	displayName: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeData(TypedDict):
	id: str
	score: int
	rank: int
	user: Union[NoneType, ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeDataUserData]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesData(TypedDict):
	cursor: str
	node: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesDataNodeData

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsData(TypedDict):
	edges: Falsy[List[ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesData]]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftData(TypedDict):
	id: str
	items: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsData
	myPosition: NoneType
	secondsRemaining: Falsy[int]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetData(TypedDict):
	bits: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsData
	subGift: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftData

class ChannelLeaderboardsResponseUserDataChannelData(TypedDict):
	id: str
	leaderboardTimePeriod: str
	leaderboardSet: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetData

class ChannelLeaderboardsResponseUserDataCheerDataSettingsData(TypedDict):
	id: str
	cheerMinimumBits: int

class ChannelLeaderboardsResponseUserDataCheerData(TypedDict):
	id: str
	settings: ChannelLeaderboardsResponseUserDataCheerDataSettingsData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataPriceinfoData(TypedDict):
	currency: str
	exponent: int
	price: int
	id: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData(TypedDict):
	key: str
	value: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: NoneType

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData]

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData(TypedDict):
	chargeModel: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData(TypedDict):
	min: int
	max: int

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

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityData(TypedDict):
	offer: Union[NoneType, ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData]

class ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingData(TypedDict):
	community: Union[NoneType, List[ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingDataCommunityData]]

class ChannelLeaderboardsResponseUserDataSubscriptionproductsData(TypedDict):
	id: str
	name: str
	price: str
	priceInfo: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataPriceinfoData
	gifting: ChannelLeaderboardsResponseUserDataSubscriptionproductsDataGiftingData

class ChannelLeaderboardsResponseUserData(TypedDict):
	id: str
	login: str
	displayName: str
	channel: ChannelLeaderboardsResponseUserDataChannelData
	cheer: ChannelLeaderboardsResponseUserDataCheerData
	subscriptionProducts: List[ChannelLeaderboardsResponseUserDataSubscriptionproductsData]

class ChannelLeaderboardsResponseCurrentuserData(TypedDict):
	id: str

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

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataTagbindingsData(TypedDict):
	key: str
	value: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceDataDiscountData(TypedDict):
	price: int
	total: int

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceDataDiscountData]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalData]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingData(TypedDict):
	chargeModel: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataListingDataChargemodelData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataPromotionDataPromodisplayData(TypedDict):
	discountPercent: int
	discountType: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataPromotionData(TypedDict):
	id: str
	name: str
	promoDisplay: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataPromotionDataPromodisplayData
	priority: Falsy[int]
	promoType: str
	endAt: NoneType

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersDataQuantityData(TypedDict):
	min: int
	max: int

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

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData(TypedDict):
	key: str
	value: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: NoneType

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData(TypedDict):
	chargeModel: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData(TypedDict):
	min: int
	max: int

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

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityData(TypedDict):
	offer: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingData(TypedDict):
	community: Union[NoneType, List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingDataCommunityData]]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsData(TypedDict):
	id: str
	emoteSetID: str
	name: str
	hasAdFree: bool
	tier: str
	offers: Union[NoneType, List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataOffersData]]
	gifting: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsDataGiftingData

class ChannelPage_SubscribeButton_UserResponseUserDataSelfDataCumulativetenureData(TypedDict):
	daysRemaining: Falsy[int]
	months: Falsy[int]

class ChannelPage_SubscribeButton_UserResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool

class ChannelPage_SubscribeButton_UserResponseUserDataSelfData(TypedDict):
	canPrimeSubscribe: bool
	cumulativeTenure: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSelfDataCumulativetenureData]
	follower: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSelfDataFollowerData]
	subscriptionBenefit: NoneType

class ChannelPage_SubscribeButton_UserResponseUserData(TypedDict):
	id: str
	displayName: str
	primaryColorHex: Union[NoneType, str]
	subscriptionProducts: Falsy[List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsData]]
	self: Union[NoneType, ChannelPage_SubscribeButton_UserResponseUserDataSelfData]

class ChannelPage_SubscribeButton_UserResponseRequestinfoData(TypedDict):
	countryCode: str

class ChannelPage_SubscribeButton_UserResponse(TypedDict):
	user: ChannelPage_SubscribeButton_UserResponseUserData
	requestInfo: ChannelPage_SubscribeButton_UserResponseRequestinfoData

class ChannelPointsContextRequest(TypedDict):
	channelLogin: str
	includeGoalTypes: List[str]

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData(TypedDict):
	id: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataLastviewedcontentData(TypedDict):
	contentType: str
	lastViewedAt: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsDataRewardData(TypedDict):
	id: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsData(TypedDict):
	reward: ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsDataRewardData
	userRedemptionsCurrentStream: Falsy[int]

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsData(TypedDict):
	availableClaim: Union[NoneType, ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData]
	balance: Falsy[int]
	activeMultipliers: Falsy[List[Any]]
	canRedeemRewardsForFree: bool
	lastViewedContent: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataLastviewedcontentData]]
	userRedemptions: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataUserredemptionsData]]

class ChannelPointsContextResponseCommunityDataChannelDataSelfData(TypedDict):
	communityPoints: Union[NoneType, ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsData]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataImageData(TypedDict):
	url: str
	url2x: str
	url4x: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataDefaultimageData(TypedDict):
	url: str
	url2x: str
	url4x: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerStream: Falsy[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperuserperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerUserPerStream: Falsy[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataGlobalcooldownsettingData(TypedDict):
	isEnabled: bool
	globalCooldownSeconds: Falsy[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsData(TypedDict):
	id: str
	backgroundColor: Union[str, NoneType]
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
	redemptionsRedeemedCurrentStream: Union[Falsy[int], NoneType]
	minimumCost: Falsy[int]
	pricingType: str
	type: str
	updatedForIndicatorAt: Union[str, NoneType]
	globallyUpdatedForIndicatorAt: str
	maxPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperstreamsettingData
	maxPerUserPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataMaxperuserperstreamsettingData
	globalCooldownSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsDataGlobalcooldownsettingData

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataDefaultimageData(TypedDict):
	url: str
	url2x: str
	url4x: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataImageData(TypedDict):
	url: str
	url2x: str
	url4x: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataMaxperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerStream: Falsy[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataMaxperuserperstreamsettingData(TypedDict):
	isEnabled: bool
	maxPerUserPerStream: Falsy[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsDataGlobalcooldownsettingData(TypedDict):
	isEnabled: bool
	globalCooldownSeconds: Falsy[int]

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

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataGoalsDataDefaultimageData(TypedDict):
	url: str
	url2x: str
	url4x: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataGoalsData(TypedDict):
	backgroundColor: str
	description: Union[str, NoneType]
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

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataEmoteData(TypedDict):
	id: str
	token: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataEmoteData(TypedDict):
	id: str
	token: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataModifierData(TypedDict):
	id: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsData(TypedDict):
	id: str
	emote: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataEmoteData
	modifier: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsDataModifierData
	globallyUpdatedForIndicatorAt: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsData(TypedDict):
	id: str
	isUnlockable: bool
	emote: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataEmoteData
	modifications: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsDataModificationsData]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataWatchstreakpointsData(TypedDict):
	points: int

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataMultipliersData(TypedDict):
	reasonCode: str
	factor: Union[int, float]

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

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsData(TypedDict):
	name: Union[str, NoneType]
	image: Union[NoneType, ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataImageData]
	automaticRewards: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsData]]
	customRewards: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsData]]
	goals: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataGoalsData]]
	isEnabled: bool
	raidPointAmount: int
	emoteVariants: Falsy[List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsData]]
	earning: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningData

class ChannelPointsContextResponseCommunityDataChannelData(TypedDict):
	id: str
	self: ChannelPointsContextResponseCommunityDataChannelDataSelfData
	communityPointsSettings: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsData

class ChannelPointsContextResponseCommunityDataSelfData(TypedDict):
	isModerator: bool

class ChannelPointsContextResponseCommunityData(TypedDict):
	id: str
	displayName: str
	profileImageURL: str
	channel: ChannelPointsContextResponseCommunityDataChannelData
	self: Union[NoneType, ChannelPointsContextResponseCommunityDataSelfData]

class ChannelPointsContextResponseCurrentuserDataCommunitypointsDataLastviewedcontentData(TypedDict):
	contentID: str
	contentType: str
	lastViewedAt: str

class ChannelPointsContextResponseCurrentuserDataCommunitypointsData(TypedDict):
	lastViewedContent: List[ChannelPointsContextResponseCurrentuserDataCommunitypointsDataLastviewedcontentData]

class ChannelPointsContextResponseCurrentuserData(TypedDict):
	id: str
	communityPoints: ChannelPointsContextResponseCurrentuserDataCommunitypointsData

class ChannelPointsContextResponse(TypedDict):
	community: ChannelPointsContextResponseCommunityData
	currentUser: Union[NoneType, ChannelPointsContextResponseCurrentuserData]

class ChannelPointsGlobalContextRequest(TypedDict):
	...

class ChannelPointsGlobalContextResponseEmotemodifiersDataIcondarkData(TypedDict):
	url: str
	url2x: str
	url4x: str

class ChannelPointsGlobalContextResponseEmotemodifiersDataIconlightData(TypedDict):
	url: str
	url2x: str
	url4x: str

class ChannelPointsGlobalContextResponseEmotemodifiersData(TypedDict):
	id: str
	title: str
	iconDark: ChannelPointsGlobalContextResponseEmotemodifiersDataIcondarkData
	iconLight: ChannelPointsGlobalContextResponseEmotemodifiersDataIconlightData

class ChannelPointsGlobalContextResponse(TypedDict):
	emoteModifiers: List[ChannelPointsGlobalContextResponseEmotemodifiersData]

class ChannelPointsPredictionContextRequest(TypedDict):
	count: int
	channelLogin: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataPredictionsettingsData(TypedDict):
	isEligibleForPredictions: bool

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataCreatedbyData(TypedDict):
	id: str
	displayName: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsData(TypedDict):
	id: str
	points: int
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsDataUserData

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

class ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: int
	totalUsers: int
	topPredictors: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataToppredictorsData]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsDataOutcomesDataBadgeData

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

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataCreatedbyData(TypedDict):
	id: str
	displayName: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsData(TypedDict):
	id: str
	points: int
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsDataUserData

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

class ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: int
	totalUsers: int
	topPredictors: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataToppredictorsData]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsDataOutcomesDataBadgeData

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

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataCreatedbyData(TypedDict):
	id: str
	displayName: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsData(TypedDict):
	id: str
	points: Falsy[int]
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsDataUserData

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

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: Falsy[int]
	totalUsers: Falsy[int]
	topPredictors: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataToppredictorsData]]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataOutcomesDataBadgeData

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsDataUserData(TypedDict):
	id: str
	displayName: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsData(TypedDict):
	id: str
	points: Falsy[int]
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsDataUserData

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

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeData(TypedDict):
	id: str
	color: str
	title: str
	totalPoints: Falsy[int]
	totalUsers: Falsy[int]
	topPredictors: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataToppredictorsData]]
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeDataWinningoutcomeDataBadgeData

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

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesData(TypedDict):
	node: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesDataNodeData

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsData(TypedDict):
	edges: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesData]]

class ChannelPointsPredictionContextResponseCommunityDataChannelDataSelfData(TypedDict):
	recentPredictions: Union[NoneType, Falsy[List[Any]]]

class ChannelPointsPredictionContextResponseCommunityDataChannelData(TypedDict):
	id: str
	predictionSettings: ChannelPointsPredictionContextResponseCommunityDataChannelDataPredictionsettingsData
	activePredictionEvents: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataActivepredictioneventsData]]
	lockedPredictionEvents: Falsy[List[ChannelPointsPredictionContextResponseCommunityDataChannelDataLockedpredictioneventsData]]
	resolvedPredictionEvents: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsData
	self: ChannelPointsPredictionContextResponseCommunityDataChannelDataSelfData

class ChannelPointsPredictionContextResponseCommunityData(TypedDict):
	id: str
	channel: ChannelPointsPredictionContextResponseCommunityDataChannelData

class ChannelPointsPredictionContextResponseCurrentuserDataPredictionssettingsData(TypedDict):
	hasAcceptedTOS: bool
	isTemporaryChatBadgeEnabled: bool

class ChannelPointsPredictionContextResponseCurrentuserData(TypedDict):
	id: str
	predictionsSettings: ChannelPointsPredictionContextResponseCurrentuserDataPredictionssettingsData

class ChannelPointsPredictionContextResponse(TypedDict):
	community: ChannelPointsPredictionContextResponseCommunityData
	currentUser: Union[NoneType, ChannelPointsPredictionContextResponseCurrentuserData]

class ChannelPollContext_GetViewablePollRequest(TypedDict):
	login: str

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataChoicesDataTokensData(TypedDict):
	communityPoints: Falsy[int]
	id: str

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataChoicesDataVotesData(TypedDict):
	total: int
	communityPoints: Falsy[int]
	base: int
	id: str

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataChoicesData(TypedDict):
	id: str
	title: str
	tokens: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataChoicesDataTokensData
	totalVoters: int
	votes: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataChoicesDataVotesData

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataOwnedbyData(TypedDict):
	id: str

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataCreatedbyData(TypedDict):
	id: str

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataTokensData(TypedDict):
	communityPoints: Falsy[int]
	id: str

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataVotesData(TypedDict):
	total: int
	communityPoints: Falsy[int]
	base: int
	id: str

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataSettingsDataCommunitypointsvotesData(TypedDict):
	cost: Falsy[int]
	isEnabled: bool

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataSettingsDataMultichoiceData(TypedDict):
	isEnabled: bool

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataSettingsData(TypedDict):
	communityPointsVotes: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataSettingsDataCommunitypointsvotesData
	id: str
	multichoice: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataSettingsDataMultichoiceData

class ChannelPollContext_GetViewablePollResponseChannelDataViewablepollData(TypedDict):
	id: str
	choices: List[ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataChoicesData]
	durationSeconds: int
	startedAt: str
	endedAt: NoneType
	status: str
	title: str
	ownedBy: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataOwnedbyData
	createdBy: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataCreatedbyData
	tokens: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataTokensData
	totalVoters: int
	votes: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataVotesData
	settings: ChannelPollContext_GetViewablePollResponseChannelDataViewablepollDataSettingsData
	remainingDurationMilliseconds: int
	topCommunityPointsContributor: NoneType
	self: NoneType

class ChannelPollContext_GetViewablePollResponseChannelDataSelfData(TypedDict):
	isEditor: bool
	isModerator: bool

class ChannelPollContext_GetViewablePollResponseChannelData(TypedDict):
	id: str
	viewablePoll: Union[NoneType, ChannelPollContext_GetViewablePollResponseChannelDataViewablepollData]
	self: Union[NoneType, ChannelPollContext_GetViewablePollResponseChannelDataSelfData]

class ChannelPollContext_GetViewablePollResponseCurrentuserData(TypedDict):
	id: str

class ChannelPollContext_GetViewablePollResponse(TypedDict):
	channel: ChannelPollContext_GetViewablePollResponseChannelData
	currentUser: Union[NoneType, ChannelPollContext_GetViewablePollResponseCurrentuserData]

class ChannelShellRequest(TypedDict):
	login: str

class ChannelShellResponseUserorerrorDataStreamData(TypedDict):
	id: str
	viewersCount: int

class ChannelShellResponseUserorerrorDataChannelDataSelfData(TypedDict):
	isAuthorized: bool
	restrictionType: NoneType

class ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoDataSelfDataViewinghistoryData(TypedDict):
	updatedAt: NoneType

class ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoDataSelfData(TypedDict):
	viewingHistory: Union[NoneType, ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoDataSelfDataViewinghistoryData]

class ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoData(TypedDict):
	id: str
	self: ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoDataSelfData

class ChannelShellResponseUserorerrorDataChannelDataTrailerData(TypedDict):
	video: Union[NoneType, ChannelShellResponseUserorerrorDataChannelDataTrailerDataVideoData]

class ChannelShellResponseUserorerrorDataChannelDataHomeDataPreferencesData(TypedDict):
	heroPreset: str

class ChannelShellResponseUserorerrorDataChannelDataHomeData(TypedDict):
	preferences: ChannelShellResponseUserorerrorDataChannelDataHomeDataPreferencesData

class ChannelShellResponseUserorerrorDataChannelData(TypedDict):
	id: str
	self: ChannelShellResponseUserorerrorDataChannelDataSelfData
	trailer: ChannelShellResponseUserorerrorDataChannelDataTrailerData
	home: ChannelShellResponseUserorerrorDataChannelDataHomeData

class ChannelShellResponseUserorerrorData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: Union[NoneType, str]
	profileImageURL: str
	stream: Union[NoneType, ChannelShellResponseUserorerrorDataStreamData]
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

class ChannelSkinsResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType

class ChannelSkinsResponseUserData(TypedDict):
	id: str
	displayName: str
	profileImageURL: str
	login: str
	primaryColorHex: Union[NoneType, str]
	self: Union[NoneType, ChannelSkinsResponseUserDataSelfData]

class ChannelSkinsResponseCurrentuserData(TypedDict):
	id: str
	hasTurbo: bool

class ChannelSkinsResponseRequestinfoData(TypedDict):
	countryCodeAlpha2: str

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

class ChannelSocialButtonsResponseChannelDataLocalemotesetsData(TypedDict):
	id: str
	emotes: List[ChannelSocialButtonsResponseChannelDataLocalemotesetsDataEmotesData]
	productType: str

class ChannelSocialButtonsResponseChannelData(TypedDict):
	id: str
	localEmoteSets: List[ChannelSocialButtonsResponseChannelDataLocalemotesetsData]

class ChannelSocialButtonsResponse(TypedDict):
	channel: ChannelSocialButtonsResponseChannelData

class ChannelSupportButtonsRequest(TypedDict):
	channelLogin: str

class ChannelSupportButtonsResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool

class ChannelSupportButtonsResponseUserDataSelfData(TypedDict):
	follower: Union[NoneType, ChannelSupportButtonsResponseUserDataSelfDataFollowerData]

class ChannelSupportButtonsResponseUserData(TypedDict):
	id: str
	displayName: str
	self: Union[NoneType, ChannelSupportButtonsResponseUserDataSelfData]

class ChannelSupportButtonsResponse(TypedDict):
	user: ChannelSupportButtonsResponseUserData

class ChannelVideoCoreRequest(TypedDict):
	videoID: str

class ChannelVideoCoreResponseVideoDataOwnerDataChannelDataSelfData(TypedDict):
	isAuthorized: bool
	restrictionType: NoneType

class ChannelVideoCoreResponseVideoDataOwnerDataChannelDataTrailerData(TypedDict):
	video: NoneType

class ChannelVideoCoreResponseVideoDataOwnerDataChannelData(TypedDict):
	id: str
	self: ChannelVideoCoreResponseVideoDataOwnerDataChannelDataSelfData
	trailer: ChannelVideoCoreResponseVideoDataOwnerDataChannelDataTrailerData

class ChannelVideoCoreResponseVideoDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: str
	profileImageURL: str
	stream: NoneType
	channel: ChannelVideoCoreResponseVideoDataOwnerDataChannelData

class ChannelVideoCoreResponseVideoData(TypedDict):
	id: str
	owner: ChannelVideoCoreResponseVideoDataOwnerData

class ChannelVideoCoreResponse(TypedDict):
	video: ChannelVideoCoreResponseVideoData

class ChannelVideosContent_GameRequest(TypedDict):
	categoryID: str

class ChannelVideosContent_GameResponseGameData(TypedDict):
	id: str
	displayName: str
	name: str

class ChannelVideosContent_GameResponse(TypedDict):
	game: ChannelVideosContent_GameResponseGameData

class Chat_ChannelDataRequest(TypedDict):
	channelLogin: str

class Chat_ChannelDataResponseChannelDataChatsettingsData(TypedDict):
	rules: Falsy[List[Falsy[str]]]

class Chat_ChannelDataResponseChannelDataSelfData(TypedDict):
	isEditor: bool
	isModerator: bool
	isVIP: bool

class Chat_ChannelDataResponseChannelData(TypedDict):
	id: str
	login: str
	displayName: str
	chatSettings: Chat_ChannelDataResponseChannelDataChatsettingsData
	self: Union[NoneType, Chat_ChannelDataResponseChannelDataSelfData]

class Chat_ChannelDataResponse(TypedDict):
	channel: Chat_ChannelDataResponseChannelData

class Chat_EarnedBadges_InitialSubStatusRequest(TypedDict):
	channelLogin: str

class Chat_EarnedBadges_InitialSubStatusResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType

class Chat_EarnedBadges_InitialSubStatusResponseUserData(TypedDict):
	id: str
	self: Chat_EarnedBadges_InitialSubStatusResponseUserDataSelfData

class Chat_EarnedBadges_InitialSubStatusResponse(TypedDict):
	user: Chat_EarnedBadges_InitialSubStatusResponseUserData

class Chat_OrbisPresetTextRequest(TypedDict):
	login: str

class Chat_OrbisPresetTextResponseUserDataStreamData(TypedDict):
	id: str
	platform: NoneType

class Chat_OrbisPresetTextResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, Chat_OrbisPresetTextResponseUserDataStreamData]

class Chat_OrbisPresetTextResponse(TypedDict):
	user: Chat_OrbisPresetTextResponseUserData

class Chat_ShareResub_ChannelDataRequest(TypedDict):
	channelLogin: str

class Chat_ShareResub_ChannelDataResponseUserDataSelfData(TypedDict):
	resubNotification: NoneType

class Chat_ShareResub_ChannelDataResponseUserData(TypedDict):
	id: str
	self: Chat_ShareResub_ChannelDataResponseUserDataSelfData

class Chat_ShareResub_ChannelDataResponse(TypedDict):
	user: Chat_ShareResub_ChannelDataResponseUserData

class Chat_UserDataRequest(TypedDict):
	...

class Chat_UserDataResponseUserDataRolesData(TypedDict):
	isGlobalMod: NoneType
	isSiteAdmin: NoneType
	isStaff: NoneType

class Chat_UserDataResponseUserData(TypedDict):
	id: str
	displayName: str
	login: str
	roles: Chat_UserDataResponseUserDataRolesData

class Chat_UserDataResponse(TypedDict):
	user: Chat_UserDataResponseUserData

class ChatClipRequest(TypedDict):
	clipSlug: str

class ChatClipResponseClipDataVideoData(TypedDict):
	id: str

class ChatClipResponseClipData(TypedDict):
	id: str
	videoOffsetSeconds: Union[int, NoneType]
	durationSeconds: int
	video: Union[NoneType, ChatClipResponseClipDataVideoData]

class ChatClipResponse(TypedDict):
	clip: ChatClipResponseClipData

class ChatFilterContextManager_UserRequest(TypedDict):
	...

class ChatFilterContextManager_UserResponseCurrentuserData(TypedDict):
	id: str
	createdAt: str

class ChatFilterContextManager_UserResponse(TypedDict):
	currentUser: ChatFilterContextManager_UserResponseCurrentuserData

class ChatInputRequest(TypedDict):
	channelLogin: str
	isEmbedded: bool

class ChatInputResponseCurrentuserData(TypedDict):
	id: str
	bitsBalance: Falsy[int]

class ChatInputResponseChannelDataSelfDataChatmoderatorstrikestatusData(TypedDict):
	id: str
	banDetails: NoneType
	warningDetails: NoneType
	timeoutDetails: NoneType

class ChatInputResponseChannelDataSelfData(TypedDict):
	chatModeratorStrikeStatus: ChatInputResponseChannelDataSelfDataChatmoderatorstrikestatusData

class ChatInputResponseChannelDataCheerDataSettingsData(TypedDict):
	id: str
	emoteMinimumBits: int
	cheerMinimumBits: int
	event: NoneType

class ChatInputResponseChannelDataCheerData(TypedDict):
	id: str
	settings: ChatInputResponseChannelDataCheerDataSettingsData

class ChatInputResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, ChatInputResponseChannelDataSelfData]
	displayName: str
	profileImageURL: str
	cheer: Union[NoneType, ChatInputResponseChannelDataCheerData]

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

class ChatList_BadgesResponseUserDataSelfData(TypedDict):
	selectedBadge: NoneType
	displayBadges: Falsy[List[Any]]

class ChatList_BadgesResponseUserData(TypedDict):
	id: str
	primaryColorHex: Union[NoneType, str]
	broadcastBadges: Falsy[List[ChatList_BadgesResponseUserDataBroadcastbadgesData]]
	self: Union[NoneType, ChatList_BadgesResponseUserDataSelfData]

class ChatList_BadgesResponse(TypedDict):
	user: ChatList_BadgesResponseUserData

class ChatModeratorStrikeStatusRequest(TypedDict):
	channelID: str
	targetUserID: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataModerateduserData(TypedDict):
	id: str
	login: str
	displayName: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataRoomownerData(TypedDict):
	id: str
	login: str
	displayName: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusData(TypedDict):
	id: str
	moderatedUser: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataModerateduserData
	roomOwner: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataRoomownerData
	banDetails: NoneType
	timeoutDetails: NoneType
	warningDetails: NoneType

class ChatModeratorStrikeStatusResponse(TypedDict):
	chatModeratorStrikeStatus: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusData

class ChatRestrictionsRequest(TypedDict):
	channelLogin: str

class ChatRestrictionsResponseChannelDataSelfDataFollowerData(TypedDict):
	followedAt: str

class ChatRestrictionsResponseChannelDataSelfData(TypedDict):
	chatRestrictedReasons: List[str]
	lastRecentChatMessageAt: NoneType
	follower: Union[NoneType, ChatRestrictionsResponseChannelDataSelfDataFollowerData]
	banStatus: NoneType
	isFirstTimeChatter: bool
	subscriptionBenefit: NoneType
	isVIP: bool
	isModerator: bool

class ChatRestrictionsResponseChannelDataChatsettingsData(TypedDict):
	requireVerifiedAccount: bool

class ChatRestrictionsResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, ChatRestrictionsResponseChannelDataSelfData]
	chatSettings: ChatRestrictionsResponseChannelDataChatsettingsData

class ChatRestrictionsResponseCurrentuserData(TypedDict):
	id: str
	createdAt: str
	isEmailVerified: bool
	isPhoneNumberVerified: bool

class ChatRestrictionsResponse(TypedDict):
	channel: ChatRestrictionsResponseChannelData
	currentUser: Union[NoneType, ChatRestrictionsResponseCurrentuserData]

class ChatRoomBanStatusRequest(TypedDict):
	targetUserID: str
	channelID: str

class ChatRoomBanStatusResponseTargetuserData(TypedDict):
	id: str
	login: str

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

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialphoneverificationconfigData(TypedDict):
	minimumAccountAgeInMinutes: Falsy[int]
	minimumFollowerAgeInMinutes: Falsy[int]
	shouldRestrictBasedOnAccountAge: bool
	shouldRestrictFirstTimeChatters: bool
	shouldRestrictBasedOnFollowerAge: bool

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsData(TypedDict):
	emailVerificationMode: str
	partialEmailVerificationConfig: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialemailverificationconfigData
	phoneVerificationMode: str
	partialPhoneVerificationConfig: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialphoneverificationconfigData
	isSubscriberExempt: bool
	isVIPExempt: bool
	isModeratorExempt: bool

class ChatRoomStateResponseChannelDataChatsettingsData(TypedDict):
	isEmoteOnlyModeEnabled: bool
	followersOnlyDurationMinutes: Union[NoneType, Falsy[int]]
	slowModeDurationSeconds: Union[int, NoneType]
	accountVerificationOptions: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsData

class ChatRoomStateResponseChannelDataSubscriptionproductsData(TypedDict):
	id: str
	hasSubOnlyChat: bool

class ChatRoomStateResponseChannelData(TypedDict):
	id: str
	chatSettings: ChatRoomStateResponseChannelDataChatsettingsData
	subscriptionProducts: Falsy[List[ChatRoomStateResponseChannelDataSubscriptionproductsData]]

class ChatRoomStateResponse(TypedDict):
	channel: ChatRoomStateResponseChannelData

class ChatScreenReaderAutoAnnounceRequest(TypedDict):
	...

class ChatScreenReaderAutoAnnounceResponseCurrentuserData(TypedDict):
	id: str
	isChatScreenReaderAutoAnnounceEnabled: bool

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

class ClaimCommunityPointsResponseClaimcommunitypointsData(TypedDict):
	claim: ClaimCommunityPointsResponseClaimcommunitypointsDataClaimData
	currentPoints: int
	error: NoneType

class ClaimCommunityPointsResponse(TypedDict):
	claimCommunityPoints: ClaimCommunityPointsResponseClaimcommunitypointsData

class ClipMetadataRequest(TypedDict):
	clipSlug: str

class ClipMetadataResponseCurrentuserDataSelfData(TypedDict):
	isEditor: bool

class ClipMetadataResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType
	isSiteAdmin: NoneType

class ClipMetadataResponseCurrentuserData(TypedDict):
	id: str
	login: str
	self: ClipMetadataResponseCurrentuserDataSelfData
	roles: ClipMetadataResponseCurrentuserDataRolesData

class ClipMetadataResponseClipDataGueststarparticipantsData(TypedDict):
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]

class ClipMetadataResponseClipData(TypedDict):
	id: str
	guestStarParticipants: ClipMetadataResponseClipDataGueststarparticipantsData

class ClipMetadataResponseRequestinfoData(TypedDict):
	countryCode: str

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

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataCuratorData(TypedDict):
	id: str
	login: str
	displayName: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	boxArtURL: str

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: str
	roles: ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataBroadcasterDataRolesData

class ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeDataGueststarparticipantsData(TypedDict):
	guests: Falsy[List[Any]]
	sessionIdentifier: Falsy[str]

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

class ClipsCards__UserResponseUserDataClipsDataEdgesData(TypedDict):
	cursor: Union[str, NoneType]
	node: ClipsCards__UserResponseUserDataClipsDataEdgesDataNodeData

class ClipsCards__UserResponseUserDataClipsData(TypedDict):
	pageInfo: ClipsCards__UserResponseUserDataClipsDataPageinfoData
	edges: List[ClipsCards__UserResponseUserDataClipsDataEdgesData]

class ClipsCards__UserResponseUserData(TypedDict):
	id: str
	clips: ClipsCards__UserResponseUserDataClipsData

class ClipsCards__UserResponse(TypedDict):
	user: ClipsCards__UserResponseUserData

class ClipsExperimentEnrollmentStatusRequest(TypedDict):
	channelID: str

class ClipsExperimentEnrollmentStatusResponseIsenrolledinclipsexperimentData(TypedDict):
	id: str
	isEnrolled: bool

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

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	roles: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataOwnerDataRolesData

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: NoneType

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

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesData(TypedDict):
	cursor: str
	node: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesDataNodeData

class CollectionCarouselQueryResponseCollectionDataItemsDataPageinfoData(TypedDict):
	hasNextPage: bool

class CollectionCarouselQueryResponseCollectionDataItemsData(TypedDict):
	totalCount: int
	edges: List[CollectionCarouselQueryResponseCollectionDataItemsDataEdgesData]
	pageInfo: CollectionCarouselQueryResponseCollectionDataItemsDataPageinfoData

class CollectionCarouselQueryResponseCollectionDataOwnerData(TypedDict):
	id: str
	login: str

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

class CollectionCarouselQueryResponse(TypedDict):
	collection: CollectionCarouselQueryResponseCollectionData

class CommonHooks_BlockedUsersRequest(TypedDict):
	...

class CommonHooks_BlockedUsersResponseCurrentuserData(TypedDict):
	id: str
	blockedUsers: Falsy[List[Any]]

class CommonHooks_BlockedUsersResponse(TypedDict):
	currentUser: Union[NoneType, CommonHooks_BlockedUsersResponseCurrentuserData]

class CommunityOnboardingAllowlistRequest(TypedDict):
	channelID: str

class CommunityOnboardingAllowlistResponseCommunityonboardingDataChannelallowlistsData(TypedDict):
	experimentName: str

class CommunityOnboardingAllowlistResponseCommunityonboardingData(TypedDict):
	channelAllowLists: Falsy[List[CommunityOnboardingAllowlistResponseCommunityonboardingDataChannelallowlistsData]]

class CommunityOnboardingAllowlistResponse(TypedDict):
	communityOnboarding: CommunityOnboardingAllowlistResponseCommunityonboardingData

class CommunityPointsAvailableClaimRequest(TypedDict):
	channelID: str

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData(TypedDict):
	id: str

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsData(TypedDict):
	availableClaim: Union[NoneType, CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData]
	balance: Falsy[int]
	activeMultipliers: Falsy[List[Any]]
	canRedeemRewardsForFree: bool

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfData(TypedDict):
	communityPoints: CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsData

class CommunityPointsAvailableClaimResponseCommunityDataChannelData(TypedDict):
	id: str
	self: CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfData

class CommunityPointsAvailableClaimResponseCommunityData(TypedDict):
	id: str
	login: str
	channel: CommunityPointsAvailableClaimResponseCommunityDataChannelData

class CommunityPointsAvailableClaimResponse(TypedDict):
	community: CommunityPointsAvailableClaimResponseCommunityData

class CommunityPointsChatPrivateCalloutUserRequest(TypedDict):
	login: str

class CommunityPointsChatPrivateCalloutUserResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType
	isModerator: bool

class CommunityPointsChatPrivateCalloutUserResponseUserData(TypedDict):
	id: str
	self: CommunityPointsChatPrivateCalloutUserResponseUserDataSelfData

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

class CommunitySupportSettingsResponseUserDataSettingsDataRecentchannelsupporteventsData(TypedDict):
	isOptedOut: bool

class CommunitySupportSettingsResponseUserDataSettingsData(TypedDict):
	leaderboard: CommunitySupportSettingsResponseUserDataSettingsDataLeaderboardData
	recentChannelSupportEvents: CommunitySupportSettingsResponseUserDataSettingsDataRecentchannelsupporteventsData

class CommunitySupportSettingsResponseUserData(TypedDict):
	id: str
	login: str
	settings: CommunitySupportSettingsResponseUserDataSettingsData

class CommunitySupportSettingsResponse(TypedDict):
	user: CommunitySupportSettingsResponseUserData

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

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelsData(TypedDict):
	id: str
	localizedName: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	signPost: str
	contentClassificationLabels: Falsy[List[str]]

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	contentGate: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesData(TypedDict):
	signPostProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData
	contentGateProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData

class ContentClassificationContextResponse1UserDataStreamData(TypedDict):
	id: str
	game: ContentClassificationContextResponse1UserDataStreamDataGameData
	contentClassificationLabels: Falsy[List[ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelsData]]
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesData

class ContentClassificationContextResponse1UserData(TypedDict):
	id: str
	stream: Union[NoneType, ContentClassificationContextResponse1UserDataStreamData]
	displayName: str

class ContentClassificationContextResponse1(TypedDict):
	user: ContentClassificationContextResponse1UserData

class ContentClassificationContextResponse2VideoDataGameData(TypedDict):
	id: str
	name: str

class ContentClassificationContextResponse2VideoDataOwnerData(TypedDict):
	id: str
	displayName: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelsData(TypedDict):
	id: str
	localizedName: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	signPost: str
	contentClassificationLabels: Falsy[List[str]]

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	contentGate: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesData(TypedDict):
	signPostProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData
	contentGateProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData

class ContentClassificationContextResponse2VideoData(TypedDict):
	id: str
	broadcastType: str
	game: ContentClassificationContextResponse2VideoDataGameData
	owner: ContentClassificationContextResponse2VideoDataOwnerData
	contentClassificationLabels: Falsy[List[ContentClassificationContextResponse2VideoDataContentclassificationlabelsData]]
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesData

class ContentClassificationContextResponse2(TypedDict):
	video: ContentClassificationContextResponse2VideoData

class ContentClassificationContextResponse3ClipDataBroadcasterData(TypedDict):
	id: str
	displayName: str

class ContentClassificationContextResponse3ClipDataGameData(TypedDict):
	id: str
	name: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelsData(TypedDict):
	id: str
	localizedName: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	signPost: str
	contentClassificationLabels: Falsy[List[str]]

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	contentGate: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesData(TypedDict):
	signPostProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData
	contentGateProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData

class ContentClassificationContextResponse3ClipData(TypedDict):
	id: str
	slug: str
	broadcaster: ContentClassificationContextResponse3ClipDataBroadcasterData
	game: ContentClassificationContextResponse3ClipDataGameData
	contentClassificationLabels: Falsy[List[ContentClassificationContextResponse3ClipDataContentclassificationlabelsData]]
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesData

class ContentClassificationContextResponse3(TypedDict):
	clip: ContentClassificationContextResponse3ClipData

class ContentPolicyPropertiesQueryRequest(TypedDict):
	login: Falsy[str]
	vodID: Falsy[str]
	isLive: bool
	isVOD: bool

class ContentPolicyPropertiesQueryResponse1UserDataStreamDataContentpolicypropertiesData(TypedDict):
	hasBrandedContent: bool

class ContentPolicyPropertiesQueryResponse1UserDataStreamData(TypedDict):
	id: str
	contentPolicyProperties: ContentPolicyPropertiesQueryResponse1UserDataStreamDataContentpolicypropertiesData

class ContentPolicyPropertiesQueryResponse1UserData(TypedDict):
	id: str
	stream: Union[NoneType, ContentPolicyPropertiesQueryResponse1UserDataStreamData]

class ContentPolicyPropertiesQueryResponse1(TypedDict):
	user: ContentPolicyPropertiesQueryResponse1UserData

class ContentPolicyPropertiesQueryResponse2VideoDataContentpolicypropertiesData(TypedDict):
	hasBrandedContent: bool

class ContentPolicyPropertiesQueryResponse2VideoDataOwnerData(TypedDict):
	id: str
	login: str

class ContentPolicyPropertiesQueryResponse2VideoData(TypedDict):
	id: str
	broadcastType: str
	contentPolicyProperties: ContentPolicyPropertiesQueryResponse2VideoDataContentpolicypropertiesData
	owner: ContentPolicyPropertiesQueryResponse2VideoDataOwnerData

class ContentPolicyPropertiesQueryResponse2(TypedDict):
	video: ContentPolicyPropertiesQueryResponse2VideoData

class CoreActionsCurrentUserRequest(TypedDict):
	...

class CoreActionsCurrentUserResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType

class CoreActionsCurrentUserResponseCurrentuserDataSettingsData(TypedDict):
	preferredLanguageTag: str

class CoreActionsCurrentUserResponseCurrentuserData(TypedDict):
	displayName: str
	id: str
	login: str
	roles: CoreActionsCurrentUserResponseCurrentuserDataRolesData
	settings: CoreActionsCurrentUserResponseCurrentuserDataSettingsData

class CoreActionsCurrentUserResponse(TypedDict):
	currentUser: CoreActionsCurrentUserResponseCurrentuserData

class CurrentUserBannedStatusRequest(TypedDict):
	channelLogin: str

class CurrentUserBannedStatusResponseChannelDataSelfData(TypedDict):
	banStatus: NoneType

class CurrentUserBannedStatusResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, CurrentUserBannedStatusResponseChannelDataSelfData]

class CurrentUserBannedStatusResponse(TypedDict):
	channel: CurrentUserBannedStatusResponseChannelData

class CurrentUserModeratorStatusRequest1(TypedDict):
	channelID: str

class CurrentUserModeratorStatusRequest2(TypedDict):
	channelLogin: str

class CurrentUserModeratorStatusResponseUserDataSelfData(TypedDict):
	isModerator: bool

class CurrentUserModeratorStatusResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, CurrentUserModeratorStatusResponseUserDataSelfData]

class CurrentUserModeratorStatusResponseCurrentuserData(TypedDict):
	id: str

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

class CurrentUserStrikeStatusResponseChannelDataSelfData(TypedDict):
	chatModeratorStrikeStatus: CurrentUserStrikeStatusResponseChannelDataSelfDataChatmoderatorstrikestatusData

class CurrentUserStrikeStatusResponseChannelData(TypedDict):
	id: str
	self: Union[NoneType, CurrentUserStrikeStatusResponseChannelDataSelfData]

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

class DirectoryCollection_BrowsableCollectionResponseCollectionDataDescriptionData(TypedDict):
	fallbackLocalizedTitle: NoneType

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataPageinfoData(TypedDict):
	hasNextPage: bool

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	roles: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataBroadcasterDataRolesData
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataFreeformtagsData(TypedDict):
	id: str
	name: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	slug: str
	boxArtURL: str
	name: str
	displayName: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str

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

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesData(TypedDict):
	cursor: str
	node: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesDataNodeData
	trackingID: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsData(TypedDict):
	pageInfo: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataPageinfoData
	edges: List[DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesData]

class DirectoryCollection_BrowsableCollectionResponseCollectionData(TypedDict):
	id: str
	slug: str
	name: DirectoryCollection_BrowsableCollectionResponseCollectionDataNameData
	description: DirectoryCollection_BrowsableCollectionResponseCollectionDataDescriptionData
	streams: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsData

class DirectoryCollection_BrowsableCollectionResponse(TypedDict):
	collection: DirectoryCollection_BrowsableCollectionResponseCollectionData

class DirectoryPage_GameRequest1OptionsData1RecommendationscontextData(TypedDict):
	platform: str

class DirectoryPage_GameRequest1OptionsData1(TypedDict):
	includeRestricted: List[str]
	sort: str
	recommendationsContext: DirectoryPage_GameRequest1OptionsData1RecommendationscontextData
	requestID: str
	freeformTags: NoneType
	tags: Falsy[List[Any]]
	broadcasterLanguages: Falsy[List[Any]]
	systemFilters: Falsy[List[Any]]

class DirectoryPage_GameRequest1OptionsData2RecommendationscontextData(TypedDict):
	platform: str

class DirectoryPage_GameRequest1OptionsData2(TypedDict):
	sort: str
	recommendationsContext: DirectoryPage_GameRequest1OptionsData2RecommendationscontextData
	requestID: str
	freeformTags: NoneType
	tags: Falsy[List[Any]]
	broadcasterLanguages: Falsy[List[Any]]
	systemFilters: Falsy[List[Any]]

class DirectoryPage_GameRequest1(TypedDict):
	imageWidth: int
	slug: str
	options: Union[DirectoryPage_GameRequest1OptionsData1, DirectoryPage_GameRequest1OptionsData2]
	sortTypeIsRecency: bool
	limit: int
	includeIsDJ: bool

class DirectoryPage_GameRequest2OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class DirectoryPage_GameRequest2OptionsData(TypedDict):
	sort: str
	recommendationsContext: DirectoryPage_GameRequest2OptionsDataRecommendationscontextData
	requestID: str
	freeformTags: NoneType
	tags: Falsy[List[Any]]
	broadcasterLanguages: Falsy[List[Any]]
	systemFilters: Falsy[List[Any]]

class DirectoryPage_GameRequest2(TypedDict):
	imageWidth: int
	slug: str
	options: DirectoryPage_GameRequest2OptionsData
	sortTypeIsRecency: bool
	limit: int
	includeIsDJ: bool
	cursor: str

class DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool

class DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	roles: DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataBroadcasterDataRolesData
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]

class DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataFreeformtagsData(TypedDict):
	id: str
	name: str

class DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	boxArtURL: str
	name: str
	displayName: str
	slug: str

class DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str

class DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	viewersCount: int
	previewImageURL: str
	broadcaster: DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataBroadcasterData
	freeformTags: List[DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataFreeformtagsData]
	type: str
	game: DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataGameData
	previewThumbnailProperties: DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeDataPreviewthumbnailpropertiesData

class DirectoryPage_GameResponseGameDataStreamsDataEdgesData(TypedDict):
	cursor: str
	node: DirectoryPage_GameResponseGameDataStreamsDataEdgesDataNodeData
	trackingID: str

class DirectoryPage_GameResponseGameDataStreamsDataPageinfoData(TypedDict):
	hasNextPage: bool

class DirectoryPage_GameResponseGameDataStreamsData(TypedDict):
	banners: Union[NoneType, List[str]]
	edges: Falsy[List[DirectoryPage_GameResponseGameDataStreamsDataEdgesData]]
	pageInfo: DirectoryPage_GameResponseGameDataStreamsDataPageinfoData

class DirectoryPage_GameResponseGameData(TypedDict):
	id: str
	name: str
	displayName: str
	streams: DirectoryPage_GameResponseGameDataStreamsData

class DirectoryPage_GameResponse(TypedDict):
	game: DirectoryPage_GameResponseGameData

class DirectoryRoot_DirectoryRequest(TypedDict):
	slug: str

class DirectoryRoot_DirectoryResponseGameData(TypedDict):
	id: str
	name: str
	displayName: str
	slug: str

class DirectoryRoot_DirectoryResponse(TypedDict):
	game: DirectoryRoot_DirectoryResponseGameData

class DirectoryVideos_GameRequest1(TypedDict):
	includePreviewBlur: bool
	slug: str
	videoLimit: int
	languages: Falsy[List[Any]]
	videoSort: str

class DirectoryVideos_GameRequest2(TypedDict):
	includePreviewBlur: bool
	slug: str
	videoLimit: int
	languages: Falsy[List[Any]]
	videoSort: str
	followedCursor: str

class DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str

class DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool

class DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	roles: DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataOwnerDataRolesData

class DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataSelfDataViewinghistoryData(TypedDict):
	position: NoneType
	updatedAt: NoneType

class DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataSelfDataViewinghistoryData

class DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str

class DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeData(TypedDict):
	animatedPreviewURL: str
	game: DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataGameData
	id: str
	lengthSeconds: int
	owner: DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	self: DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataSelfData
	title: str
	viewCount: int
	resourceRestriction: NoneType
	contentTags: Falsy[List[Any]]
	previewThumbnailProperties: DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeDataPreviewthumbnailpropertiesData

class DirectoryVideos_GameResponseGameDataVideosDataEdgesData(TypedDict):
	cursor: Union[NoneType, str]
	node: DirectoryVideos_GameResponseGameDataVideosDataEdgesDataNodeData

class DirectoryVideos_GameResponseGameDataVideosDataPageinfoData(TypedDict):
	hasNextPage: bool

class DirectoryVideos_GameResponseGameDataVideosData(TypedDict):
	banners: NoneType
	edges: List[DirectoryVideos_GameResponseGameDataVideosDataEdgesData]
	pageInfo: DirectoryVideos_GameResponseGameDataVideosDataPageinfoData

class DirectoryVideos_GameResponseGameData(TypedDict):
	id: str
	name: str
	videos: DirectoryVideos_GameResponseGameDataVideosData

class DirectoryVideos_GameResponse(TypedDict):
	game: DirectoryVideos_GameResponseGameData

class DiscoveryPreferenceMutationRequestInputData(TypedDict):
	isPreviewBlurEnabled: bool
	blockedTypes: Falsy[List[Any]]

class DiscoveryPreferenceMutationRequest(TypedDict):
	input: DiscoveryPreferenceMutationRequestInputData

class DiscoveryPreferenceMutationResponseSetdiscoverypreferenceDataPreferenceDataOptionsData(TypedDict):
	type: str
	name: str
	isBlocked: bool

class DiscoveryPreferenceMutationResponseSetdiscoverypreferenceDataPreferenceDataPreviewblurData(TypedDict):
	name: str
	description: str
	isEnabled: bool

class DiscoveryPreferenceMutationResponseSetdiscoverypreferenceDataPreferenceData(TypedDict):
	id: str
	options: List[DiscoveryPreferenceMutationResponseSetdiscoverypreferenceDataPreferenceDataOptionsData]
	previewBlur: DiscoveryPreferenceMutationResponseSetdiscoverypreferenceDataPreferenceDataPreviewblurData

class DiscoveryPreferenceMutationResponseSetdiscoverypreferenceData(TypedDict):
	error: NoneType
	preference: DiscoveryPreferenceMutationResponseSetdiscoverypreferenceDataPreferenceData

class DiscoveryPreferenceMutationResponse(TypedDict):
	setDiscoveryPreference: DiscoveryPreferenceMutationResponseSetdiscoverypreferenceData

class DiscoveryPreferenceQueryRequest(TypedDict):
	...

class DiscoveryPreferenceQueryResponseDiscoverypreferenceDataOptionsData(TypedDict):
	type: str
	name: str
	isBlocked: bool

class DiscoveryPreferenceQueryResponseDiscoverypreferenceDataPreviewblurData(TypedDict):
	name: str
	description: str
	isEnabled: bool

class DiscoveryPreferenceQueryResponseDiscoverypreferenceData(TypedDict):
	id: str
	options: List[DiscoveryPreferenceQueryResponseDiscoverypreferenceDataOptionsData]
	previewBlur: DiscoveryPreferenceQueryResponseDiscoverypreferenceDataPreviewblurData

class DiscoveryPreferenceQueryResponse(TypedDict):
	discoveryPreference: DiscoveryPreferenceQueryResponseDiscoverypreferenceData

class DropCurrentSessionContextRequest(TypedDict):
	channelLogin: str

class DropCurrentSessionContextResponseCurrentuserDataDropcurrentsessionData(TypedDict):
	channel: NoneType
	game: NoneType
	currentMinutesWatched: Falsy[int]
	requiredMinutesWatched: Falsy[int]
	dropID: Falsy[str]

class DropCurrentSessionContextResponseCurrentuserData(TypedDict):
	id: str
	dropCurrentSession: DropCurrentSessionContextResponseCurrentuserDataDropcurrentsessionData

class DropCurrentSessionContextResponse(TypedDict):
	currentUser: Union[NoneType, DropCurrentSessionContextResponseCurrentuserData]

class DropsHighlightService_AvailableDropsRequest(TypedDict):
	channelID: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataGameData(TypedDict):
	id: str
	name: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitDataGameData(TypedDict):
	name: str
	id: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitData(TypedDict):
	id: str
	name: str
	game: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitDataGameData
	imageAssetURL: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesData(TypedDict):
	benefit: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesDataBenefitData
	entitlementLimit: int

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsData(TypedDict):
	id: str
	name: str
	startAt: str
	endAt: str
	benefitEdges: List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataTimebaseddropsDataBenefitedgesData]
	requiredMinutesWatched: int
	requiredSubs: Falsy[int]

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsDataSummaryData(TypedDict):
	includesMWRequirement: bool
	includesSubRequirement: bool
	isSitewide: bool
	isRewardCampaign: bool
	isPermanentlyDismissible: bool

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

class DropsHighlightService_AvailableDropsResponseChannelData(TypedDict):
	id: str
	viewerDropCampaigns: Union[NoneType, List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsData]]

class DropsHighlightService_AvailableDropsResponse(TypedDict):
	channel: DropsHighlightService_AvailableDropsResponseChannelData

class EmotesForChannelFollowStatusRequest(TypedDict):
	channelID: str

class EmotesForChannelFollowStatusResponseUserDataSelfDataFollowerData(TypedDict):
	followedAt: str

class EmotesForChannelFollowStatusResponseUserDataSelfData(TypedDict):
	follower: Union[NoneType, EmotesForChannelFollowStatusResponseUserDataSelfDataFollowerData]

class EmotesForChannelFollowStatusResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, EmotesForChannelFollowStatusResponseUserDataSelfData]

class EmotesForChannelFollowStatusResponse(TypedDict):
	user: EmotesForChannelFollowStatusResponseUserData

class FeaturedContentCarouselStreamsRequest(TypedDict):
	language: str
	first: int
	acceptedMature: bool

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataBroadcasterData(TypedDict):
	displayName: str
	id: str
	profileImageURL: str
	login: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamData(TypedDict):
	broadcaster: FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataBroadcasterData
	game: FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataGameData
	id: str
	type: str
	viewersCount: int
	previewImageURL: str
	freeformTags: List[FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamDataFreeformtagsData]

class FeaturedContentCarouselStreamsResponseFeaturedstreamsData(TypedDict):
	itemTrackingID: str
	isScheduled: bool
	isSponsored: bool
	priorityLevel: int
	description: Falsy[str]
	stream: FeaturedContentCarouselStreamsResponseFeaturedstreamsDataStreamData
	title: Falsy[str]
	version: int

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

class FilterableVideoTower_VideosRequest3OptionsData(TypedDict):
	gameIDs: List[str]

class FilterableVideoTower_VideosRequest3(TypedDict):
	includePreviewBlur: bool
	limit: int
	channelOwnerLogin: str
	broadcastType: str
	videoSort: str
	options: FilterableVideoTower_VideosRequest3OptionsData

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	roles: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataOwnerDataRolesData

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataSelfDataViewinghistoryData(TypedDict):
	position: Union[NoneType, int]
	updatedAt: Union[NoneType, str]

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: Union[NoneType, FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeDataSelfDataViewinghistoryData]

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

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesData(TypedDict):
	cursor: Union[NoneType, str]
	node: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesDataNodeData

class FilterableVideoTower_VideosResponseUserDataVideosDataPageinfoData(TypedDict):
	hasNextPage: bool

class FilterableVideoTower_VideosResponseUserDataVideosData(TypedDict):
	edges: List[FilterableVideoTower_VideosResponseUserDataVideosDataEdgesData]
	pageInfo: FilterableVideoTower_VideosResponseUserDataVideosDataPageinfoData

class FilterableVideoTower_VideosResponseUserData(TypedDict):
	id: str
	videos: FilterableVideoTower_VideosResponseUserDataVideosData

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

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfData(TypedDict):
	canFollow: bool
	follower: FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfDataFollowerData

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfData

class FollowButton_FollowUserResponseFollowuserDataFollowData(TypedDict):
	disableNotifications: bool
	user: FollowButton_FollowUserResponseFollowuserDataFollowDataUserData

class FollowButton_FollowUserResponseFollowuserData(TypedDict):
	follow: FollowButton_FollowUserResponseFollowuserDataFollowData
	error: NoneType

class FollowButton_FollowUserResponse(TypedDict):
	followUser: FollowButton_FollowUserResponseFollowuserData

class FollowButton_UnfollowUserRequestInputData(TypedDict):
	targetID: str

class FollowButton_UnfollowUserRequest(TypedDict):
	input: FollowButton_UnfollowUserRequestInputData

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserDataSelfData(TypedDict):
	canFollow: bool
	follower: NoneType

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserDataSelfData

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowData(TypedDict):
	disableNotifications: bool
	user: FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserData

class FollowButton_UnfollowUserResponseUnfollowuserData(TypedDict):
	follow: FollowButton_UnfollowUserResponseUnfollowuserDataFollowData

class FollowButton_UnfollowUserResponse(TypedDict):
	unfollowUser: FollowButton_UnfollowUserResponseUnfollowuserData

class FollowButton_UserRequest(TypedDict):
	login: str

class FollowButton_UserResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool
	followedAt: str

class FollowButton_UserResponseUserDataSelfData(TypedDict):
	canFollow: bool
	follower: Union[NoneType, FollowButton_UserResponseUserDataSelfDataFollowerData]

class FollowButton_UserResponseUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: Union[NoneType, FollowButton_UserResponseUserDataSelfData]

class FollowButton_UserResponse(TypedDict):
	user: FollowButton_UserResponseUserData

class FollowedIndex_CurrentUserRequest(TypedDict):
	...

class FollowedIndex_CurrentUserResponseCurrentuserData(TypedDict):
	id: str

class FollowedIndex_CurrentUserResponse(TypedDict):
	currentUser: FollowedIndex_CurrentUserResponseCurrentuserData

class FollowedIndex_FollowCountRequest(TypedDict):
	...

class FollowedIndex_FollowCountResponseCurrentuserDataFollowsData(TypedDict):
	totalCount: int

class FollowedIndex_FollowCountResponseCurrentuserData(TypedDict):
	id: str
	follows: FollowedIndex_FollowCountResponseCurrentuserDataFollowsData

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

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerDataSubscriptionproductsData(TypedDict):
	id: str
	emotes: Falsy[List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerDataSubscriptionproductsDataEmotesData]]

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerData(TypedDict):
	id: str
	displayName: str
	login: str
	isPartner: bool
	profileImageURL: str
	primaryColorHex: str
	bannerImageURL: str
	subscriptionProducts: List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerDataSubscriptionproductsData]

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelData(TypedDict):
	id: str
	owner: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelDataOwnerData

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	startAt: str
	categories: Falsy[List[Any]]
	hasReminder: bool
	baseSegmentID: str
	repeatEndsAfterCount: Falsy[int]
	channel: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeDataChannelData

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesData(TypedDict):
	node: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesDataNodeData

class FollowedStreamsResponseFollowedupcomingstreamsData(TypedDict):
	edges: List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesData]

class FollowedStreamsResponse(TypedDict):
	followedUpcomingStreams: FollowedStreamsResponseFollowedupcomingstreamsData

class FollowedStreamsContinueWatchingRequest(TypedDict):
	includePreviewBlur: bool
	limit: int

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData(TypedDict):
	position: Falsy[int]
	updatedAt: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	roles: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataOwnerDataRolesData

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData(TypedDict):
	position: Falsy[int]
	updatedAt: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData

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

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesData(TypedDict):
	history: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData
	node: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesDataNodeData

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosData(TypedDict):
	edges: List[FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesData]

class FollowedStreamsContinueWatchingResponseCurrentuserData(TypedDict):
	id: str
	viewedVideos: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosData

class FollowedStreamsContinueWatchingResponse(TypedDict):
	currentUser: FollowedStreamsContinueWatchingResponseCurrentuserData

class FollowedVideos_CurrentUserRequest(TypedDict):
	includePreviewBlur: bool
	limit: int

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowsData(TypedDict):
	totalCount: int

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataPageinfoData(TypedDict):
	hasNextPage: bool

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataGameData(TypedDict):
	boxArtURL: str
	id: str
	slug: str
	displayName: str
	name: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataOwnerDataRolesData(TypedDict):
	isPartner: bool

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataOwnerData(TypedDict):
	displayName: str
	id: str
	login: str
	profileImageURL: str
	primaryColorHex: str
	roles: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataOwnerDataRolesData

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData(TypedDict):
	position: Union[NoneType, int]
	updatedAt: Union[NoneType, str]

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataSelfData(TypedDict):
	isRestricted: bool
	viewingHistory: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeDataSelfDataViewinghistoryData

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

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesData(TypedDict):
	cursor: str
	node: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesDataNodeData

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosData(TypedDict):
	pageInfo: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataPageinfoData
	edges: List[FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesData]

class FollowedVideos_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	follows: FollowedVideos_CurrentUserResponseCurrentuserDataFollowsData
	followedVideos: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosData

class FollowedVideos_CurrentUserResponse(TypedDict):
	currentUser: FollowedVideos_CurrentUserResponseCurrentuserData

class FollowGameButton_GameRequest(TypedDict):
	slug: str

class FollowGameButton_GameResponseGameDataSelfData(TypedDict):
	follow: NoneType

class FollowGameButton_GameResponseGameData(TypedDict):
	id: str
	name: str
	self: FollowGameButton_GameResponseGameDataSelfData

class FollowGameButton_GameResponseCurrentuserData(TypedDict):
	id: str

class FollowGameButton_GameResponse(TypedDict):
	game: FollowGameButton_GameResponseGameData
	currentUser: FollowGameButton_GameResponseCurrentuserData

class FollowingGames_CurrentUserRequest(TypedDict):
	limit: int
	type: str

class FollowingGames_CurrentUserResponseCurrentuserDataFollowedgamesData(TypedDict):
	nodes: Falsy[List[Any]]

class FollowingGames_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	followedGames: FollowingGames_CurrentUserResponseCurrentuserDataFollowedgamesData

class FollowingGames_CurrentUserResponse(TypedDict):
	currentUser: FollowingGames_CurrentUserResponseCurrentuserData

class FollowingLive_CurrentUserRequest(TypedDict):
	imageWidth: int
	limit: int
	includeIsDJ: bool

class FollowingLive_CurrentUserResponseCurrentuserDataFollowsData(TypedDict):
	totalCount: int

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str
	boxArtURL: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelDataSelfData(TypedDict):
	isAuthorized: bool

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelData(TypedDict):
	id: str
	self: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelDataSelfData

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterData(TypedDict):
	id: str
	primaryColorHex: str
	roles: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataRolesData
	channel: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamDataBroadcasterDataChannelData

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

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	stream: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeDataStreamData

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesData(TypedDict):
	node: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesDataNodeData
	cursor: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataPageinfoData(TypedDict):
	hasNextPage: bool

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersData(TypedDict):
	edges: List[FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesData]
	pageInfo: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataPageinfoData

class FollowingLive_CurrentUserResponseCurrentuserData(TypedDict):
	id: str
	follows: FollowingLive_CurrentUserResponseCurrentuserDataFollowsData
	followedLiveUsers: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersData

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

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterDataRolesData(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterData(TypedDict):
	id: str
	broadcastSettings: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterDataBroadcastsettingsData
	displayName: str
	login: str
	profileImageURL: str
	largeProfileImageURL: str
	primaryColorHex: Union[NoneType, str]
	roles: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterDataRolesData

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameDataGametagsData(TypedDict):
	id: str
	isLanguageTag: bool
	localizedName: str
	tagName: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	categorySlug: str
	name: str
	viewersCount: int
	displayName: str
	boxArtURL: str
	gameTags: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameDataGametagsData]
	originalReleaseDate: Union[NoneType, str]

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataFreeformtagsData(TypedDict):
	id: str
	name: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataPreviewthumbnailpropertiesData(TypedDict):
	blurReason: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeData(TypedDict):
	id: str
	broadcaster: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataBroadcasterData
	game: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataGameData
	freeformTags: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataFreeformtagsData]
	viewersCount: int
	previewImageURL: str
	createdAt: str
	type: str
	previewThumbnailProperties: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeDataPreviewthumbnailpropertiesData

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesData(TypedDict):
	node: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesDataNodeData
	trackingID: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsData(TypedDict):
	edges: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesData]

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsData(TypedDict):
	liveRecommendations: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsData

class FollowingPage_RecommendedChannelsResponseCurrentuserData(TypedDict):
	id: str
	recommendations: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsData

class FollowingPage_RecommendedChannelsResponse(TypedDict):
	currentUser: FollowingPage_RecommendedChannelsResponseCurrentuserData

class FrontPageNew_UserRequest(TypedDict):
	limit: int

class FrontPageNew_UserResponseCurrentuserDataFollowedgamesData(TypedDict):
	nodes: Falsy[List[Any]]

class FrontPageNew_UserResponseCurrentuserDataRolesData(TypedDict):
	isPartner: bool
	isStaff: NoneType

class FrontPageNew_UserResponseCurrentuserData(TypedDict):
	id: str
	createdAt: str
	followedGames: FrontPageNew_UserResponseCurrentuserDataFollowedgamesData
	roles: FrontPageNew_UserResponseCurrentuserDataRolesData

class FrontPageNew_UserResponse(TypedDict):
	currentUser: Union[NoneType, FrontPageNew_UserResponseCurrentuserData]

class GetDisplayNameRequest(TypedDict):
	login: Falsy[str]

class GetDisplayNameResponseUserData(TypedDict):
	id: str
	login: str
	displayName: str

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

class GetGuestSessionBlocksAndBansResponseUserData(TypedDict):
	id: str
	self: GetGuestSessionBlocksAndBansResponseUserDataSelfData

class GetGuestSessionBlocksAndBansResponse(TypedDict):
	user: GetGuestSessionBlocksAndBansResponseUserData
	guestStarSession: NoneType

class GetHypeTrainExecutionV2Request(TypedDict):
	userLogin: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressDataLevelDataRewardsDataEmoteData(TypedDict):
	id: str
	token: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressDataLevelDataRewardsData(TypedDict):
	id: str
	type: str
	emote: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressDataLevelDataRewardsDataEmoteData

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressDataLevelData(TypedDict):
	id: str
	value: int
	goal: int
	rewards: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressDataLevelDataRewardsData]

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressData(TypedDict):
	id: str
	level: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressDataLevelData
	goal: int
	progression: int
	total: int
	allTimeHighState: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConductorsDataParticipationData(TypedDict):
	source: str
	action: str
	quantity: int

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConductorsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConductorsData(TypedDict):
	id: str
	source: str
	participation: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConductorsDataParticipationData]
	user: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConductorsDataUserData

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataDifficultysettingsData(TypedDict):
	difficulty: str
	maxLevel: int

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataConductorrewardsDataRewardsDataBadgeData(TypedDict):
	id: str
	setID: str
	imageURL: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataConductorrewardsDataRewardsData(TypedDict):
	id: str
	type: str
	badge: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataConductorrewardsDataRewardsDataBadgeData

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataConductorrewardsData(TypedDict):
	source: str
	type: str
	rewards: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataConductorrewardsDataRewardsData]

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataParticipationconversionratesData(TypedDict):
	action: str
	source: str
	value: Falsy[int]

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataCalloutemoteData(TypedDict):
	id: str
	token: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataPotentialrewardsDataValueDataEmoteData(TypedDict):
	id: str
	token: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataPotentialrewardsDataValueData(TypedDict):
	id: str
	type: str
	emote: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataPotentialrewardsDataValueDataEmoteData

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataPotentialrewardsData(TypedDict):
	id: str
	level: int
	value: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataPotentialrewardsDataValueData

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataKickoffData(TypedDict):
	minPoints: int

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigData(TypedDict):
	id: str
	difficulty: str
	difficultySettings: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataDifficultysettingsData]
	conductorRewards: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataConductorrewardsData]
	participationConversionRates: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataParticipationconversionratesData]
	calloutEmote: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataCalloutemoteData
	willUseCreatorColor: bool
	primaryHexColor: NoneType
	potentialRewards: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataPotentialrewardsData]
	kickoff: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigDataKickoffData

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataAlltimehighDataLevelData(TypedDict):
	id: str
	value: int

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataAlltimehighData(TypedDict):
	level: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataAlltimehighDataLevelData
	goal: int
	progression: int
	total: int

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataParticipationsData(TypedDict):
	action: str
	quantity: int
	source: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataSelfData(TypedDict):
	isEligibleForRewards: bool

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionData(TypedDict):
	id: str
	startedAt: str
	expiresAt: str
	updatedAt: str
	endedAt: NoneType
	endReason: NoneType
	progress: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataProgressData
	conductors: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConductorsData]
	config: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataConfigData
	allTimeHigh: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataAlltimehighData
	participations: List[GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataParticipationsData]
	isGoldenKappaTrain: bool
	isFastMode: bool
	self: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionDataSelfData

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainData(TypedDict):
	execution: Union[NoneType, GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainDataExecutionData]
	approaching: NoneType

class GetHypeTrainExecutionV2ResponseUserDataChannelData(TypedDict):
	id: str
	hypeTrain: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainData

class GetHypeTrainExecutionV2ResponseUserData(TypedDict):
	id: str
	displayName: str
	channel: GetHypeTrainExecutionV2ResponseUserDataChannelData

class GetHypeTrainExecutionV2Response(TypedDict):
	user: GetHypeTrainExecutionV2ResponseUserData

class GetIDFromLoginRequest(TypedDict):
	login: str

class GetIDFromLoginResponseUserData(TypedDict):
	id: str

class GetIDFromLoginResponse(TypedDict):
	user: GetIDFromLoginResponseUserData

class GetPinnedChatRequest(TypedDict):
	channelID: str
	count: int

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsDataContentData(TypedDict):
	emoteID: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsData(TypedDict):
	content: Union[NoneType, GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsDataContentData]
	text: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentData(TypedDict):
	text: str
	fragments: List[GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentDataFragmentsData]

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderDataDisplaybadgesData(TypedDict):
	id: str
	setID: str
	version: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderData(TypedDict):
	id: str
	chatColor: Union[NoneType, str]
	displayName: str
	displayBadges: List[GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderDataDisplaybadgesData]

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageData(TypedDict):
	id: str
	content: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataContentData
	parentMessage: NoneType
	threadParentMessage: NoneType
	sentAt: str
	sender: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageDataSenderData

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedbyData(TypedDict):
	id: str
	displayName: str

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeData(TypedDict):
	id: str
	type: str
	pinnedMessage: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedmessageData
	startsAt: str
	updatedAt: str
	endsAt: NoneType
	pinnedBy: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeDataPinnedbyData

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesData(TypedDict):
	node: GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesDataNodeData
	cursor: Falsy[str]

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData(TypedDict):
	hasNextPage: bool

class GetPinnedChatResponseChannelDataPinnedchatmessagesData(TypedDict):
	edges: Falsy[List[GetPinnedChatResponseChannelDataPinnedchatmessagesDataEdgesData]]
	pageInfo: GetPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData

class GetPinnedChatResponseChannelData(TypedDict):
	id: str
	pinnedChatMessages: GetPinnedChatResponseChannelDataPinnedchatmessagesData

class GetPinnedChatResponse(TypedDict):
	channel: GetPinnedChatResponseChannelData

class GetUserIDRequest(TypedDict):
	login: str
	lookupType: str

class GetUserIDResponseUserData(TypedDict):
	id: str

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

class GlobalBadgesResponse(TypedDict):
	badges: List[GlobalBadgesResponseBadgesData]

class GuestListQueryRequest(TypedDict):
	channelID: str

class GuestListQueryResponseChannelData(TypedDict):
	id: str
	guestStarSessionCall: NoneType

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
	primaryColorHex: Union[NoneType, str]
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: int
	viewersCount: int
	id: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	description: str
	stream: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsDataUserData

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionDataGuestsData]

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData1SessionData]
	canJoinStatus: str
	isFavorite: bool

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: Union[NoneType, int]
	viewersCount: int
	id: str

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	description: Union[NoneType, Falsy[str]]
	stream: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsDataUserData

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionDataGuestsData]

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationData2SessionData]
	canDropIn: bool
	canJoinStatus: str
	isFavorite: bool

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: int
	viewersCount: int
	id: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	description: str
	stream: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsDataUserData

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionDataGuestsData]

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1SessionData]
	canJoinStatus: str
	isFavorite: bool

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataHostData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	description: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserDataStreamData(TypedDict):
	collaborationViewersCount: Union[NoneType, int]
	viewersCount: int
	id: str

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str
	primaryColorHex: Union[NoneType, str]
	description: Union[NoneType, Falsy[str]]
	stream: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserDataStreamData

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsData(TypedDict):
	id: str
	slotID: str
	user: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsDataUserData

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionData(TypedDict):
	id: str
	host: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataHostData
	guests: List[GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionDataGuestsData]

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2(TypedDict):
	id: str
	session: Union[NoneType, GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2SessionData]
	canDropIn: bool
	canJoinStatus: str
	isFavorite: bool

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesData(TypedDict):
	shouldRefetch: bool
	shouldSubscribeToUpdates: bool
	channelCollabs: Falsy[List[Union[GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData1, GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData2]]]

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

class GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesData(TypedDict):
	shouldRefetch: bool
	shouldSubscribeToUpdates: bool
	channelCollabs: List[GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsData]

class GuestStarChannelPageCollaborationQueryResponse(TypedDict):
	guestStarCollaborationStatuses: GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesData

class HappeningNowSettingsRequest(TypedDict):
	...

class HappeningNowSettingsResponseCurrentuserData(TypedDict):
	id: str
	isChatHappeningNowEnabled: bool

class HappeningNowSettingsResponse(TypedDict):
	currentUser: HappeningNowSettingsResponseCurrentuserData

class HomeOfflineCarouselRequest(TypedDict):
	channelLogin: str
	includeTrailerUpsell: bool
	trailerUpsellVideoID: str

class HomeOfflineCarouselResponseUserDataChannelDataHomeData(TypedDict):
	autohostCarouselCard: NoneType

class HomeOfflineCarouselResponseUserDataChannelDataSocialmediasData(TypedDict):
	id: str
	name: str
	title: str
	url: str

class HomeOfflineCarouselResponseUserDataChannelDataScheduleDataNextsegmentData(TypedDict):
	id: str
	startAt: str

class HomeOfflineCarouselResponseUserDataChannelDataScheduleData(TypedDict):
	id: str
	nextSegment: Union[NoneType, HomeOfflineCarouselResponseUserDataChannelDataScheduleDataNextsegmentData]

class HomeOfflineCarouselResponseUserDataChannelDataTrailerData(TypedDict):
	video: NoneType

class HomeOfflineCarouselResponseUserDataChannelData(TypedDict):
	id: str
	home: HomeOfflineCarouselResponseUserDataChannelDataHomeData
	socialMedias: Falsy[List[HomeOfflineCarouselResponseUserDataChannelDataSocialmediasData]]
	schedule: Union[NoneType, HomeOfflineCarouselResponseUserDataChannelDataScheduleData]
	trailer: HomeOfflineCarouselResponseUserDataChannelDataTrailerData

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str
	displayName: str

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	description: NoneType
	previewThumbnailURL: str
	publishedAt: str
	owner: HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataOwnerData
	game: HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeDataGameData

class HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesData(TypedDict):
	node: HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesDataNodeData

class HomeOfflineCarouselResponseUserDataArchivevideosData(TypedDict):
	edges: Falsy[List[HomeOfflineCarouselResponseUserDataArchivevideosDataEdgesData]]

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str
	displayName: str

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	description: NoneType
	previewThumbnailURL: str
	publishedAt: str
	owner: HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataOwnerData
	game: HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeDataGameData

class HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesData(TypedDict):
	node: HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesDataNodeData

class HomeOfflineCarouselResponseUserDataHighlightvideosData(TypedDict):
	edges: Falsy[List[HomeOfflineCarouselResponseUserDataHighlightvideosDataEdgesData]]

class HomeOfflineCarouselResponseUserDataRolesData(TypedDict):
	isPartner: bool
	isAffiliate: bool
	isStaff: NoneType

class HomeOfflineCarouselResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool

class HomeOfflineCarouselResponseUserDataSelfData(TypedDict):
	isEditor: bool
	follower: Union[NoneType, HomeOfflineCarouselResponseUserDataSelfDataFollowerData]
	subscriptionBenefit: NoneType

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

class HomeOfflineCarouselResponse(TypedDict):
	user: HomeOfflineCarouselResponseUserData

class incrementClipViewCountRequestInputData(TypedDict):
	slug: str

class incrementClipViewCountRequest(TypedDict):
	input: incrementClipViewCountRequestInputData

class incrementClipViewCountResponseUpdateclipviewcountDataClipData(TypedDict):
	id: str

class incrementClipViewCountResponseUpdateclipviewcountData(TypedDict):
	clip: incrementClipViewCountResponseUpdateclipviewcountDataClipData

class incrementClipViewCountResponse(TypedDict):
	updateClipViewCount: incrementClipViewCountResponseUpdateclipviewcountData

class LastUnbanRequestRequest(TypedDict):
	channelID: str
	includeCanRequestUnban: bool

class LastUnbanRequestResponseChannelDataSelfData(TypedDict):
	lastUnbanRequest: NoneType

class LastUnbanRequestResponseChannelData(TypedDict):
	id: str
	self: LastUnbanRequestResponseChannelDataSelfData

class LastUnbanRequestResponse(TypedDict):
	channel: LastUnbanRequestResponseChannelData

class LowerHomeHeaderRequest(TypedDict):
	channelLogin: str

class LowerHomeHeaderResponseUserDataSelfData(TypedDict):
	isEditor: bool

class LowerHomeHeaderResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, LowerHomeHeaderResponseUserDataSelfData]

class LowerHomeHeaderResponse(TypedDict):
	user: LowerHomeHeaderResponseUserData

class MessageBuffer_ChannelRequest(TypedDict):
	channelLogin: str

class MessageBuffer_ChannelResponseUserDataChatsettingsData(TypedDict):
	chatDelayMs: Falsy[int]

class MessageBuffer_ChannelResponseUserData(TypedDict):
	id: str
	chatSettings: MessageBuffer_ChannelResponseUserDataChatsettingsData

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

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData2(TypedDict):
	id: str
	login: str
	displayName: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData3(TypedDict):
	bitsAmount: int
	prefix: str
	tier: int

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsData(TypedDict):
	text: str
	content: Union[NoneType, Union[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData1, MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData2, MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsDataContentData3]]

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentData(TypedDict):
	text: str
	fragments: List[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataContentDataFragmentsData]

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataContentData(TypedDict):
	text: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataSenderData(TypedDict):
	id: str
	login: str
	displayName: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageData(TypedDict):
	id: str
	content: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataContentData
	deletedAt: NoneType
	sender: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataParentmessageDataSenderData

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataThreadparentmessageDataSenderData(TypedDict):
	id: str
	login: str
	displayName: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataThreadparentmessageData(TypedDict):
	id: str
	deletedAt: NoneType
	sender: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataThreadparentmessageDataSenderData

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataSenderData(TypedDict):
	id: str
	login: str
	displayName: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesDataSenderbadgesData(TypedDict):
	setID: str
	version: str
	id: str

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

class MessageBufferChatHistoryResponseChannelData(TypedDict):
	id: str
	recentChatMessages: Falsy[List[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesData]]

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

class NielsenContentMetadataResponse1UserDataStreamDataGameData(TypedDict):
	id: str
	displayName: str

class NielsenContentMetadataResponse1UserDataStreamData(TypedDict):
	id: str
	createdAt: str
	game: NielsenContentMetadataResponse1UserDataStreamDataGameData

class NielsenContentMetadataResponse1UserData(TypedDict):
	id: str
	broadcastSettings: NielsenContentMetadataResponse1UserDataBroadcastsettingsData
	stream: Union[NoneType, NielsenContentMetadataResponse1UserDataStreamData]

class NielsenContentMetadataResponse1(TypedDict):
	user: NielsenContentMetadataResponse1UserData

class NielsenContentMetadataResponse2VideoDataGameData(TypedDict):
	id: str
	displayName: str

class NielsenContentMetadataResponse2VideoDataOwnerData(TypedDict):
	id: str
	login: str

class NielsenContentMetadataResponse2VideoData(TypedDict):
	id: str
	createdAt: str
	title: str
	game: NielsenContentMetadataResponse2VideoDataGameData
	owner: NielsenContentMetadataResponse2VideoDataOwnerData

class NielsenContentMetadataResponse2(TypedDict):
	video: NielsenContentMetadataResponse2VideoData

class OneClickEligibilityRequest(TypedDict):
	walletType: str

class OneClickEligibilityResponseRequestinfoData(TypedDict):
	countryCode: str

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

class OneClickEligibilityResponseCurrentuserDataWalletbalancesDataAllbalancesData(TypedDict):
	amount: Falsy[int]
	currency: str
	expiresAt: NoneType
	exponent: int

class OneClickEligibilityResponseCurrentuserDataWalletbalancesData(TypedDict):
	allBalances: List[OneClickEligibilityResponseCurrentuserDataWalletbalancesDataAllbalancesData]

class OneClickEligibilityResponseCurrentuserData(TypedDict):
	id: str
	paymentMethods: List[OneClickEligibilityResponseCurrentuserDataPaymentmethodsData]
	walletBalances: OneClickEligibilityResponseCurrentuserDataWalletbalancesData
	residence: NoneType

class OneClickEligibilityResponseRecurlyconfigsDataPaywithamazonconfigsData(TypedDict):
	clientID: str
	isProduction: bool
	sellerID: str

class OneClickEligibilityResponseRecurlyconfigsData(TypedDict):
	payWithAmazonConfigs: OneClickEligibilityResponseRecurlyconfigsDataPaywithamazonconfigsData
	braintreeClientAuthorization: str
	publicKey: str

class OneClickEligibilityResponse(TypedDict):
	requestInfo: OneClickEligibilityResponseRequestinfoData
	currentUser: Union[NoneType, OneClickEligibilityResponseCurrentuserData]
	recurlyConfigs: OneClickEligibilityResponseRecurlyconfigsData

class OneTapFeedRequest(TypedDict):
	channelID: str

class OneTapFeedResponseOnetapfeedData(TypedDict):
	items: Falsy[List[Any]]

class OneTapFeedResponse(TypedDict):
	oneTapFeed: OneTapFeedResponseOnetapfeedData

class PaidPinnedChatRequest(TypedDict):
	channelID: str
	count: int
	messageType: str

class PaidPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData(TypedDict):
	hasNextPage: bool

class PaidPinnedChatResponseChannelDataPinnedchatmessagesData(TypedDict):
	edges: Falsy[List[Any]]
	pageInfo: PaidPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData

class PaidPinnedChatResponseChannelData(TypedDict):
	id: str
	pinnedChatMessages: PaidPinnedChatResponseChannelDataPinnedchatmessagesData

class PaidPinnedChatResponse(TypedDict):
	channel: PaidPinnedChatResponseChannelData

class PbyPGameRequest(TypedDict):
	channelLogin: str
	tagType: str

class PbyPGameResponseUserDataStreamDataGameDataTagsData(TypedDict):
	id: str
	tagName: str

class PbyPGameResponseUserDataStreamDataGameData(TypedDict):
	id: str
	name: str
	tags: List[PbyPGameResponseUserDataStreamDataGameDataTagsData]

class PbyPGameResponseUserDataStreamData(TypedDict):
	id: str
	game: PbyPGameResponseUserDataStreamDataGameData

class PbyPGameResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, PbyPGameResponseUserDataStreamData]

class PbyPGameResponse(TypedDict):
	user: PbyPGameResponseUserData

class PersistentGoalFollowButton_UserRequest(TypedDict):
	login: str

class PersistentGoalFollowButton_UserResponseUserDataSelfDataFollowerData(TypedDict):
	disableNotifications: bool
	followedAt: str

class PersistentGoalFollowButton_UserResponseUserDataSelfData(TypedDict):
	canFollow: bool
	follower: Union[NoneType, PersistentGoalFollowButton_UserResponseUserDataSelfDataFollowerData]

class PersistentGoalFollowButton_UserResponseUserData(TypedDict):
	id: str
	displayName: str
	login: str
	self: Union[NoneType, PersistentGoalFollowButton_UserResponseUserDataSelfData]

class PersistentGoalFollowButton_UserResponse(TypedDict):
	user: PersistentGoalFollowButton_UserResponseUserData

class PersonalSectionsHypeTrainsRequest(TypedDict):
	channelIDs: List[str]

class PersonalSectionsHypeTrainsResponseActivehypetrainstatusesDataChannelData(TypedDict):
	id: str

class PersonalSectionsHypeTrainsResponseActivehypetrainstatusesData(TypedDict):
	id: str
	channel: PersonalSectionsHypeTrainsResponseActivehypetrainstatusesDataChannelData
	level: int
	isGoldenKappaTrain: bool
	isAllTimeHighTrain: bool

class PersonalSectionsHypeTrainsResponse(TypedDict):
	activeHypeTrainStatuses: List[PersonalSectionsHypeTrainsResponseActivehypetrainstatusesData]

class PinnedChatSettingsRequest(TypedDict):
	channelID: str

class PinnedChatSettingsResponseChannelDataPinnedchatsettingsData(TypedDict):
	isModAccessEnabled: bool

class PinnedChatSettingsResponseChannelData(TypedDict):
	id: str
	pinnedChatSettings: Union[NoneType, PinnedChatSettingsResponseChannelDataPinnedchatsettingsData]

class PinnedChatSettingsResponse(TypedDict):
	channel: PinnedChatSettingsResponseChannelData

class PinnedCheersSettingsRequest(TypedDict):
	login: str

class PinnedCheersSettingsResponseUserDataCheerDataSettingsData(TypedDict):
	id: str
	isPinnedCheersEnabled: bool

class PinnedCheersSettingsResponseUserDataCheerData(TypedDict):
	id: str
	settings: PinnedCheersSettingsResponseUserDataCheerDataSettingsData

class PinnedCheersSettingsResponseUserData(TypedDict):
	id: str
	cheer: Union[NoneType, PinnedCheersSettingsResponseUserDataCheerData]

class PinnedCheersSettingsResponse(TypedDict):
	user: PinnedCheersSettingsResponseUserData

class PlaybackAccessTokenRequest(TypedDict):
	isLive: bool
	login: Falsy[str]
	isVod: bool
	vodID: Falsy[str]
	playerType: str
	platform: str

class PlaybackAccessTokenResponse1VideoplaybackaccesstokenData(TypedDict):
	value: str
	signature: str

class PlaybackAccessTokenResponse1(TypedDict):
	videoPlaybackAccessToken: PlaybackAccessTokenResponse1VideoplaybackaccesstokenData

class PlaybackAccessTokenResponse2StreamplaybackaccesstokenDataAuthorizationData(TypedDict):
	isForbidden: bool
	forbiddenReasonCode: str

class PlaybackAccessTokenResponse2StreamplaybackaccesstokenData(TypedDict):
	value: str
	signature: str
	authorization: PlaybackAccessTokenResponse2StreamplaybackaccesstokenDataAuthorizationData

class PlaybackAccessTokenResponse2(TypedDict):
	streamPlaybackAccessToken: PlaybackAccessTokenResponse2StreamplaybackaccesstokenData

class PollChannelSettingsRequest(TypedDict):
	channelLogin: str

class PollChannelSettingsResponsePollchannelsettingsData(TypedDict):
	hasPollsAccess: bool

class PollChannelSettingsResponse(TypedDict):
	pollChannelSettings: PollChannelSettingsResponsePollchannelsettingsData

class PrefetchPlaybackAccessTokenRequest(TypedDict):
	login: str
	playerType: str
	platform: str

class PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenDataAuthorizationData(TypedDict):
	isForbidden: bool
	forbiddenReasonCode: str

class PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenData(TypedDict):
	value: str
	signature: str
	expiresAt: str
	authorization: PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenDataAuthorizationData

class PrefetchPlaybackAccessTokenResponse(TypedDict):
	streamPlaybackAccessToken: PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenData

class ProfileImageSettingRequest(TypedDict):
	...

class ProfileImageSettingResponseCurrentuserData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str

class ProfileImageSettingResponse(TypedDict):
	currentUser: ProfileImageSettingResponseCurrentuserData

class queryUserViewedVideoRequest(TypedDict):
	...

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataNodeData(TypedDict):
	id: str

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData(TypedDict):
	position: Falsy[int]

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesData(TypedDict):
	node: queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataNodeData
	history: queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesDataHistoryData

class queryUserViewedVideoResponseCurrentuserDataViewedvideosData(TypedDict):
	edges: List[queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesData]

class queryUserViewedVideoResponseCurrentuserData(TypedDict):
	id: str
	viewedVideos: queryUserViewedVideoResponseCurrentuserDataViewedvideosData

class queryUserViewedVideoResponse(TypedDict):
	currentUser: queryUserViewedVideoResponseCurrentuserData

class RealtimeStreamTagListRequest(TypedDict):
	channelLogin: str

class RealtimeStreamTagListResponseUserDataStreamDataFreeformtagsData(TypedDict):
	id: str
	name: str

class RealtimeStreamTagListResponseUserDataStreamData(TypedDict):
	id: str
	freeformTags: List[RealtimeStreamTagListResponseUserDataStreamDataFreeformtagsData]

class RealtimeStreamTagListResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, RealtimeStreamTagListResponseUserDataStreamData]

class RealtimeStreamTagListResponse(TypedDict):
	user: RealtimeStreamTagListResponseUserData

class RecapEligibilityQueryRequest(TypedDict):
	channelLogin: str

class RecapEligibilityQueryResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType
	banStatus: NoneType

class RecapEligibilityQueryResponseUserDataRolesData(TypedDict):
	isAffiliate: bool
	isPartner: bool

class RecapEligibilityQueryResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, RecapEligibilityQueryResponseUserDataSelfData]
	roles: RecapEligibilityQueryResponseUserDataRolesData

class RecapEligibilityQueryResponse(TypedDict):
	user: RecapEligibilityQueryResponseUserData

class RoleRestrictedRequest(TypedDict):
	contentOwnerLogin: str

class RoleRestrictedResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType

class RoleRestrictedResponseCurrentuserData(TypedDict):
	id: str
	roles: RoleRestrictedResponseCurrentuserDataRolesData

class RoleRestrictedResponseUserDataSelfData(TypedDict):
	isEditor: bool

class RoleRestrictedResponseUserData(TypedDict):
	id: str
	self: RoleRestrictedResponseUserDataSelfData

class RoleRestrictedResponse(TypedDict):
	currentUser: RoleRestrictedResponseCurrentuserData
	user: RoleRestrictedResponseUserData

class Settings_ProfilePage_AccountInfoSettingsRequest(TypedDict):
	...

class Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserDataSettingsData(TypedDict):
	preferredLanguageTag: str

class Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserData(TypedDict):
	id: str
	description: NoneType
	displayName: str
	isEmailVerified: bool
	login: str
	settings: Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserDataSettingsData

class Settings_ProfilePage_AccountInfoSettingsResponse(TypedDict):
	currentUser: Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserData

class ShareClipRenderStatusRequest(TypedDict):
	slug: str

class ShareClipRenderStatusResponseClipDataAssetsDataCuratorData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str

class ShareClipRenderStatusResponseClipDataAssetsDataVideoqualitiesData(TypedDict):
	frameRate: Union[float, int]
	quality: str
	sourceURL: str

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataTopleftData(TypedDict):
	xPercentage: Union[Falsy[int], float]
	yPercentage: float

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: float

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeDataBottomrightData

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataTopleftData(TypedDict):
	xPercentage: float
	yPercentage: Falsy[int]

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: Union[int, float]

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeDataBottomrightData

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataData(TypedDict):
	topFrame: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataTopframeData
	bottomFrame: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataDataBottomframeData

class ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataData(TypedDict):
	portraitClipLayout: str
	fullTemplateMetadata: NoneType
	stackedTemplateMetadata: ShareClipRenderStatusResponseClipDataAssetsDataPortraitmetadataDataStackedtemplatemetadataData

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

class ShareClipRenderStatusResponseClipDataCuratorData(TypedDict):
	id: str
	login: str
	displayName: str
	profileImageURL: str

class ShareClipRenderStatusResponseClipDataGameData(TypedDict):
	id: str
	name: str
	boxArtURL: str
	displayName: str
	slug: str

class ShareClipRenderStatusResponseClipDataBroadcastData(TypedDict):
	id: str
	title: NoneType

class ShareClipRenderStatusResponseClipDataBroadcasterDataFollowersData(TypedDict):
	totalCount: int

class ShareClipRenderStatusResponseClipDataBroadcasterDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str

class ShareClipRenderStatusResponseClipDataBroadcasterDataSelfData(TypedDict):
	isEditor: bool

class ShareClipRenderStatusResponseClipDataBroadcasterData(TypedDict):
	id: str
	login: str
	displayName: str
	primaryColorHex: Union[NoneType, str]
	isPartner: bool
	profileImageURL: str
	followers: ShareClipRenderStatusResponseClipDataBroadcasterDataFollowersData
	stream: NoneType
	lastBroadcast: ShareClipRenderStatusResponseClipDataBroadcasterDataLastbroadcastData
	self: Union[NoneType, ShareClipRenderStatusResponseClipDataBroadcasterDataSelfData]

class ShareClipRenderStatusResponseClipDataPlaybackaccesstokenData(TypedDict):
	signature: str
	value: str

class ShareClipRenderStatusResponseClipDataVideoData(TypedDict):
	id: str
	broadcastType: str
	title: str

class ShareClipRenderStatusResponseClipDataVideoqualitiesData(TypedDict):
	sourceURL: str

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData(TypedDict):
	xPercentage: float
	yPercentage: Falsy[int]

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: int

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataData(TypedDict):
	mainFrame: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataTopframeDataTopleftData(TypedDict):
	xPercentage: Falsy[int]
	yPercentage: float

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataTopframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: float

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataTopframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataTopframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataTopframeDataBottomrightData

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataBottomframeDataTopleftData(TypedDict):
	xPercentage: float
	yPercentage: Falsy[int]

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataBottomframeDataBottomrightData(TypedDict):
	xPercentage: float
	yPercentage: int

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataBottomframeData(TypedDict):
	topLeft: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataBottomframeDataTopleftData
	bottomRight: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataBottomframeDataBottomrightData

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataData(TypedDict):
	topFrame: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataTopframeData
	bottomFrame: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataDataBottomframeData

class ShareClipRenderStatusResponseClipDataSuggestedcroppingData(TypedDict):
	portraitClipLayout: str
	fullTemplateMetadata: Union[NoneType, ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataData]
	stackedTemplateMetadata: Union[NoneType, ShareClipRenderStatusResponseClipDataSuggestedcroppingDataStackedtemplatemetadataData]

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

class ShoutoutHighlightServiceQueryRequest(TypedDict):
	targetLogin: Falsy[str]
	isLoggedOut: bool

class ShoutoutHighlightServiceQueryResponse1(TypedDict):
	...

class ShoutoutHighlightServiceQueryResponse2(TypedDict):
	user: NoneType

class StoryChannelQueryRequest(TypedDict):
	channelLogin: str

class StoryChannelQueryResponseUserData(TypedDict):
	id: str

class StoryChannelQueryResponse(TypedDict):
	user: StoryChannelQueryResponseUserData

class StreamChatRequest(TypedDict):
	login: str

class StreamChatResponseChannelDataRolesData(TypedDict):
	isPartner: bool
	isAffiliate: bool

class StreamChatResponseChannelDataSelfData(TypedDict):
	banStatus: NoneType
	isChannelMember: bool
	isModerator: bool
	subscriptionBenefit: NoneType

class StreamChatResponseChannelDataStreamData(TypedDict):
	id: str

class StreamChatResponseChannelData(TypedDict):
	id: str
	displayName: str
	roles: StreamChatResponseChannelDataRolesData
	self: Union[NoneType, StreamChatResponseChannelDataSelfData]
	stream: Union[NoneType, StreamChatResponseChannelDataStreamData]

class StreamChatResponse(TypedDict):
	channel: StreamChatResponseChannelData

class StreamMetadataRequest(TypedDict):
	channelLogin: str
	includeIsDJ: bool

class StreamMetadataResponseUserDataRolesData1(TypedDict):
	isPartner: bool
	isParticipatingDJ: bool

class StreamMetadataResponseUserDataRolesData2(TypedDict):
	isPartner: bool

class StreamMetadataResponseUserDataPrimaryteamData(TypedDict):
	id: str
	name: str
	displayName: str

class StreamMetadataResponseUserDataChannelData(TypedDict):
	id: str

class StreamMetadataResponseUserDataLastbroadcastData(TypedDict):
	id: str
	title: str

class StreamMetadataResponseUserDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str

class StreamMetadataResponseUserDataStreamData(TypedDict):
	id: str
	type: str
	createdAt: str
	game: StreamMetadataResponseUserDataStreamDataGameData

class StreamMetadataResponseUserData(TypedDict):
	id: str
	primaryColorHex: Union[NoneType, str]
	roles: Union[StreamMetadataResponseUserDataRolesData1, StreamMetadataResponseUserDataRolesData2]
	profileImageURL: str
	primaryTeam: Union[NoneType, StreamMetadataResponseUserDataPrimaryteamData]
	channel: StreamMetadataResponseUserDataChannelData
	lastBroadcast: StreamMetadataResponseUserDataLastbroadcastData
	stream: Union[NoneType, StreamMetadataResponseUserDataStreamData]

class StreamMetadataResponse(TypedDict):
	user: StreamMetadataResponseUserData

class StreamRefetchManagerRequest(TypedDict):
	channel: str

class StreamRefetchManagerResponseUserDataStreamData(TypedDict):
	id: str
	isEncrypted: bool

class StreamRefetchManagerResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, StreamRefetchManagerResponseUserDataStreamData]

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

class StreamScheduleResponseUserDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str

class StreamScheduleResponseUserDataBroadcastsettingsData(TypedDict):
	id: str
	title: str

class StreamScheduleResponseUserDataStreamDataGameData(TypedDict):
	id: str
	slug: str
	name: str

class StreamScheduleResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str
	viewersCount: int
	previewImageURL: str
	game: StreamScheduleResponseUserDataStreamDataGameData

class StreamScheduleResponseUserDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	slug: str
	name: str

class StreamScheduleResponseUserDataVideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	createdAt: str
	lengthSeconds: int
	viewCount: int
	previewThumbnailURL: str
	game: StreamScheduleResponseUserDataVideosDataEdgesDataNodeDataGameData

class StreamScheduleResponseUserDataVideosDataEdgesData(TypedDict):
	node: StreamScheduleResponseUserDataVideosDataEdgesDataNodeData

class StreamScheduleResponseUserDataVideosData(TypedDict):
	edges: Falsy[List[StreamScheduleResponseUserDataVideosDataEdgesData]]

class StreamScheduleResponseUserDataChannelDataScheduleDataNextsegmentData(TypedDict):
	id: str
	startAt: str

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

class StreamScheduleResponseUserDataChannelDataScheduleData(TypedDict):
	id: str
	nextSegment: Union[NoneType, StreamScheduleResponseUserDataChannelDataScheduleDataNextsegmentData]
	interruption: NoneType
	segments: Union[NoneType, List[StreamScheduleResponseUserDataChannelDataScheduleDataSegmentsData]]

class StreamScheduleResponseUserDataChannelData(TypedDict):
	id: str
	schedule: Union[NoneType, StreamScheduleResponseUserDataChannelDataScheduleData]

class StreamScheduleResponseUserData(TypedDict):
	id: str
	primaryColorHex: Union[NoneType, str]
	lastBroadcast: StreamScheduleResponseUserDataLastbroadcastData
	broadcastSettings: StreamScheduleResponseUserDataBroadcastsettingsData
	stream: Union[NoneType, StreamScheduleResponseUserDataStreamData]
	videos: StreamScheduleResponseUserDataVideosData
	channel: StreamScheduleResponseUserDataChannelData

class StreamScheduleResponse(TypedDict):
	currentUser: Union[NoneType, StreamScheduleResponseCurrentuserData]
	user: StreamScheduleResponseUserData

class SubscribedContextRequest(TypedDict):
	login: str

class SubscribedContextResponseUserDataSelfData(TypedDict):
	subscriptionBenefit: NoneType

class SubscribedContextResponseUserData(TypedDict):
	id: str
	self: Union[NoneType, SubscribedContextResponseUserDataSelfData]

class SubscribedContextResponse(TypedDict):
	user: SubscribedContextResponseUserData

class SyncedSettingsChatPauseSettingRequest(TypedDict):
	...

class SyncedSettingsChatPauseSettingResponseCurrentuserDataChatuisettingsData(TypedDict):
	chatPauseSetting: NoneType

class SyncedSettingsChatPauseSettingResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsChatPauseSettingResponseCurrentuserDataChatuisettingsData

class SyncedSettingsChatPauseSettingResponse(TypedDict):
	currentUser: SyncedSettingsChatPauseSettingResponseCurrentuserData

class SyncedSettingsDeletedMessageDisplaySettingRequest(TypedDict):
	...

class SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserDataChatuisettingsData(TypedDict):
	deletedMessageDisplaySetting: NoneType

class SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserDataChatuisettingsData

class SyncedSettingsDeletedMessageDisplaySettingResponse(TypedDict):
	currentUser: SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserData

class SyncedSettingsEmoteAnimationsRequest(TypedDict):
	...

class SyncedSettingsEmoteAnimationsResponseCurrentuserDataChatuisettingsData(TypedDict):
	isEmoteAnimationsEnabled: bool

class SyncedSettingsEmoteAnimationsResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsEmoteAnimationsResponseCurrentuserDataChatuisettingsData

class SyncedSettingsEmoteAnimationsResponse(TypedDict):
	currentUser: SyncedSettingsEmoteAnimationsResponseCurrentuserData

class SyncedSettingsReadableChatColorsRequest(TypedDict):
	...

class SyncedSettingsReadableChatColorsResponseCurrentuserDataChatuisettingsData(TypedDict):
	isReadableChatColorsEnabled: bool

class SyncedSettingsReadableChatColorsResponseCurrentuserData(TypedDict):
	id: str
	chatUISettings: SyncedSettingsReadableChatColorsResponseCurrentuserDataChatuisettingsData

class SyncedSettingsReadableChatColorsResponse(TypedDict):
	currentUser: SyncedSettingsReadableChatColorsResponseCurrentuserData

class TitleMentionsRequest(TypedDict):
	logins: Falsy[List[str]]

class TitleMentionsResponseUsersData(TypedDict):
	id: str
	login: str
	displayName: str
	description: Union[NoneType, str]
	primaryColorHex: Union[NoneType, str]
	profileImageURL: str

class TitleMentionsResponseCurrentuserDataRolesData(TypedDict):
	isSiteAdmin: NoneType
	isStaff: NoneType
	isGlobalMod: NoneType

class TitleMentionsResponseCurrentuserData(TypedDict):
	id: str
	login: str
	roles: TitleMentionsResponseCurrentuserDataRolesData
	blockedUsers: Falsy[List[Any]]

class TitleMentionsResponse(TypedDict):
	users: Falsy[List[TitleMentionsResponseUsersData]]
	currentUser: Union[NoneType, TitleMentionsResponseCurrentuserData]

class updateUserViewedVideoRequestInputData(TypedDict):
	userID: str
	position: Falsy[int]
	videoID: str
	videoType: str

class updateUserViewedVideoRequest(TypedDict):
	input: updateUserViewedVideoRequestInputData

class updateUserViewedVideoResponseUpdateuserviewedvideoDataVideoData(TypedDict):
	id: str

class updateUserViewedVideoResponseUpdateuserviewedvideoData(TypedDict):
	video: Union[NoneType, updateUserViewedVideoResponseUpdateuserviewedvideoDataVideoData]

class updateUserViewedVideoResponse(TypedDict):
	updateUserViewedVideo: Union[NoneType, updateUserViewedVideoResponseUpdateuserviewedvideoData]

class UseLiveRequest(TypedDict):
	channelLogin: str

class UseLiveResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str

class UseLiveResponseUserData(TypedDict):
	id: str
	login: str
	stream: Union[NoneType, UseLiveResponseUserDataStreamData]

class UseLiveResponse(TypedDict):
	user: UseLiveResponseUserData

class UseLiveBroadcastRequest(TypedDict):
	channelLogin: str

class UseLiveBroadcastResponseUserDataLastbroadcastDataGameData(TypedDict):
	id: str
	slug: str
	name: str
	displayName: str

class UseLiveBroadcastResponseUserDataLastbroadcastData(TypedDict):
	id: str
	title: str
	game: UseLiveBroadcastResponseUserDataLastbroadcastDataGameData

class UseLiveBroadcastResponseUserData(TypedDict):
	id: str
	lastBroadcast: UseLiveBroadcastResponseUserDataLastbroadcastData

class UseLiveBroadcastResponse(TypedDict):
	user: UseLiveBroadcastResponseUserData

class UserEmoticonPrefix_QueryRequest(TypedDict):
	...

class UserEmoticonPrefix_QueryResponseCurrentuserDataEmoticonprefixData(TypedDict):
	name: Falsy[str]
	state: str
	isEditable: bool

class UserEmoticonPrefix_QueryResponseCurrentuserDataRolesData(TypedDict):
	isPartner: bool
	isAffiliate: bool

class UserEmoticonPrefix_QueryResponseCurrentuserData(TypedDict):
	id: str
	login: str
	emoticonPrefix: UserEmoticonPrefix_QueryResponseCurrentuserDataEmoticonprefixData
	roles: UserEmoticonPrefix_QueryResponseCurrentuserDataRolesData

class UserEmoticonPrefix_QueryResponse(TypedDict):
	currentUser: UserEmoticonPrefix_QueryResponseCurrentuserData

class UserModStatusRequest(TypedDict):
	channelID: str
	userID: str

class UserModStatusResponseUserData(TypedDict):
	id: str
	login: str
	isModerator: bool

class UserModStatusResponse(TypedDict):
	user: UserModStatusResponseUserData

class UsernameRenameStatusRequest(TypedDict):
	...

class UsernameRenameStatusResponseCurrentuserDataLoginrenamestatusData(TypedDict):
	isEligible: bool
	eligibleAt: str

class UsernameRenameStatusResponseCurrentuserData(TypedDict):
	id: str
	loginRenameStatus: UsernameRenameStatusResponseCurrentuserDataLoginrenamestatusData

class UsernameRenameStatusResponse(TypedDict):
	currentUser: UsernameRenameStatusResponseCurrentuserData

class UseViewCountRequest(TypedDict):
	channelLogin: Falsy[str]

class UseViewCountResponseUserDataStreamData(TypedDict):
	id: str
	viewersCount: int
	collaborationViewersCount: NoneType

class UseViewCountResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, UseViewCountResponseUserDataStreamData]

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

class VerifyEmail_CurrentUserResponseRequestinfoData(TypedDict):
	countryCode: str

class VerifyEmail_CurrentUserResponse(TypedDict):
	currentUser: VerifyEmail_CurrentUserResponseCurrentuserData
	requestInfo: VerifyEmail_CurrentUserResponseRequestinfoData

class VideoAccessToken_ClipRequest(TypedDict):
	platform: str
	slug: str

class VideoAccessToken_ClipResponseClipDataPlaybackaccesstokenData(TypedDict):
	signature: str
	value: str

class VideoAccessToken_ClipResponseClipDataVideoqualitiesData(TypedDict):
	frameRate: Union[float, int]
	quality: str
	sourceURL: str

class VideoAccessToken_ClipResponseClipData(TypedDict):
	id: str
	playbackAccessToken: VideoAccessToken_ClipResponseClipDataPlaybackaccesstokenData
	videoQualities: List[VideoAccessToken_ClipResponseClipDataVideoqualitiesData]

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

class VideoCommentsResponseCheerconfigDataDisplayconfigDataColorsData(TypedDict):
	bits: int
	color: str

class VideoCommentsResponseCheerconfigDataDisplayconfigDataTypesData(TypedDict):
	animation: str
	extension: str

class VideoCommentsResponseCheerconfigDataDisplayconfigData(TypedDict):
	backgrounds: List[str]
	colors: List[VideoCommentsResponseCheerconfigDataDisplayconfigDataColorsData]
	order: List[str]
	scales: List[str]
	types: List[VideoCommentsResponseCheerconfigDataDisplayconfigDataTypesData]

class VideoCommentsResponseCheerconfigDataGroupsDataNodesDataTiersData(TypedDict):
	id: str
	bits: int
	canShowInBitsCard: bool

class VideoCommentsResponseCheerconfigDataGroupsDataNodesData(TypedDict):
	id: str
	prefix: str
	type: str
	campaign: NoneType
	tiers: List[VideoCommentsResponseCheerconfigDataGroupsDataNodesDataTiersData]

class VideoCommentsResponseCheerconfigDataGroupsData(TypedDict):
	templateURL: str
	nodes: List[VideoCommentsResponseCheerconfigDataGroupsDataNodesData]

class VideoCommentsResponseCheerconfigData(TypedDict):
	displayConfig: VideoCommentsResponseCheerconfigDataDisplayconfigData
	groups: List[VideoCommentsResponseCheerconfigDataGroupsData]

class VideoCommentsResponseCurrentuserDataRolesData(TypedDict):
	isStaff: NoneType
	isSiteAdmin: NoneType
	isGlobalMod: NoneType

class VideoCommentsResponseCurrentuserData(TypedDict):
	id: str
	roles: VideoCommentsResponseCurrentuserDataRolesData
	blockedUsers: Falsy[List[Any]]

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

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesDataTiersData(TypedDict):
	id: str
	bits: int
	canShowInBitsCard: bool

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesData(TypedDict):
	id: str
	prefix: str
	type: str
	campaign: NoneType
	tiers: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesDataTiersData]

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsData(TypedDict):
	templateURL: str
	nodes: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsDataNodesData]

class VideoCommentsResponseVideoDataOwnerDataCheerData(TypedDict):
	id: str
	cheerGroups: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsData]

class VideoCommentsResponseVideoDataOwnerDataSelfData(TypedDict):
	isModerator: bool

class VideoCommentsResponseVideoDataOwnerData(TypedDict):
	id: str
	login: str
	broadcastBadges: List[VideoCommentsResponseVideoDataOwnerDataBroadcastbadgesData]
	cheer: VideoCommentsResponseVideoDataOwnerDataCheerData
	self: Union[NoneType, VideoCommentsResponseVideoDataOwnerDataSelfData]

class VideoCommentsResponseVideoData(TypedDict):
	id: str
	broadcastType: str
	lengthSeconds: int
	owner: VideoCommentsResponseVideoDataOwnerData

class VideoCommentsResponseRequestinfoData(TypedDict):
	countryCode: str

class VideoCommentsResponse(TypedDict):
	badges: List[VideoCommentsResponseBadgesData]
	cheerConfig: VideoCommentsResponseCheerconfigData
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

class VideoCommentsByOffsetOrCursorResponseVideoDataCreatorData(TypedDict):
	id: str
	channel: VideoCommentsByOffsetOrCursorResponseVideoDataCreatorDataChannelData

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataCommenterData(TypedDict):
	id: str
	login: str
	displayName: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsDataEmoteData(TypedDict):
	id: str
	emoteID: str
	from_: Falsy[int] # WARNING: ADDED UNDERSCORE

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsData(TypedDict):
	emote: Union[NoneType, VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsDataEmoteData]
	text: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataUserbadgesData(TypedDict):
	id: str
	setID: Falsy[str]
	version: Falsy[str]

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageData(TypedDict):
	fragments: Falsy[List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataFragmentsData]]
	userBadges: Falsy[List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageDataUserbadgesData]]
	userColor: Union[NoneType, str]

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeData(TypedDict):
	id: str
	commenter: Union[NoneType, VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataCommenterData]
	contentOffsetSeconds: Falsy[int]
	createdAt: str
	message: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeDataMessageData

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesData(TypedDict):
	cursor: str
	node: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesDataNodeData

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataPageinfoData(TypedDict):
	hasNextPage: bool
	hasPreviousPage: bool

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsData(TypedDict):
	edges: List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesData]
	pageInfo: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataPageinfoData

class VideoCommentsByOffsetOrCursorResponseVideoData(TypedDict):
	id: str
	creator: VideoCommentsByOffsetOrCursorResponseVideoDataCreatorData
	comments: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsData

class VideoCommentsByOffsetOrCursorResponse(TypedDict):
	video: VideoCommentsByOffsetOrCursorResponseVideoData

class VideoMarkersChatCommandRequest(TypedDict):
	channelLogin: str

class VideoMarkersChatCommandResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str

class VideoMarkersChatCommandResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoMarkersChatCommandResponseUserDataStreamData]

class VideoMarkersChatCommandResponse(TypedDict):
	user: VideoMarkersChatCommandResponseUserData

class VideoMetadataRequest(TypedDict):
	channelLogin: str
	videoID: str

class VideoMetadataResponseUserDataLastbroadcastData(TypedDict):
	id: str
	startedAt: str

class VideoMetadataResponseUserDataStreamData(TypedDict):
	id: str
	viewersCount: int

class VideoMetadataResponseUserDataFollowersData(TypedDict):
	totalCount: int

class VideoMetadataResponseUserData(TypedDict):
	id: str
	primaryColorHex: Union[NoneType, str]
	isPartner: bool
	profileImageURL: str
	lastBroadcast: VideoMetadataResponseUserDataLastbroadcastData
	stream: Union[NoneType, VideoMetadataResponseUserDataStreamData]
	followers: VideoMetadataResponseUserDataFollowersData

class VideoMetadataResponseCurrentuserData(TypedDict):
	id: str

class VideoMetadataResponseVideoDataOwnerData(TypedDict):
	id: str
	login: str
	displayName: str

class VideoMetadataResponseVideoDataGameData(TypedDict):
	id: str
	slug: str
	boxArtURL: str
	name: str
	displayName: str

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

class VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeData(TypedDict):
	id: str
	login: str
	adProperties: VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeDataAdpropertiesData

class VideoPlayer_AgeGateOverlayBroadcasterResponse(TypedDict):
	userByAttribute: VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeData

class VideoPlayer_ChapterSelectButtonVideoRequest(TypedDict):
	includePrivate: bool
	videoID: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataMomentsData(TypedDict):
	edges: Falsy[List[Any]]

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData(TypedDict):
	id: str
	displayName: str
	boxArtURL: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataDetailsData(TypedDict):
	game: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeDataVideoData(TypedDict):
	id: str
	lengthSeconds: int

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

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesData(TypedDict):
	node: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesDataNodeData

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsData(TypedDict):
	edges: Falsy[List[VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesData]]

class VideoPlayer_ChapterSelectButtonVideoResponseVideoData(TypedDict):
	id: str
	moments: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsData

class VideoPlayer_ChapterSelectButtonVideoResponse(TypedDict):
	video: VideoPlayer_ChapterSelectButtonVideoResponseVideoData

class VideoPlayer_MutedSegmentsAlertOverlayRequest(TypedDict):
	includePrivate: bool
	vodID: str

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData(TypedDict):
	duration: int
	offset: Falsy[int]

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionData(TypedDict):
	nodes: List[VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData]

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoData(TypedDict):
	mutedSegmentConnection: Union[NoneType, VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionData]

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoData(TypedDict):
	id: str
	muteInfo: VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoData

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

class VideoPlayer_VideoSourceManagerResponse(TypedDict):
	userByAttribute: Union[NoneType, VideoPlayer_VideoSourceManagerResponseUserbyattributeData]

class VideoPlayer_VODSeekbarRequest(TypedDict):
	includePrivate: bool
	vodID: str

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData(TypedDict):
	duration: int
	offset: Falsy[int]

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionData(TypedDict):
	nodes: List[VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesData]

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoData(TypedDict):
	mutedSegmentConnection: Union[NoneType, VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionData]

class VideoPlayer_VODSeekbarResponseVideoData(TypedDict):
	id: str
	lengthSeconds: int
	muteInfo: VideoPlayer_VODSeekbarResponseVideoDataMuteinfoData

class VideoPlayer_VODSeekbarResponse(TypedDict):
	video: VideoPlayer_VODSeekbarResponseVideoData

class VideoPlayer_VODSeekbarPreviewVideoRequest(TypedDict):
	includePrivate: bool
	videoID: str

class VideoPlayer_VODSeekbarPreviewVideoResponseVideoData(TypedDict):
	id: str
	seekPreviewsURL: str

class VideoPlayer_VODSeekbarPreviewVideoResponse(TypedDict):
	video: VideoPlayer_VODSeekbarPreviewVideoResponseVideoData

class VideoPlayerClipPostplayRecommendationsOverlayRequest(TypedDict):
	slug: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str
	stream: NoneType

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataGameData(TypedDict):
	id: str
	displayName: str
	name: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataGameData(TypedDict):
	id: str
	displayName: str
	name: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	title: str
	thumbnailURL: str
	viewCount: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterDataGameData

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataGameData(TypedDict):
	id: str
	displayName: str
	name: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	title: str
	thumbnailURL: str
	viewCount: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameDataGameData

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataBroadcasterData(TypedDict):
	id: str
	displayName: str
	login: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataGameData(TypedDict):
	id: str
	displayName: str
	name: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	title: str
	thumbnailURL: str
	viewCount: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopDataGameData

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsData(TypedDict):
	broadcaster: List[VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataBroadcasterData]
	game: List[VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataGameData]
	top: List[VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsDataTopData]

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoDataGameData(TypedDict):
	id: str
	displayName: str
	name: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoData(TypedDict):
	id: str
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoDataGameData
	lengthSeconds: int
	previewThumbnailURL: str

class VideoPlayerClipPostplayRecommendationsOverlayResponseClipData(TypedDict):
	id: str
	durationSeconds: int
	slug: str
	videoOffsetSeconds: int
	broadcaster: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataBroadcasterData
	game: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataGameData
	relatedClips: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataRelatedclipsData
	video: VideoPlayerClipPostplayRecommendationsOverlayResponseClipDataVideoData

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

class VideoPlayerClipsButtonBroadcasterResponseUserbyattributeData(TypedDict):
	id: str
	login: str
	stream: Union[NoneType, VideoPlayerClipsButtonBroadcasterResponseUserbyattributeDataStreamData]

class VideoPlayerClipsButtonBroadcasterResponse(TypedDict):
	userByAttribute: VideoPlayerClipsButtonBroadcasterResponseUserbyattributeData

class VideoPlayerOfflineRecommendationsOverlayRequest(TypedDict):
	login: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeData(TypedDict):
	id: str
	title: str
	previewThumbnailURL: str
	game: VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeDataGameData

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesData(TypedDict):
	node: VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesDataNodeData

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosData(TypedDict):
	edges: Falsy[List[VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosDataEdgesData]]

class VideoPlayerOfflineRecommendationsOverlayResponseUserData(TypedDict):
	id: str
	videos: VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosData

class VideoPlayerOfflineRecommendationsOverlayResponse(TypedDict):
	user: VideoPlayerOfflineRecommendationsOverlayResponseUserData

class VideoPlayerStatusOverlayChannelRequest(TypedDict):
	channel: str

class VideoPlayerStatusOverlayChannelResponseUserDataStreamData(TypedDict):
	id: str
	type: str

class VideoPlayerStatusOverlayChannelResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoPlayerStatusOverlayChannelResponseUserDataStreamData]

class VideoPlayerStatusOverlayChannelResponse(TypedDict):
	user: VideoPlayerStatusOverlayChannelResponseUserData

class VideoPlayerStreamMetadataRequest(TypedDict):
	channel: str

class VideoPlayerStreamMetadataResponseUserDataStreamData(TypedDict):
	id: str
	isEncrypted: bool

class VideoPlayerStreamMetadataResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoPlayerStreamMetadataResponseUserDataStreamData]

class VideoPlayerStreamMetadataResponse(TypedDict):
	user: VideoPlayerStreamMetadataResponseUserData

class VideoPlayerVODPostplayRecommendationsRequest(TypedDict):
	videoID: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataGameData(TypedDict):
	id: str
	name: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataSelfData(TypedDict):
	viewingHistory: NoneType

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeData(TypedDict):
	id: str
	createdAt: str
	lengthSeconds: int
	title: str
	previewThumbnailURL: str
	game: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataGameData
	self: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeDataSelfData

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesData(TypedDict):
	node: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesDataNodeData

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosData(TypedDict):
	edges: List[VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosDataEdgesData]

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerData(TypedDict):
	id: str
	displayName: str
	videos: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosData

class VideoPlayerVODPostplayRecommendationsResponseVideoData(TypedDict):
	id: str
	owner: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerData

class VideoPlayerVODPostplayRecommendationsResponse(TypedDict):
	video: VideoPlayerVODPostplayRecommendationsResponseVideoData

class VideoPreviewCard__VideoMomentsRequest(TypedDict):
	videoId: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData(TypedDict):
	id: str
	slug: str
	displayName: str
	boxArtURL: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsData(TypedDict):
	game: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsDataGameData

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataVideoData(TypedDict):
	id: str
	lengthSeconds: int

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeData(TypedDict):
	id: str
	durationMilliseconds: int
	positionMilliseconds: Falsy[int]
	type: str
	description: str
	thumbnailURL: Falsy[str]
	details: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataDetailsData
	video: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeDataVideoData

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesData(TypedDict):
	cursor: Falsy[str]
	node: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesDataNodeData

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsData(TypedDict):
	edges: Falsy[List[VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesData]]

class VideoPreviewCard__VideoMomentsResponseVideoData(TypedDict):
	id: str
	moments: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsData

class VideoPreviewCard__VideoMomentsResponse(TypedDict):
	video: VideoPreviewCard__VideoMomentsResponseVideoData

class VideoPreviewOverlayRequest(TypedDict):
	login: str

class VideoPreviewOverlayResponseUserDataStreamData(TypedDict):
	id: str
	previewImageURL: str
	restrictionType: NoneType

class VideoPreviewOverlayResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, VideoPreviewOverlayResponseUserDataStreamData]

class VideoPreviewOverlayResponse(TypedDict):
	user: VideoPreviewOverlayResponseUserData

class ViewerCardRequest(TypedDict):
	channelID: str
	channelLogin: str
	hasChannelID: bool
	giftRecipientLogin: str
	isViewerBadgeCollectionEnabled: bool
	withStandardGifting: bool
	badgeSourceChannelID: str
	badgeSourceChannelLogin: str

class ViewerCardResponseActivetargetuserData(TypedDict):
	id: str

class ViewerCardResponseTargetuserDataRelationshipDataCumulativetenureData(TypedDict):
	daysRemaining: Falsy[int]
	months: Falsy[int]

class ViewerCardResponseTargetuserDataRelationshipData(TypedDict):
	cumulativeTenure: ViewerCardResponseTargetuserDataRelationshipDataCumulativetenureData
	followedAt: str
	subscriptionBenefit: NoneType

class ViewerCardResponseTargetuserData(TypedDict):
	id: str
	login: str
	bannerImageURL: NoneType
	displayName: str
	displayBadges: Falsy[List[Any]]
	profileImageURL: str
	createdAt: str
	relationship: ViewerCardResponseTargetuserDataRelationshipData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataEmotesData(TypedDict):
	id: str
	setID: str
	token: str
	assetType: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataEmotemodifiersData(TypedDict):
	code: str
	name: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataIntervalData(TypedDict):
	unit: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataSelfData(TypedDict):
	canGiftInChannel: bool

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataTagbindingsData(TypedDict):
	key: str
	value: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceDataDiscountData(TypedDict):
	price: int
	total: int

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: Union[NoneType, ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceDataDiscountData]

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalDataPlanData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelDataInternalData]

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingData(TypedDict):
	chargeModel: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingDataChargemodelData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataPromotionDataPromodisplayData(TypedDict):
	discountPercent: int
	discountType: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataPromotionData(TypedDict):
	id: str
	name: str
	promoDisplay: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataPromotionDataPromodisplayData
	priority: Falsy[int]
	promoType: str
	endAt: NoneType

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataQuantityData(TypedDict):
	min: int
	max: int

class ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersData(TypedDict):
	id: str
	tplr: str
	platform: str
	eligibility: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataEligibilityData
	tagBindings: List[ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataTagbindingsData]
	giftType: NoneType
	listing: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataListingData
	promotion: Union[NoneType, ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataPromotionData]
	quantity: ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersDataQuantityData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataTagbindingsData(TypedDict):
	key: str
	value: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: NoneType

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalDataPlanData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelDataInternalData]

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingData(TypedDict):
	chargeModel: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingDataChargemodelData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataQuantityData(TypedDict):
	min: int
	max: int

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferData(TypedDict):
	id: str
	tplr: str
	platform: str
	eligibility: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataEligibilityData
	tagBindings: List[ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataTagbindingsData]
	giftType: str
	listing: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataListingData
	promotion: NoneType
	quantity: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferDataQuantityData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardData(TypedDict):
	offer: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardDataOfferData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData(TypedDict):
	benefitsStartAt: str
	isEligible: bool

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData(TypedDict):
	key: str
	value: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	id: str
	currency: str
	exponent: int
	price: int
	total: int
	discount: NoneType

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	duration: int
	unit: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	interval: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData(TypedDict):
	previewPrice: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPreviewpriceData
	plan: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalDataPlanData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData(TypedDict):
	internal: Union[NoneType, ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelDataInternalData]

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData(TypedDict):
	chargeModel: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingDataChargemodelData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData(TypedDict):
	min: int
	max: int

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData(TypedDict):
	id: str
	tplr: str
	platform: str
	eligibility: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataEligibilityData
	tagBindings: List[ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataTagbindingsData]
	giftType: str
	listing: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataListingData
	promotion: NoneType
	quantity: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferDataQuantityData

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityData(TypedDict):
	offer: Union[NoneType, ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityDataOfferData]

class ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingData(TypedDict):
	standard: List[ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataStandardData]
	community: List[ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingDataCommunityData]

class ViewerCardResponseChanneluserDataSubscriptionproductsData(TypedDict):
	id: str
	price: str
	url: str
	emoteSetID: str
	displayName: str
	name: str
	tier: str
	type: str
	hasAdFree: bool
	emotes: Falsy[List[ViewerCardResponseChanneluserDataSubscriptionproductsDataEmotesData]]
	emoteModifiers: Falsy[List[ViewerCardResponseChanneluserDataSubscriptionproductsDataEmotemodifiersData]]
	interval: ViewerCardResponseChanneluserDataSubscriptionproductsDataIntervalData
	self: ViewerCardResponseChanneluserDataSubscriptionproductsDataSelfData
	offers: List[ViewerCardResponseChanneluserDataSubscriptionproductsDataOffersData]
	gifting: ViewerCardResponseChanneluserDataSubscriptionproductsDataGiftingData

class ViewerCardResponseChanneluserDataSelfData(TypedDict):
	banStatus: NoneType
	isModerator: bool

class ViewerCardResponseChanneluserData(TypedDict):
	id: str
	login: str
	displayName: str
	subscriptionProducts: List[ViewerCardResponseChanneluserDataSubscriptionproductsData]
	self: ViewerCardResponseChanneluserDataSelfData

class ViewerCardResponseCurrentuserDataRolesData(TypedDict):
	isSiteAdmin: NoneType
	isStaff: NoneType
	isGlobalMod: NoneType

class ViewerCardResponseCurrentuserData(TypedDict):
	login: str
	id: str
	roles: ViewerCardResponseCurrentuserDataRolesData
	blockedUsers: Falsy[List[Any]]

class ViewerCardResponseChannelviewerData(TypedDict):
	id: str
	earnedBadges: NoneType

class ViewerCardResponseChannelDataModerationsettingsData(TypedDict):
	canAccessViewerCardModLogs: bool

class ViewerCardResponseChannelData(TypedDict):
	id: str
	moderationSettings: ViewerCardResponseChannelDataModerationsettingsData

class ViewerCardResponseRequestinfoData(TypedDict):
	countryCode: str

class ViewerCardResponse(TypedDict):
	activeTargetUser: ViewerCardResponseActivetargetuserData
	targetUser: ViewerCardResponseTargetuserData
	channelUser: ViewerCardResponseChanneluserData
	currentUser: ViewerCardResponseCurrentuserData
	channelViewer: ViewerCardResponseChannelviewerData
	channel: ViewerCardResponseChannelData
	requestInfo: ViewerCardResponseRequestinfoData

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

class VODMidrollManagerResponseVideoDataOwnerData(TypedDict):
	id: str
	adProperties: VODMidrollManagerResponseVideoDataOwnerDataAdpropertiesData

class VODMidrollManagerResponseVideoData(TypedDict):
	id: str
	broadcastType: str
	owner: VODMidrollManagerResponseVideoDataOwnerData

class VODMidrollManagerResponse(TypedDict):
	video: VODMidrollManagerResponseVideoData

class WatchStreakExperimentRequest(TypedDict):
	channelID: Falsy[str]

class WatchStreakExperimentResponseChannelviewermilestonesettingsData(TypedDict):
	id: str
	isWatchStreakOptOut: bool
	isInWatchStreakProgressExperiment: bool

class WatchStreakExperimentResponse(TypedDict):
	channelViewerMilestoneSettings: Union[NoneType, WatchStreakExperimentResponseChannelviewermilestonesettingsData]

class Whispers_Whispers_UserWhisperThreadsRequest(TypedDict):
	...

class Whispers_Whispers_UserWhisperThreadsResponseCurrentuserDataWhisperthreadsData(TypedDict):
	edges: Falsy[List[Any]]

class Whispers_Whispers_UserWhisperThreadsResponseCurrentuserData(TypedDict):
	id: str
	login: str
	whisperThreads: Whispers_Whispers_UserWhisperThreadsResponseCurrentuserDataWhisperthreadsData

class Whispers_Whispers_UserWhisperThreadsResponse(TypedDict):
	currentUser: Whispers_Whispers_UserWhisperThreadsResponseCurrentuserData

class WithIsStreamLiveQueryRequest(TypedDict):
	id: str

class WithIsStreamLiveQueryResponseUserDataStreamData(TypedDict):
	id: str
	createdAt: str

class WithIsStreamLiveQueryResponseUserData(TypedDict):
	id: str
	stream: Union[NoneType, WithIsStreamLiveQueryResponseUserDataStreamData]

class WithIsStreamLiveQueryResponse(TypedDict):
	user: WithIsStreamLiveQueryResponseUserData

class AccessGetFeatureClipRestrictionsQuery(Endpoint[AccessGetFeatureClipRestrictionsQueryRequest]):
	sha256Hash = '14ae9c701ed1113c7c16a0cb613e7ba7eca000bc1b907c2969f2756e8af5a05b'
	operation_name = 'AccessGetFeatureClipRestrictionsQuery'

class AcknowledgeUnbanRequestPrompt(Endpoint[AcknowledgeUnbanRequestPromptRequest]):
	sha256Hash = '814210afb9c7c392ce35028f3a3aebfff446c3be2925af8c9ff4c04a34fe8c5f'
	operation_name = 'AcknowledgeUnbanRequestPrompt'

class ActiveGoals(Endpoint[ActiveGoalsRequest]):
	sha256Hash = 'c855218eb019092b69369658150473e440e1c09cb8515396897b96cfe350e647'
	operation_name = 'ActiveGoals'

class AvailableEmotesForChannelPaginated(Endpoint[AvailableEmotesForChannelPaginatedRequest]):
	sha256Hash = '6c45e0ecaa823cc7db3ecdd1502af2223c775bdcfb0f18a3a0ce9a0b7db8ef6c'
	operation_name = 'AvailableEmotesForChannelPaginated'

class BlockedUsers(Endpoint[BlockedUsersRequest]):
	sha256Hash = '8044e3fd61f8158a39e07b38f5d1a279d1fdb748faa9889fde046feae640f76b'
	operation_name = 'BlockedUsers'

class BrowsePage_AllDirectories(Endpoint[Union[BrowsePage_AllDirectoriesRequest1, BrowsePage_AllDirectoriesRequest2]]):
	sha256Hash = '2f67f71ba89f3c0ed26a141ec00da1defecb2303595f5cda4298169549783d9e'
	operation_name = 'BrowsePage_AllDirectories'

class BrowseVerticalDirectory(Endpoint[BrowseVerticalDirectoryRequest]):
	sha256Hash = 'd27ea34dd3c0a4c183deb152c1223b44794e7fd3c336bdc15aa61abc65cc2b76'
	operation_name = 'BrowseVerticalDirectory'

class CanCreateClip(Endpoint[CanCreateClipRequest]):
	sha256Hash = 'ea1796b7893cd9ab447c989967e8441ea230ea54091f63e71d4b189b72d17215'
	operation_name = 'CanCreateClip'

class CanViewersExportQuery(Endpoint[CanViewersExportQueryRequest]):
	sha256Hash = '8f5d5163e711a884a88079cbcd24d68adc6a90a7fcb4030a5aef266372c33fd0'
	operation_name = 'CanViewersExportQuery'

class ChannelAvatar(Endpoint[ChannelAvatarRequest]):
	sha256Hash = '12575ab92ea9444d8bade6de529b288a05073617f319c87078b3a89e74cd783a'
	operation_name = 'ChannelAvatar'

class ChannelClipCore(Endpoint[ChannelClipCoreRequest]):
	sha256Hash = 'a33067cdf92191dccfb53aa86f878a2c271e6a3587a6731dc8275e5751dd133f'
	operation_name = 'ChannelClipCore'

class ChannelCollaborationEligibilityQuery(Endpoint[ChannelCollaborationEligibilityQueryRequest]):
	sha256Hash = 'f32cb49f6bc54a4dc182b54c6e247d8344f8a16cc255acbc2e18fbd145df4cb2'
	operation_name = 'ChannelCollaborationEligibilityQuery'

class ChannelLeaderboards(Endpoint[ChannelLeaderboardsRequest]):
	sha256Hash = 'ccc0fe65d86216ca35fae890e29e53e508dc3ff6bbe4fd893ca9b5b87dffbe5e'
	operation_name = 'ChannelLeaderboards'

class ChannelPage_SetSessionStatus(Endpoint[ChannelPage_SetSessionStatusRequest]):
	sha256Hash = '8521e08af74c8cb5128e4bb99fa53b591391cb19492e65fb0489aeee2f96947f'
	operation_name = 'ChannelPage_SetSessionStatus'

class ChannelPage_SubscribeButton_User(Endpoint[Union[ChannelPage_SubscribeButton_UserRequest1, ChannelPage_SubscribeButton_UserRequest2]]):
	sha256Hash = '53b7d2bfc430935ea80f813edba87f2447d5401acae5b6d8c885534997c3ca15'
	operation_name = 'ChannelPage_SubscribeButton_User'

class ChannelPointsContext(Endpoint[ChannelPointsContextRequest]):
	sha256Hash = '374314de591e69925fce3ddc2bcf085796f56ebb8cad67a0daa3165c03adc345'
	operation_name = 'ChannelPointsContext'

class ChannelPointsGlobalContext(Endpoint[ChannelPointsGlobalContextRequest]):
	sha256Hash = 'd3fa3a96e78a3e62bdd3ef3c4effafeda52442906cec41a9440e609a388679e2'
	operation_name = 'ChannelPointsGlobalContext'

class ChannelPointsPredictionContext(Endpoint[ChannelPointsPredictionContextRequest]):
	sha256Hash = 'beb846598256b75bd7c1fe54a80431335996153e358ca9c7837ce7bb83d7d383'
	operation_name = 'ChannelPointsPredictionContext'

class ChannelPollContext_GetViewablePoll(Endpoint[ChannelPollContext_GetViewablePollRequest]):
	sha256Hash = 'e83188a3836c636393df3191665e543a03733d7c51d3ade3d85e42aa46c2bf55'
	operation_name = 'ChannelPollContext_GetViewablePoll'

class ChannelShell(Endpoint[ChannelShellRequest]):
	sha256Hash = '580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe'
	operation_name = 'ChannelShell'

class ChannelSkins(Endpoint[ChannelSkinsRequest]):
	sha256Hash = 'b035de8611dc0bfbea6d0ce43af3f95319220fb5d23fc7a1448c16e1d83fed1c'
	operation_name = 'ChannelSkins'

class ChannelSocialButtons(Endpoint[ChannelSocialButtonsRequest]):
	sha256Hash = '597b4ee27086064ccd59bef5c02775e9963cc3354f2095159484e816ccc1aec2'
	operation_name = 'ChannelSocialButtons'

class ChannelSupportButtons(Endpoint[ChannelSupportButtonsRequest]):
	sha256Hash = '834a75e1c06cffada00f0900664a5033e392f6fb655fae8d2e25b21b340545a9'
	operation_name = 'ChannelSupportButtons'

class ChannelVideoCore(Endpoint[ChannelVideoCoreRequest]):
	sha256Hash = 'cf1ccf6f5b94c94d662efec5223dfb260c9f8bf053239a76125a58118769e8e2'
	operation_name = 'ChannelVideoCore'

class ChannelVideosContent_Game(Endpoint[ChannelVideosContent_GameRequest]):
	sha256Hash = 'ed8a9f2a5a99b96d010b66f45c81c157190c52635fc7ffee31b591f866041390'
	operation_name = 'ChannelVideosContent_Game'

class Chat_ChannelData(Endpoint[Chat_ChannelDataRequest]):
	sha256Hash = '3c445f9a8315fa164f2d3fb12c2f932754c2f2c129f952605b9ec6cf026dd362'
	operation_name = 'Chat_ChannelData'

class Chat_EarnedBadges_InitialSubStatus(Endpoint[Chat_EarnedBadges_InitialSubStatusRequest]):
	sha256Hash = '85a95b95a12628668eaac4d2862b53bb376dba0325c80eae8f26539cedc5f1a3'
	operation_name = 'Chat_EarnedBadges_InitialSubStatus'

class Chat_OrbisPresetText(Endpoint[Chat_OrbisPresetTextRequest]):
	sha256Hash = '960bf1fac4adb3f4e99b0c67627180d5f5ebb6e46139b1149fbdeab68f7f62e1'
	operation_name = 'Chat_OrbisPresetText'

class Chat_ShareResub_ChannelData(Endpoint[Chat_ShareResub_ChannelDataRequest]):
	sha256Hash = '1cef2e84b602f767839e5ffd489e81536e9d11e0be250bb85a17974cedad8f54'
	operation_name = 'Chat_ShareResub_ChannelData'

class Chat_UserData(Endpoint[Chat_UserDataRequest]):
	sha256Hash = '39985d1ff9324442a3a5df1be212e1bc4f358a31100e5025c4e61a07d7e70743'
	operation_name = 'Chat_UserData'

class ChatClip(Endpoint[ChatClipRequest]):
	sha256Hash = '9aa558e066a22227c5ef2c0a8fded3aaa57d35181ad15f63df25bff516253a90'
	operation_name = 'ChatClip'

class ChatFilterContextManager_User(Endpoint[ChatFilterContextManager_UserRequest]):
	sha256Hash = '98821224809f26e3f3a627a0e30134b00c4db33b602b4249cec518a8c21fe902'
	operation_name = 'ChatFilterContextManager_User'

class ChatInput(Endpoint[ChatInputRequest]):
	sha256Hash = 'd8ab574eb44e3e82aabc96fc9c59af6eafead3e96262910a6396c007e7a11e05'
	operation_name = 'ChatInput'

class ChatInput_Badges(Endpoint[ChatInput_BadgesRequest]):
	sha256Hash = '8cb0eae66555ad6dc76aaa111d191ea6174c743f996d506f530e479f28e6b37c'
	operation_name = 'ChatInput_Badges'

class ChatList_Badges(Endpoint[ChatList_BadgesRequest]):
	sha256Hash = '838a7e0b47c09cac05f93ff081a9ff4f876b68f7624f0fc465fe30031e372fc2'
	operation_name = 'ChatList_Badges'

class ChatModeratorStrikeStatus(Endpoint[ChatModeratorStrikeStatusRequest]):
	sha256Hash = '7f50f7190a840cd9fe9a91398f34ebb690eeba7cb28bce70e4cbf7ed1d06f268'
	operation_name = 'ChatModeratorStrikeStatus'

class ChatRestrictions(Endpoint[ChatRestrictionsRequest]):
	sha256Hash = '7514aeb3d2c203087b83e920f8d36eb18a5ca1bfa96a554ed431255ecbbbc089'
	operation_name = 'ChatRestrictions'

class ChatRoomBanStatus(Endpoint[ChatRoomBanStatusRequest]):
	sha256Hash = '319f2a9a3ac7ddecd7925944416c14b818b65676ab69da604460b68938d22bea'
	operation_name = 'ChatRoomBanStatus'

class ChatRoomState(Endpoint[ChatRoomStateRequest]):
	sha256Hash = '9e0f79669e31950c658459564bc4cff236ac9c03e534cc32769ac58bc0cdd708'
	operation_name = 'ChatRoomState'

class ChatScreenReaderAutoAnnounce(Endpoint[ChatScreenReaderAutoAnnounceRequest]):
	sha256Hash = '3ddf79c5dd411106eae1d44801f1a123ecf82cad7e973575b18367b2c5d63a0c'
	operation_name = 'ChatScreenReaderAutoAnnounce'

class ClaimCommunityPoints(Endpoint[ClaimCommunityPointsRequest]):
	sha256Hash = '46aaeebe02c99afdf4fc97c7c0cba964124bf6b0af229395f1f6d1feed05b3d0'
	operation_name = 'ClaimCommunityPoints'

class ClipMetadata(Endpoint[ClipMetadataRequest]):
	sha256Hash = '49817470e0129051cd93c86069aee755795f1a952688f0111bac71a49841ece7'
	operation_name = 'ClipMetadata'

class ClipsCards__User(Endpoint[ClipsCards__UserRequest]):
	sha256Hash = '4eb8f85fc41a36c481d809e8e99b2a32127fdb7647c336d27743ec4a88c4ea44'
	operation_name = 'ClipsCards__User'

class ClipsExperimentEnrollmentStatus(Endpoint[ClipsExperimentEnrollmentStatusRequest]):
	sha256Hash = '0575e09a580d3a30bffe06b09ebda047ebebf57ab86a4d7329527d312e8dea22'
	operation_name = 'ClipsExperimentEnrollmentStatus'

class CollectionCarouselQuery(Endpoint[CollectionCarouselQueryRequest]):
	sha256Hash = '0ca5b673f0a160f85267d7c5fbfe797f1d7b8129025aedc353cb5c99f2c94fec'
	operation_name = 'CollectionCarouselQuery'

class CommonHooks_BlockedUsers(Endpoint[CommonHooks_BlockedUsersRequest]):
	sha256Hash = '7c87171d7497df41f9938d2bc18a26f7a97f32f11b7f28c4826950c4ebe000b2'
	operation_name = 'CommonHooks_BlockedUsers'

class CommunityOnboardingAllowlist(Endpoint[CommunityOnboardingAllowlistRequest]):
	sha256Hash = 'b9119d11f5d434ed5482a7598000066f49dccbcb2395ae11105e28469370d110'
	operation_name = 'CommunityOnboardingAllowlist'

class CommunityPointsAvailableClaim(Endpoint[CommunityPointsAvailableClaimRequest]):
	sha256Hash = '3a4ca75d2a784eea5c40f38a60fe9f6ab8c565c030de06c561398ee5099f818c'
	operation_name = 'CommunityPointsAvailableClaim'

class CommunityPointsChatPrivateCalloutUser(Endpoint[CommunityPointsChatPrivateCalloutUserRequest]):
	sha256Hash = '15b66a0a6b743c72a63c273f2bfc4155c4209c1a85c29b6847474717877c3507'
	operation_name = 'CommunityPointsChatPrivateCalloutUser'

class CommunitySupportSettings(Endpoint[CommunitySupportSettingsRequest]):
	sha256Hash = '11b3e9eeff8190e1fa7b97cafbcb2427e3a54289676b030fc16a7ae125702da0'
	operation_name = 'CommunitySupportSettings'

class ContentClassificationContext(Endpoint[Union[ContentClassificationContextRequest1, ContentClassificationContextRequest2, ContentClassificationContextRequest3]]):
	sha256Hash = '57bb6c1aca3631b2b3e74b1c3c8adbecbbcc3becb70ec52d7c5ef0f90d7c3b02'
	operation_name = 'ContentClassificationContext'

class ContentPolicyPropertiesQuery(Endpoint[ContentPolicyPropertiesQueryRequest]):
	sha256Hash = 'e2c1cb362a9b601440d764b2db98eaf4fc21b9091973b158c8b702716419545a'
	operation_name = 'ContentPolicyPropertiesQuery'

class CoreActionsCurrentUser(Endpoint[CoreActionsCurrentUserRequest]):
	sha256Hash = '6b5b63a013cf66a995d61f71a508ab5c8e4473350c5d4136f846ba65e8101e95'
	operation_name = 'CoreActionsCurrentUser'

class CurrentUserBannedStatus(Endpoint[CurrentUserBannedStatusRequest]):
	sha256Hash = 'dede147839ea4a357639f1dc3d3eb978556e82eefb7abdefce8911d0e23a63ad'
	operation_name = 'CurrentUserBannedStatus'

class CurrentUserModeratorStatus(Endpoint[Union[CurrentUserModeratorStatusRequest1, CurrentUserModeratorStatusRequest2]]):
	sha256Hash = '1684c97f8b9f49bbeff32bfd6fcc08bd4e631f16b4fca43bdcc7e14e20eff110'
	operation_name = 'CurrentUserModeratorStatus'

class CurrentUserStrikeStatus(Endpoint[CurrentUserStrikeStatusRequest]):
	sha256Hash = '954bb138c800c581b291b7068a9225f7e139eb2b5066bc5840a9b251f5eaf11b'
	operation_name = 'CurrentUserStrikeStatus'

class DirectoryCollection_BrowsableCollection(Endpoint[Union[DirectoryCollection_BrowsableCollectionRequest1, DirectoryCollection_BrowsableCollectionRequest2]]):
	sha256Hash = '459f2a65ca11d3765450546a68980ac5868a6b4cce1a9e10bccb9a6e52d2c30d'
	operation_name = 'DirectoryCollection_BrowsableCollection'

class DirectoryPage_Game(Endpoint[Union[DirectoryPage_GameRequest1, DirectoryPage_GameRequest2]]):
	sha256Hash = 'c7c9d5aad09155c4161d2382092dc44610367f3536aac39019ec2582ae5065f9'
	operation_name = 'DirectoryPage_Game'

class DirectoryRoot_Directory(Endpoint[DirectoryRoot_DirectoryRequest]):
	sha256Hash = '99d3c9b5ceaadb36f77c8bc2d576a737c83d2e9f06c4d6190cf2c6b4f214cccb'
	operation_name = 'DirectoryRoot_Directory'

class DirectoryVideos_Game(Endpoint[Union[DirectoryVideos_GameRequest1, DirectoryVideos_GameRequest2]]):
	sha256Hash = 'f19b861ed9c767a1c231be8f757958005cd537a6e9730bc01c6b4735c2eaf211'
	operation_name = 'DirectoryVideos_Game'

class DiscoveryPreferenceMutation(Endpoint[DiscoveryPreferenceMutationRequest]):
	sha256Hash = '8d678244f64bdc494b1f80405ae4dc5a288da40a3eeb337fa11a3204c0a88215'
	operation_name = 'DiscoveryPreferenceMutation'

class DiscoveryPreferenceQuery(Endpoint[DiscoveryPreferenceQueryRequest]):
	sha256Hash = '1f8967625aae5c8617bfe7a16f8cb1a5647db9c4cc4e5aceda09c76d61cef9b0'
	operation_name = 'DiscoveryPreferenceQuery'

class DropCurrentSessionContext(Endpoint[DropCurrentSessionContextRequest]):
	sha256Hash = '4d06b702d25d652afb9ef835d2a550031f1cf762b193523a92166f40ea3d142b'
	operation_name = 'DropCurrentSessionContext'

class DropsHighlightService_AvailableDrops(Endpoint[DropsHighlightService_AvailableDropsRequest]):
	sha256Hash = '19e0b383db0be3dc917379fddcbf9dfa7c49f1fcc543d920f39f4efd054bc636'
	operation_name = 'DropsHighlightService_AvailableDrops'

class EmotesForChannelFollowStatus(Endpoint[EmotesForChannelFollowStatusRequest]):
	sha256Hash = '40cf0bf434717c70fa192e8a7805ae8651fae53a410d609f02ad853e3af94e78'
	operation_name = 'EmotesForChannelFollowStatus'

class FeaturedContentCarouselStreams(Endpoint[FeaturedContentCarouselStreamsRequest]):
	sha256Hash = '663a12a5bcf38aa3f6f566e328e9e7de44986746101c0ad10b50186f768b41b7'
	operation_name = 'FeaturedContentCarouselStreams'

class FilterableVideoTower_Videos(Endpoint[Union[FilterableVideoTower_VideosRequest1, FilterableVideoTower_VideosRequest2, FilterableVideoTower_VideosRequest3]]):
	sha256Hash = 'acea7539a293dfd30f0b0b81a263134bb5d9a7175592e14ac3f7c77b192de416'
	operation_name = 'FilterableVideoTower_Videos'

class FollowButton_FollowUser(Endpoint[FollowButton_FollowUserRequest]):
	sha256Hash = '800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08'
	operation_name = 'FollowButton_FollowUser'

class FollowButton_UnfollowUser(Endpoint[FollowButton_UnfollowUserRequest]):
	sha256Hash = 'f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880'
	operation_name = 'FollowButton_UnfollowUser'

class FollowButton_User(Endpoint[FollowButton_UserRequest]):
	sha256Hash = '870906a2de25d7488239dbeb947dafe3e5697f1fef2e8bce6601555a17e4d86d'
	operation_name = 'FollowButton_User'

class FollowedIndex_CurrentUser(Endpoint[FollowedIndex_CurrentUserRequest]):
	sha256Hash = '740647c696400dad6767b9407089fc2d52e88c4227dbb1f5cd763e015cc61df2'
	operation_name = 'FollowedIndex_CurrentUser'

class FollowedIndex_FollowCount(Endpoint[FollowedIndex_FollowCountRequest]):
	sha256Hash = '8945379bb5b05b905ba4e3669d02b863a3089fae81befc9f2a82dbd45ae6efc5'
	operation_name = 'FollowedIndex_FollowCount'

class FollowedStreams(Endpoint[FollowedStreamsRequest]):
	sha256Hash = '10fbb27d9260e3688cd9febdbdd3e21e3331d698ca282dc5f0cf0d29bb468fdd'
	operation_name = 'FollowedStreams'

class FollowedStreamsContinueWatching(Endpoint[FollowedStreamsContinueWatchingRequest]):
	sha256Hash = 'c689d0645defdd63aaab322166a570c785cefa97b6e97c1a1e7fb66ccdfcad82'
	operation_name = 'FollowedStreamsContinueWatching'

class FollowedVideos_CurrentUser(Endpoint[FollowedVideos_CurrentUserRequest]):
	sha256Hash = '11d0ddb94121afab8fa8b641e01f038db35892f95b4e4b9e5380eaa33d5e4a8c'
	operation_name = 'FollowedVideos_CurrentUser'

class FollowGameButton_Game(Endpoint[FollowGameButton_GameRequest]):
	sha256Hash = '8c5ac3233e26d9132ca2aaa8fb4b07ae97bc70f3c9a357967b9a764ebccaa9f0'
	operation_name = 'FollowGameButton_Game'

class FollowingGames_CurrentUser(Endpoint[FollowingGames_CurrentUserRequest]):
	sha256Hash = 'f3c5d45175d623ed3d5ff4ca4c7de379ea6a1a4852236087dc1b81b7dbfd3114'
	operation_name = 'FollowingGames_CurrentUser'

class FollowingLive_CurrentUser(Endpoint[FollowingLive_CurrentUserRequest]):
	sha256Hash = 'ecadcf350272dde399a63385cf888903d7fcd4c8fc6809a8469fe3753579d1c6'
	operation_name = 'FollowingLive_CurrentUser'

class FollowingPage_RecommendedChannels(Endpoint[FollowingPage_RecommendedChannelsRequest]):
	sha256Hash = '39c731d90e41de782e21c370c6e43bd23757fcaf98051e865016faef05c080b4'
	operation_name = 'FollowingPage_RecommendedChannels'

class FrontPageNew_User(Endpoint[FrontPageNew_UserRequest]):
	sha256Hash = '64bd07a2cbaca80699d62636d966cf6395a5d14a1f0a14282067dcb28b13eb11'
	operation_name = 'FrontPageNew_User'

class GetDisplayName(Endpoint[GetDisplayNameRequest]):
	sha256Hash = 'ba351b3d3018c3779fcaa398507e41579ae6cf12ad123a04f090943c21dedb8a'
	operation_name = 'GetDisplayName'

class GetGuestSessionBlocksAndBans(Endpoint[GetGuestSessionBlocksAndBansRequest]):
	sha256Hash = '4a96b8e893624487d7eaf212f61e756e00354e969a19b0e01d2e863021d75974'
	operation_name = 'GetGuestSessionBlocksAndBans'

class GetHypeTrainExecutionV2(Endpoint[GetHypeTrainExecutionV2Request]):
	sha256Hash = '9248d0eed139a2127b61e5c57e4c7bc4252cd521cb70af6bd5036a7c789598b8'
	operation_name = 'GetHypeTrainExecutionV2'

class GetIDFromLogin(Endpoint[GetIDFromLoginRequest]):
	sha256Hash = '94e82a7b1e3c21e186daa73ee2afc4b8f23bade1fbbff6fe8ac133f50a2f58ca'
	operation_name = 'GetIDFromLogin'

class GetPinnedChat(Endpoint[GetPinnedChatRequest]):
	sha256Hash = '2d099d4c9b6af80a07d8440140c4f3dbb04d516b35c401aab7ce8f60765308d5'
	operation_name = 'GetPinnedChat'

class GetUserID(Endpoint[GetUserIDRequest]):
	sha256Hash = 'bf6c594605caa0c63522f690156aa04bd434870bf963deb76668c381d16fcaa5'
	operation_name = 'GetUserID'

class GlobalBadges(Endpoint[GlobalBadgesRequest]):
	sha256Hash = '9db27e18d61ee393ccfdec8c7d90f14f9a11266298c2e5eb808550b77d7bcdf6'
	operation_name = 'GlobalBadges'

class GuestListQuery(Endpoint[GuestListQueryRequest]):
	sha256Hash = '7a2267973bdd74b9ddd5d07ceabd73b5b5d13eae83b54d4436fb5a3fa26c3bc8'
	operation_name = 'GuestListQuery'

class GuestStarActiveJoinRequest(Endpoint[GuestStarActiveJoinRequestRequest]):
	sha256Hash = 'ee299efe4c857e2ab673e57c0c29ff3171671dc4980ca3834f63d6e66ed16a8b'
	operation_name = 'GuestStarActiveJoinRequest'

class GuestStarBatchCollaborationQuery(Endpoint[GuestStarBatchCollaborationQueryRequest]):
	sha256Hash = '096d50357df5e938f4fa83fe2acf25cb0f4886149aa81ddb9754eae98c05f2dd'
	operation_name = 'GuestStarBatchCollaborationQuery'

class GuestStarChannelPageCollaborationQuery(Endpoint[GuestStarChannelPageCollaborationQueryRequest]):
	sha256Hash = 'adb54eefd172fc9d310040afe5c158e2e41ec93dfe030067afa365178243ffa3'
	operation_name = 'GuestStarChannelPageCollaborationQuery'

class HappeningNowSettings(Endpoint[HappeningNowSettingsRequest]):
	sha256Hash = '6945ce7f7df91e52f21edc98ea04f63e5ab38f4e6f4b5699bdd652171f9a7b48'
	operation_name = 'HappeningNowSettings'

class HomeOfflineCarousel(Endpoint[HomeOfflineCarouselRequest]):
	sha256Hash = '84e25789b04ac4dcaefd673cfb4259d39d03c6422838d09a4ed2aaf9b67054d8'
	operation_name = 'HomeOfflineCarousel'

class incrementClipViewCount(Endpoint[incrementClipViewCountRequest]):
	sha256Hash = '6b2f169f994f2b93ff68774f6928de66a1e8cdb70a42f4af3a5a1ecc68ee759b'
	operation_name = 'incrementClipViewCount'

class LastUnbanRequest(Endpoint[LastUnbanRequestRequest]):
	sha256Hash = 'ff196f08b09d9f9f977610f676cfc56bc5e2f679ad773c1acc4f889defb9aebd'
	operation_name = 'LastUnbanRequest'

class LowerHomeHeader(Endpoint[LowerHomeHeaderRequest]):
	sha256Hash = '08af264bf5d5231cadb05acaddce0992622f86a0d3d7f6f59955316564d3c008'
	operation_name = 'LowerHomeHeader'

class MessageBuffer_Channel(Endpoint[MessageBuffer_ChannelRequest]):
	sha256Hash = 'bfc959904f55b5003ae4674d4bea83ebdcd8867ad76e12f38957d433902d2fcc'
	operation_name = 'MessageBuffer_Channel'

class MessageBufferChatHistory(Endpoint[Union[MessageBufferChatHistoryRequest1, MessageBufferChatHistoryRequest2]]):
	sha256Hash = '33dba0e0c249135052e930cbd6c4a66daa32249ba00d1c8def75857fa3f3431d'
	operation_name = 'MessageBufferChatHistory'

class NielsenContentMetadata(Endpoint[NielsenContentMetadataRequest]):
	sha256Hash = '2dbf505ee929438369e68e72319d1106bb3c142e295332fac157c90638968586'
	operation_name = 'NielsenContentMetadata'

class OneClickEligibility(Endpoint[OneClickEligibilityRequest]):
	sha256Hash = 'ab0d03b2c38e3a570ca5f8fb4d0884bc7764c6f25a05345dc2014c611fa02de9'
	operation_name = 'OneClickEligibility'

class OneTapFeed(Endpoint[OneTapFeedRequest]):
	sha256Hash = '287ce6226da1b78e05e5024b99a3e3190a3e57e1bd1a95ae16d0eef33edc1547'
	operation_name = 'OneTapFeed'

class PaidPinnedChat(Endpoint[PaidPinnedChatRequest]):
	sha256Hash = '888056ddc92e62a7d2fd7a8e0afae5d61fab767ba621ed1006ba8628f6de8e41'
	operation_name = 'PaidPinnedChat'

class PbyPGame(Endpoint[PbyPGameRequest]):
	sha256Hash = 'f7444c6e187868a7b82e7659e59bb8ccd177cb4deca277e3a951fb2ef66c2389'
	operation_name = 'PbyPGame'

class PersistentGoalFollowButton_User(Endpoint[PersistentGoalFollowButton_UserRequest]):
	sha256Hash = '88f5b0d6e9d13d6751b07b5e9cc175e3f7f6f7cedb07b033e1b548ba2323f015'
	operation_name = 'PersistentGoalFollowButton_User'

class PersonalSectionsHypeTrains(Endpoint[PersonalSectionsHypeTrainsRequest]):
	sha256Hash = '073ad6ed08cd7d57f2532cd9b2ae962c323343a8ed8a46e853cd9afa00712c06'
	operation_name = 'PersonalSectionsHypeTrains'

class PinnedChatSettings(Endpoint[PinnedChatSettingsRequest]):
	sha256Hash = 'ff555546ff83a3034dee18a6d764123717b6f68553e082dea6b77a66b7b2672e'
	operation_name = 'PinnedChatSettings'

class PinnedCheersSettings(Endpoint[PinnedCheersSettingsRequest]):
	sha256Hash = 'ca73cb0396fe5bcbe05c906fd472622e4b873eeb07699c2664026a079aeec631'
	operation_name = 'PinnedCheersSettings'

class PlaybackAccessToken(Endpoint[PlaybackAccessTokenRequest]):
	sha256Hash = 'ed230aa1e33e07eebb8928504583da78a5173989fadfb1ac94be06a04f3cdbe9'
	operation_name = 'PlaybackAccessToken'

class PollChannelSettings(Endpoint[PollChannelSettingsRequest]):
	sha256Hash = 'e31355d5fd19bf9b3c0907c8302ce9ff5466d06230bec209f78cf04724b7380c'
	operation_name = 'PollChannelSettings'

class PrefetchPlaybackAccessToken(Endpoint[PrefetchPlaybackAccessTokenRequest]):
	sha256Hash = 'c101f277c6ab7de34f64e63c90d698edae0d83ed5fad8efe198596b472ef3337'
	operation_name = 'PrefetchPlaybackAccessToken'

class ProfileImageSetting(Endpoint[ProfileImageSettingRequest]):
	sha256Hash = '3d814a91606062a51f71e90c9b5a2d6e86792f52dacd912967d458067b5db44d'
	operation_name = 'ProfileImageSetting'

class queryUserViewedVideo(Endpoint[queryUserViewedVideoRequest]):
	sha256Hash = 'e249447c070b095eb599cceec239bbca567e30080795789f85bc25db3f7a27ad'
	operation_name = 'queryUserViewedVideo'

class RealtimeStreamTagList(Endpoint[RealtimeStreamTagListRequest]):
	sha256Hash = 'a4747cac9d8e8bf6cf80969f6da6363ca1bdbd80fe136797e71504eb404313fd'
	operation_name = 'RealtimeStreamTagList'

class RecapEligibilityQuery(Endpoint[RecapEligibilityQueryRequest]):
	sha256Hash = 'caf047b3d39c4ab74d0ae590e4a24530f531e1a33945058a4526d75cd86eb3fc'
	operation_name = 'RecapEligibilityQuery'

class RoleRestricted(Endpoint[RoleRestrictedRequest]):
	sha256Hash = '7f57264e30ae6d9daa154bb62c8b0bcb1b38fc0b53a7b3cdecd60a060ff8332b'
	operation_name = 'RoleRestricted'

class Settings_ProfilePage_AccountInfoSettings(Endpoint[Settings_ProfilePage_AccountInfoSettingsRequest]):
	sha256Hash = '60a54ebcbd29e095db489ed6268f33d5fe5ed1d4fa3176668d8091587ae81779'
	operation_name = 'Settings_ProfilePage_AccountInfoSettings'

class ShareClipRenderStatus(Endpoint[ShareClipRenderStatusRequest]):
	sha256Hash = 'f130048a462a0ac86bb54d653c968c514e9ab9ca94db52368c1179e97b0f16eb'
	operation_name = 'ShareClipRenderStatus'

class SharedChatModeratorStrikes(Endpoint[SharedChatModeratorStrikesRequest]):
	sha256Hash = '846b72652391105f0cd30ff586c807dfb4d4815f768ec13462d7b4d2e0d75d52'
	operation_name = 'SharedChatModeratorStrikes'

class SharedChatSession(Endpoint[SharedChatSessionRequest]):
	sha256Hash = '0ff9562b30cfa2b41ab1738485ced6f8f1e725a93abe732c396be5f4f1d13694'
	operation_name = 'SharedChatSession'

class ShoutoutHighlightServiceQuery(Endpoint[ShoutoutHighlightServiceQueryRequest]):
	sha256Hash = 'da377690d61c9f2923af148efb8b79b29674e4195c0230a4037a567ce8d40825'
	operation_name = 'ShoutoutHighlightServiceQuery'

class StoryChannelQuery(Endpoint[StoryChannelQueryRequest]):
	sha256Hash = 'efa575524a7a86bf6172801278301584a366e59a8049c667fd4abea01522b8a2'
	operation_name = 'StoryChannelQuery'

class StreamChat(Endpoint[StreamChatRequest]):
	sha256Hash = 'fed5f3ae0f569dc9d6faf768475456715b853ef737873ed5cb2bb45b3e28e67f'
	operation_name = 'StreamChat'

class StreamMetadata(Endpoint[StreamMetadataRequest]):
	sha256Hash = 'b57f9b910f8cd1a4659d894fe7550ccc81ec9052c01e438b290fd66a040b9b93'
	operation_name = 'StreamMetadata'

class StreamRefetchManager(Endpoint[StreamRefetchManagerRequest]):
	sha256Hash = 'ecdcb724b0559d49689e6a32795e6a43bba4b2071b5e762a4d1edf2bb42a6789'
	operation_name = 'StreamRefetchManager'

class StreamSchedule(Endpoint[StreamScheduleRequest]):
	sha256Hash = '83552f5614707fd3e897495c18875b6fa9c83d8cf11e73b9f158f3173b4f3b75'
	operation_name = 'StreamSchedule'

class SubscribedContext(Endpoint[SubscribedContextRequest]):
	sha256Hash = '56f8d2d143e1045284432c96830b3fdb811876efb03f9b5c8504a0cee4fd1bbb'
	operation_name = 'SubscribedContext'

class SyncedSettingsChatPauseSetting(Endpoint[SyncedSettingsChatPauseSettingRequest]):
	sha256Hash = '922f2a23e49da4ce2660f7fbfeefeefab19f7651196f9b54f03555590f173627'
	operation_name = 'SyncedSettingsChatPauseSetting'

class SyncedSettingsDeletedMessageDisplaySetting(Endpoint[SyncedSettingsDeletedMessageDisplaySettingRequest]):
	sha256Hash = '79fbdf86e8ee5fa4ca27cad96c292702eed8a8cc14faedc874a577f6e8fe4004'
	operation_name = 'SyncedSettingsDeletedMessageDisplaySetting'

class SyncedSettingsEmoteAnimations(Endpoint[SyncedSettingsEmoteAnimationsRequest]):
	sha256Hash = '64ac5d385b316fd889f8c46942a7c7463a1429452ef20ffc5d0cd23fcc4ecf30'
	operation_name = 'SyncedSettingsEmoteAnimations'

class SyncedSettingsReadableChatColors(Endpoint[SyncedSettingsReadableChatColorsRequest]):
	sha256Hash = 'cd9c43ab3cb4c04515a879bbd618055aab18c6ac4081ed9de333945ca91247ba'
	operation_name = 'SyncedSettingsReadableChatColors'

class TitleMentions(Endpoint[TitleMentionsRequest]):
	sha256Hash = '79439ae721a6f24f9d761ceae3a5c91097929fc59f5072a3b505e675bb3d432f'
	operation_name = 'TitleMentions'

class updateUserViewedVideo(Endpoint[updateUserViewedVideoRequest]):
	sha256Hash = 'bb58b1bd08a4ca0c61f2b8d323381a5f4cd39d763da8698f680ef1dfaea89ca1'
	operation_name = 'updateUserViewedVideo'

class UseLive(Endpoint[UseLiveRequest]):
	sha256Hash = '639d5f11bfb8bf3053b424d9ef650d04c4ebb7d94711d644afb08fe9a0fad5d9'
	operation_name = 'UseLive'

class UseLiveBroadcast(Endpoint[UseLiveBroadcastRequest]):
	sha256Hash = '0b47cc6d8c182acd2e78b81c8ba5414a5a38057f2089b1bbcfa6046aae248bd2'
	operation_name = 'UseLiveBroadcast'

class UserEmoticonPrefix_Query(Endpoint[UserEmoticonPrefix_QueryRequest]):
	sha256Hash = '6eb368f3a785c358509cc0da9ff56ac76d535e255196d496dd7312487d3abbe1'
	operation_name = 'UserEmoticonPrefix_Query'

class UserModStatus(Endpoint[UserModStatusRequest]):
	sha256Hash = '511b58faf547070bc95b7d32e7b5cdedf8c289a3aeabfc3c5d3ece2de01ae06f'
	operation_name = 'UserModStatus'

class UsernameRenameStatus(Endpoint[UsernameRenameStatusRequest]):
	sha256Hash = 'caed6a3d336fc50251da7b944462ea321d7f276ee6fcccdf7e2e3de4d6ab5204'
	operation_name = 'UsernameRenameStatus'

class UseViewCount(Endpoint[UseViewCountRequest]):
	sha256Hash = '95e6bd7acfbb2f220c17e387805141b77b43b18e5b27b4f702713e9ddbe6b907'
	operation_name = 'UseViewCount'

class VerifyEmail_CurrentUser(Endpoint[VerifyEmail_CurrentUserRequest]):
	sha256Hash = 'f9e7dcdf7e99c314c82d8f7f725fab5f99d1df3d7359b53c9ae122deec590198'
	operation_name = 'VerifyEmail_CurrentUser'

class VideoAccessToken_Clip(Endpoint[VideoAccessToken_ClipRequest]):
	sha256Hash = '6fd3af2b22989506269b9ac02dd87eb4a6688392d67d94e41a6886f1e9f5c00f'
	operation_name = 'VideoAccessToken_Clip'

class VideoComments(Endpoint[VideoCommentsRequest]):
	sha256Hash = 'be06407e8d7cda72f2ee086ebb11abb6b062a7deb8985738e648090904d2f0eb'
	operation_name = 'VideoComments'

class VideoCommentsByOffsetOrCursor(Endpoint[Union[VideoCommentsByOffsetOrCursorRequest1, VideoCommentsByOffsetOrCursorRequest2]]):
	sha256Hash = 'b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a'
	operation_name = 'VideoCommentsByOffsetOrCursor'

class VideoMarkersChatCommand(Endpoint[VideoMarkersChatCommandRequest]):
	sha256Hash = 'c65f8b33e3bcccf2b16057e8f445311d213ecf8729f842ccdc71908231fa9a78'
	operation_name = 'VideoMarkersChatCommand'

class VideoMetadata(Endpoint[VideoMetadataRequest]):
	sha256Hash = '45111672eea2e507f8ba44d101a61862f9c56b11dee09a15634cb75cb9b9084d'
	operation_name = 'VideoMetadata'

class VideoPlayer_AgeGateOverlayBroadcaster(Endpoint[VideoPlayer_AgeGateOverlayBroadcasterRequest]):
	sha256Hash = 'ab175a77fb908cd5dfe25d6d23da0765b3fc187e3d3461d1c7b157c354e917ee'
	operation_name = 'VideoPlayer_AgeGateOverlayBroadcaster'

class VideoPlayer_ChapterSelectButtonVideo(Endpoint[VideoPlayer_ChapterSelectButtonVideoRequest]):
	sha256Hash = '71835d5ef425e154bf282453a926d99b328cdc5e32f36d3a209d0f4778b41203'
	operation_name = 'VideoPlayer_ChapterSelectButtonVideo'

class VideoPlayer_MutedSegmentsAlertOverlay(Endpoint[VideoPlayer_MutedSegmentsAlertOverlayRequest]):
	sha256Hash = 'c36e7400657815f4704e6063d265dff766ed8fc1590361c6d71e4368805e0b49'
	operation_name = 'VideoPlayer_MutedSegmentsAlertOverlay'

class VideoPlayer_VideoSourceManager(Endpoint[VideoPlayer_VideoSourceManagerRequest]):
	sha256Hash = 'f5e1b35d6f5a40348c6476fea36945d0931ba50621e1701b6c31252ee498cc3e'
	operation_name = 'VideoPlayer_VideoSourceManager'

class VideoPlayer_VODSeekbar(Endpoint[VideoPlayer_VODSeekbarRequest]):
	sha256Hash = 'c67d32eba8f1c93b02e7efa6a278be46009e390ed5195c02dd0621e4c7ca14ac'
	operation_name = 'VideoPlayer_VODSeekbar'

class VideoPlayer_VODSeekbarPreviewVideo(Endpoint[VideoPlayer_VODSeekbarPreviewVideoRequest]):
	sha256Hash = '07e99e4d56c5a7c67117a154777b0baf85a5ffefa393b213f4bc712ccaf85dd6'
	operation_name = 'VideoPlayer_VODSeekbarPreviewVideo'

class VideoPlayerClipPostplayRecommendationsOverlay(Endpoint[VideoPlayerClipPostplayRecommendationsOverlayRequest]):
	sha256Hash = '4261232b81ad1b4dde3bbf8ada53b8c236bf035fcd18842ec327f631ba4a3870'
	operation_name = 'VideoPlayerClipPostplayRecommendationsOverlay'

class VideoPlayerClipsButtonBroadcaster(Endpoint[VideoPlayerClipsButtonBroadcasterRequest]):
	sha256Hash = '784065d408671ee105d64241cc6f461b1c32684d837734fa2f4c761229a7efcd'
	operation_name = 'VideoPlayerClipsButtonBroadcaster'

class VideoPlayerOfflineRecommendationsOverlay(Endpoint[VideoPlayerOfflineRecommendationsOverlayRequest]):
	sha256Hash = '73794e55fa4149d5a17b31105f74e625f291ca68a4c034076053be0f647ba5ee'
	operation_name = 'VideoPlayerOfflineRecommendationsOverlay'

class VideoPlayerStatusOverlayChannel(Endpoint[VideoPlayerStatusOverlayChannelRequest]):
	sha256Hash = '938d155c890df88b5da53592e327d36ae9b851d2ee38bdb13342a1402fc24ad2'
	operation_name = 'VideoPlayerStatusOverlayChannel'

class VideoPlayerStreamMetadata(Endpoint[VideoPlayerStreamMetadataRequest]):
	sha256Hash = '248fee6868e983c4e7b69074e888960f77735bd21a1d4a1d882b55f45d30a420'
	operation_name = 'VideoPlayerStreamMetadata'

class VideoPlayerVODPostplayRecommendations(Endpoint[VideoPlayerVODPostplayRecommendationsRequest]):
	sha256Hash = '2e29be981ae55ea4cf78cda648afa156928508c3cb03c6ca5c1726fdef1183d8'
	operation_name = 'VideoPlayerVODPostplayRecommendations'

class VideoPreviewCard__VideoMoments(Endpoint[VideoPreviewCard__VideoMomentsRequest]):
	sha256Hash = '7399051b2d46f528d5f0eedf8b0db8d485bb1bb4c0a2c6707be6f1290cdcb31a'
	operation_name = 'VideoPreviewCard__VideoMoments'

class VideoPreviewOverlay(Endpoint[VideoPreviewOverlayRequest]):
	sha256Hash = '9515480dee68a77e667cb19de634739d33f243572b007e98e67184b1a5d8369f'
	operation_name = 'VideoPreviewOverlay'

class ViewerCard(Endpoint[ViewerCardRequest]):
	sha256Hash = 'd46031bdcc9880edd0a8b57dfebe13ce27493f4da64fad744ba6a81560900a52'
	operation_name = 'ViewerCard'

class VODMidrollManager(Endpoint[VODMidrollManagerRequest]):
	sha256Hash = 'dcfb8c8cd3b721da5720fda11b9a20a3ab94be85ec04e8c2ac48ff69f300e959'
	operation_name = 'VODMidrollManager'

class WatchStreakExperiment(Endpoint[WatchStreakExperimentRequest]):
	sha256Hash = 'ec1ad3e0e7a2c3c3c762652f7a42b12da8b4db074fe99f0d29b2febd330465db'
	operation_name = 'WatchStreakExperiment'

class Whispers_Whispers_UserWhisperThreads(Endpoint[Whispers_Whispers_UserWhisperThreadsRequest]):
	sha256Hash = '9d4bf15288a0b4d96492c97dafa17222aa000528adcad4f8d1652441d9132d62'
	operation_name = 'Whispers_Whispers_UserWhisperThreads'

class WithIsStreamLiveQuery(Endpoint[WithIsStreamLiveQueryRequest]):
	sha256Hash = '04e46329a6786ff3a81c01c50bfa5d725902507a0deb83b0edbf7abe7a3716ea'
	operation_name = 'WithIsStreamLiveQuery'


class PlaybackAccessToken_Template(Endpoint[PlaybackAccessTokenRequest]):
	def __init__(self):
		self.draft = {
			"operationName": "PlaybackAccessToken_Template",
			'query': "query PlaybackAccessToken_Template($login: String!, $isLive: Boolean!, $vodID: ID!, $isVod: Boolean!, $playerType: String!, $platform: String!) {  streamPlaybackAccessToken(channelName: $login, params: {platform: $platform, playerBackend: \"mediaplayer\", playerType: $playerType}) @include(if: $isLive) {    value    signature   authorization { isForbidden forbiddenReasonCode }   __typename  }  videoPlaybackAccessToken(id: $vodID, params: {platform: $platform, playerBackend: \"mediaplayer\", playerType: $playerType}) @include(if: $isVod) {    value    signature   __typename  }}",
			"variables": {}
		}

class Endpoints:
	"""Placeholder for all endpoints in current module"""
	amount = 164
	AccessGetFeatureClipRestrictionsQuery = AccessGetFeatureClipRestrictionsQuery()
	AcknowledgeUnbanRequestPrompt = AcknowledgeUnbanRequestPrompt()
	ActiveGoals = ActiveGoals()
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
	ChannelPollContext_GetViewablePoll = ChannelPollContext_GetViewablePoll()
	ChannelShell = ChannelShell()
	ChannelSkins = ChannelSkins()
	ChannelSocialButtons = ChannelSocialButtons()
	ChannelSupportButtons = ChannelSupportButtons()
	ChannelVideoCore = ChannelVideoCore()
	ChannelVideosContent_Game = ChannelVideosContent_Game()
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
	CommonHooks_BlockedUsers = CommonHooks_BlockedUsers()
	CommunityOnboardingAllowlist = CommunityOnboardingAllowlist()
	CommunityPointsAvailableClaim = CommunityPointsAvailableClaim()
	CommunityPointsChatPrivateCalloutUser = CommunityPointsChatPrivateCalloutUser()
	CommunitySupportSettings = CommunitySupportSettings()
	ContentClassificationContext = ContentClassificationContext()
	ContentPolicyPropertiesQuery = ContentPolicyPropertiesQuery()
	CoreActionsCurrentUser = CoreActionsCurrentUser()
	CurrentUserBannedStatus = CurrentUserBannedStatus()
	CurrentUserModeratorStatus = CurrentUserModeratorStatus()
	CurrentUserStrikeStatus = CurrentUserStrikeStatus()
	DirectoryCollection_BrowsableCollection = DirectoryCollection_BrowsableCollection()
	DirectoryPage_Game = DirectoryPage_Game()
	DirectoryRoot_Directory = DirectoryRoot_Directory()
	DirectoryVideos_Game = DirectoryVideos_Game()
	DiscoveryPreferenceMutation = DiscoveryPreferenceMutation()
	DiscoveryPreferenceQuery = DiscoveryPreferenceQuery()
	DropCurrentSessionContext = DropCurrentSessionContext()
	DropsHighlightService_AvailableDrops = DropsHighlightService_AvailableDrops()
	EmotesForChannelFollowStatus = EmotesForChannelFollowStatus()
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
	FollowGameButton_Game = FollowGameButton_Game()
	FollowingGames_CurrentUser = FollowingGames_CurrentUser()
	FollowingLive_CurrentUser = FollowingLive_CurrentUser()
	FollowingPage_RecommendedChannels = FollowingPage_RecommendedChannels()
	FrontPageNew_User = FrontPageNew_User()
	GetDisplayName = GetDisplayName()
	GetGuestSessionBlocksAndBans = GetGuestSessionBlocksAndBans()
	GetHypeTrainExecutionV2 = GetHypeTrainExecutionV2()
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
	incrementClipViewCount = incrementClipViewCount()
	LastUnbanRequest = LastUnbanRequest()
	LowerHomeHeader = LowerHomeHeader()
	MessageBuffer_Channel = MessageBuffer_Channel()
	MessageBufferChatHistory = MessageBufferChatHistory()
	NielsenContentMetadata = NielsenContentMetadata()
	OneClickEligibility = OneClickEligibility()
	OneTapFeed = OneTapFeed()
	PaidPinnedChat = PaidPinnedChat()
	PbyPGame = PbyPGame()
	PersistentGoalFollowButton_User = PersistentGoalFollowButton_User()
	PersonalSectionsHypeTrains = PersonalSectionsHypeTrains()
	PinnedChatSettings = PinnedChatSettings()
	PinnedCheersSettings = PinnedCheersSettings()
	PlaybackAccessToken = PlaybackAccessToken()
	PollChannelSettings = PollChannelSettings()
	PrefetchPlaybackAccessToken = PrefetchPlaybackAccessToken()
	ProfileImageSetting = ProfileImageSetting()
	queryUserViewedVideo = queryUserViewedVideo()
	RealtimeStreamTagList = RealtimeStreamTagList()
	RecapEligibilityQuery = RecapEligibilityQuery()
	RoleRestricted = RoleRestricted()
	Settings_ProfilePage_AccountInfoSettings = Settings_ProfilePage_AccountInfoSettings()
	ShareClipRenderStatus = ShareClipRenderStatus()
	SharedChatModeratorStrikes = SharedChatModeratorStrikes()
	SharedChatSession = SharedChatSession()
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
	updateUserViewedVideo = updateUserViewedVideo()
	UseLive = UseLive()
	UseLiveBroadcast = UseLiveBroadcast()
	UserEmoticonPrefix_Query = UserEmoticonPrefix_Query()
	UserModStatus = UserModStatus()
	UsernameRenameStatus = UsernameRenameStatus()
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
	ViewerCard = ViewerCard()
	VODMidrollManager = VODMidrollManager()
	WatchStreakExperiment = WatchStreakExperiment()
	Whispers_Whispers_UserWhisperThreads = Whispers_Whispers_UserWhisperThreads()
	WithIsStreamLiveQuery = WithIsStreamLiveQuery()
	PlaybackAccessToken_Template = PlaybackAccessToken_Template()
	...
