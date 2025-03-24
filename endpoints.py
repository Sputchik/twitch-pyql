from typing import Dict, TypedDict, List, Optional, Any, Union
from types import NoneType


__all__ = [
	"Endpoint",
	"Endpoints",

	"AccessGetFeatureClipRestrictionsQueryRequest",
	"AccessGetFeatureClipRestrictionsQueryResponse",
	"AccessGetUserQueryRequest",
	"AccessGetUserQueryResponse",
	"AccessIsAffiliateQueryRequest",
	"AccessIsAffiliateQueryResponse",
	"AccessIsBountiesEnabledQueryRequest",
	"AccessIsBountiesEnabledQueryResponse",
	"AccessIsChannelEditorQueryRequest",
	"AccessIsChannelEditorQueryResponse",
	"AccessIsChannelModeratorQueryRequest",
	"AccessIsChannelModeratorQueryResponse",
	"AccessIsChannelPointsAvailableQueryRequest",
	"AccessIsChannelPointsAvailableQueryResponse",
	"AccessIsCommunityMomentsEnabledQueryRequest",
	"AccessIsCommunityMomentsEnabledQueryResponse",
	"AccessIsExtensionsDeveloperQueryRequest",
	"AccessIsExtensionsDeveloperQueryResponse",
	"AccessIsPartnerQueryRequest",
	"AccessIsPartnerQueryResponse",
	"AccessIsSiteAdminQueryRequest",
	"AccessIsSiteAdminQueryResponse",
	"AchievementsPageRequest",
	"AchievementsPageResponse",
	"AcknowledgeUnbanRequestPromptRequest",
	"AcknowledgeUnbanRequestPromptResponse",
	"ActiveGoalsRequest",
	"ActiveGoalsResponse",
	"ActiveWatchPartyRequest",
	"ActiveWatchPartyResponse",
	"AdRequestHandlingRequest",
	"AdRequestHandlingResponse1",
	"AdRequestHandlingResponse2",
	"Ads_Components_AdManager_UserRequest",
	"Ads_Components_AdManager_UserResponse",
	"AdvancedNotificationSettings_UserRequest",
	"AdvancedNotificationSettings_UserResponse",
	"AnnouncementsIconRequest",
	"AnnouncementsIconResponse",
	"ArtistAttributionChannelsRequest",
	"ArtistAttributionChannelsResponse",
	"AvailableEmotesForChannelPaginatedRequest",
	"AvailableEmotesForChannelPaginatedResponse",
	"BannerNotificationQueryRequest",
	"BannerNotificationQueryResponse",
	"BitsCard_BitsRequest",
	"BitsCard_BitsResponse",
	"BitsConfigContext_ChannelRequest",
	"BitsConfigContext_ChannelResponse",
	"BitsConfigContext_GlobalRequest",
	"BitsConfigContext_GlobalResponse",
	"BlockedUsersRequest",
	"BlockedUsersResponse",
	"BrowsePage_AllDirectoriesRequest1",
	"BrowsePage_AllDirectoriesRequest2",
	"BrowsePage_AllDirectoriesResponse",
	"BrowsePage_PopularRequest",
	"BrowsePage_PopularResponse",
	"BrowseVerticalDirectoryRequest",
	"BrowseVerticalDirectoryResponse",
	"CanCreateClipRequest",
	"CanCreateClipResponse",
	"CanViewersExportQueryRequest",
	"CanViewersExportQueryResponse",
	"CategoryChannels_InternationalSectionRequest",
	"CategoryChannels_InternationalSectionResponse",
	"CelebrationContextChannelIDRequest",
	"CelebrationContextChannelIDResponse",
	"CelebrationEmotesRequest",
	"CelebrationEmotesResponse",
	"ChannelActiveCharityCampaignRequest",
	"ChannelActiveCharityCampaignResponse",
	"ChannelAvatarRequest",
	"ChannelAvatarResponse",
	"ChannelClipCoreRequest",
	"ChannelClipCoreResponse",
	"ChannelCollaborationEligibilityQueryRequest",
	"ChannelCollaborationEligibilityQueryResponse",
	"ChannelFollowsRequest",
	"ChannelFollowsResponse",
	"ChannelLeaderboardsRequest",
	"ChannelLeaderboardsResponse",
	"ChannelPage_SetSessionStatusRequest",
	"ChannelPage_SetSessionStatusResponse",
	"ChannelPage_SubscribeButton_UserRequest1",
	"ChannelPage_SubscribeButton_UserRequest2",
	"ChannelPage_SubscribeButton_UserResponse",
	"ChannelPanelsRequest",
	"ChannelPanelsResponse",
	"ChannelPointsAutomaticRewardsRequest",
	"ChannelPointsAutomaticRewardsResponse",
	"ChannelPointsContextRequest",
	"ChannelPointsContextResponse",
	"ChannelPointsGlobalContextRequest",
	"ChannelPointsGlobalContextResponse",
	"ChannelPointsPredictionContextRequest",
	"ChannelPointsPredictionContextResponse",
	"ChannelPollContext_GetViewablePollRequest",
	"ChannelPollContext_GetViewablePollResponse",
	"ChannelProductsWithCommunityGiftOffersRequest",
	"ChannelProductsWithCommunityGiftOffersResponse",
	"ChannelRoot_AboutPanelRequest",
	"ChannelRoot_AboutPanelResponse",
	"ChannelSharedBansRequest",
	"ChannelSharedBansResponse",
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
	"CharityNavItemRequest",
	"CharityNavItemResponse",
	"ChatClipRequest",
	"ChatClipResponse",
	"ChatFilterContextManager_UserRequest",
	"ChatFilterContextManager_UserResponse",
	"ChatHighlightSettingsRequest",
	"ChatHighlightSettingsResponse",
	"ChatInputRequest",
	"ChatInputResponse",
	"ChatInput_BadgesRequest",
	"ChatInput_BadgesResponse",
	"ChatList_ActiveCharityCampaignRequest",
	"ChatList_ActiveCharityCampaignResponse",
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
	"ChatSettings_BadgesRequest",
	"ChatSettings_BadgesResponse",
	"Chat_ChannelDataRequest",
	"Chat_ChannelDataResponse",
	"Chat_EarnedBadges_InitialSubStatusRequest",
	"Chat_EarnedBadges_InitialSubStatusResponse",
	"Chat_OrbisPresetTextRequest",
	"Chat_OrbisPresetTextResponse",
	"Chat_ShareBitsBadgeTier_ChannelDataRequest",
	"Chat_ShareBitsBadgeTier_ChannelDataResponse",
	"Chat_ShareResub_ChannelDataRequest",
	"Chat_ShareResub_ChannelDataResponse",
	"Chat_UserDataRequest",
	"Chat_UserDataResponse",
	"ClaimCommunityPointsRequest",
	"ClaimCommunityPointsResponse",
	"ClientSideAdEventHandling_RecordAdEventRequest",
	"ClientSideAdEventHandling_RecordAdEventResponse",
	"ClipMetadataBroadcastInfoQueryRequest",
	"ClipMetadataBroadcastInfoQueryResponse",
	"ClipMetadataRequest",
	"ClipMetadataResponse",
	"ClipsCards__GameRequest",
	"ClipsCards__GameResponse",
	"ClipsCards__UserRequest",
	"ClipsCards__UserResponse",
	"ClipsExperimentEnrollmentStatusRequest",
	"ClipsExperimentEnrollmentStatusResponse",
	"CollaborationPromoPrivateCalloutRequest",
	"CollaborationPromoPrivateCalloutResponse",
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
	"CommunityPointsRewardRedemptionContextRequest",
	"CommunityPointsRewardRedemptionContextResponse",
	"CommunitySupportSettingsRequest",
	"CommunitySupportSettingsResponse",
	"ConnectAdIdentityMutationRequest",
	"ConnectAdIdentityMutationResponse",
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
	"CopyrightSchoolInvitationRequest",
	"CopyrightSchoolInvitationResponse",
	"CoreActionsCurrentUserRequest",
	"CoreActionsCurrentUserResponse",
	"Core_Services_Spade_CurrentUserRequest",
	"Core_Services_Spade_CurrentUserResponse",
	"CreateRawMediaRequest",
	"CreateRawMediaResponse",
	"CreatorHomeGetEmoteDataRequest",
	"CreatorHomeGetEmoteDataResponse",
	"CreatorHomeSuggestedExtensionsRequest",
	"CreatorHomeSuggestedExtensionsResponse",
	"CurrentUserBannedStatusRequest",
	"CurrentUserBannedStatusResponse",
	"CurrentUserModeratorStatusRequest1",
	"CurrentUserModeratorStatusRequest2",
	"CurrentUserModeratorStatusResponse",
	"CurrentUserStrikeStatusRequest",
	"CurrentUserStrikeStatusResponse",
	"DMCAViolationCountBannerRequest",
	"DMCAViolationCountBannerResponse",
	"DashboardChannelSettingsRequest",
	"DashboardChannelSettingsResponse",
	"DashboardInsights_ChannelRequest",
	"DashboardInsights_ChannelResponse",
	"Dashboard_CensusGetBirthdateRequest",
	"Dashboard_CensusGetBirthdateResponse",
	"DirectoryCollection_BrowsableCollectionRequest1",
	"DirectoryCollection_BrowsableCollectionRequest2",
	"DirectoryCollection_BrowsableCollectionResponse",
	"DirectoryPage_GameRequest",
	"DirectoryPage_GameResponse",
	"DirectoryRoot_DirectoryRequest",
	"DirectoryRoot_DirectoryResponse",
	"DirectoryVideos_GameRequest1",
	"DirectoryVideos_GameRequest2",
	"DirectoryVideos_GameResponse",
	"Directory_DirectoryBannerRequest",
	"Directory_DirectoryBannerResponse",
	"DropCurrentSessionContextRequest",
	"DropCurrentSessionContextResponse",
	"DropsHighlightService_AvailableDropsRequest",
	"DropsHighlightService_AvailableDropsResponse",
	"EmotePicker_EmotePicker_UserSubscriptionProductsRequest",
	"EmotePicker_EmotePicker_UserSubscriptionProductsResponse",
	"EmotesForChannelFollowStatusRequest",
	"EmotesForChannelFollowStatusResponse",
	"ExtensionProductsRequest",
	"ExtensionProductsResponse",
	"ExtensionsForChannelRequest",
	"ExtensionsForChannelResponse",
	"ExtensionsInfoBalloonRequest",
	"ExtensionsInfoBalloonResponse",
	"ExtensionsNotificationBitsBalanceRequest",
	"ExtensionsNotificationBitsBalanceResponse",
	"ExtensionsOverlayRequest",
	"ExtensionsOverlayResponse",
	"ExtensionsUIContext_ChannelIDRequest",
	"ExtensionsUIContext_ChannelIDResponse",
	"FeaturedClipsShelfCoverRequest",
	"FeaturedClipsShelfCoverResponse",
	"FeaturedContentCarouselStreamsRequest",
	"FeaturedContentCarouselStreamsResponse",
	"FeaturedUpcomingStreamsRequest",
	"FeaturedUpcomingStreamsResponse",
	"FilterableVideoTower_VideosRequest1",
	"FilterableVideoTower_VideosRequest2",
	"FilterableVideoTower_VideosResponse",
	"FollowButton_FollowUserRequest",
	"FollowButton_FollowUserResponse",
	"FollowButton_UnfollowUserRequest",
	"FollowButton_UnfollowUserResponse",
	"FollowButton_UserRequest",
	"FollowButton_UserResponse",
	"FollowGameButton_GameRequest",
	"FollowGameButton_GameResponse",
	"FollowPanelOverlayRequest",
	"FollowPanelOverlayResponse",
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
	"GetBitsButton_BitsRequest",
	"GetBitsButton_BitsResponse",
	"GetDisplayNameRequest",
	"GetDisplayNameResponse",
	"GetGuestSessionBlocksAndBansRequest",
	"GetGuestSessionBlocksAndBansResponse",
	"GetGuestStarSessionQueryRequest",
	"GetGuestStarSessionQueryResponse",
	"GetHypeTrainExecutionV2Request",
	"GetHypeTrainExecutionV2Response",
	"GetIDFromLoginRequest",
	"GetIDFromLoginResponse",
	"GetPinnedChatRequest",
	"GetPinnedChatResponse",
	"GetRawMediaRequest",
	"GetRawMediaResponse",
	"GetUserIDRequest",
	"GetUserIDResponse",
	"GiftSubscriptionRewardPreviewsRequest",
	"GiftSubscriptionRewardPreviewsResponse",
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
	"GuestStarFavoriteGuestsRequest",
	"GuestStarFavoriteGuestsResponse",
	"HappeningNowSettingsRequest",
	"HappeningNowSettingsResponse",
	"HasNewBountiesContextQueryRequest",
	"HasNewBountiesContextQueryResponse",
	"HomeOfflineCarouselRequest",
	"HomeOfflineCarouselResponse1",
	"HomeOfflineCarouselResponse2",
	"HomeShelfEditorRequest",
	"HomeShelfEditorResponse",
	"HomeShelfGamesRequest",
	"HomeShelfGamesResponse",
	"HomeShelfUsersRequest",
	"HomeShelfUsersResponse",
	"HomeShelfVideosRequest",
	"HomeShelfVideosResponse",
	"HomeTrackQueryRequest",
	"HomeTrackQueryResponse",
	"InventoryRequest",
	"InventoryResponse",
	"LastUnbanRequestRequest",
	"LastUnbanRequestResponse",
	"LiveNotificationsToggle_UserRequest",
	"LiveNotificationsToggle_UserResponse",
	"LowerHomeHeaderRequest",
	"LowerHomeHeaderResponse",
	"MessageBufferChatHistoryRequest1",
	"MessageBufferChatHistoryRequest2",
	"MessageBufferChatHistoryResponse",
	"MessageBuffer_ChannelRequest",
	"MessageBuffer_ChannelResponse",
	"MinimalTopNav_MinimalUserRequest",
	"MinimalTopNav_MinimalUserResponse",
	"NielsenContentMetadataRequest",
	"NielsenContentMetadataResponse1",
	"NielsenContentMetadataResponse2",
	"OfflineBannerOverlayRequest",
	"OfflineBannerOverlayResponse",
	"OneClickEligibilityRequest",
	"OneClickEligibilityResponse",
	"OneTapFeedRequest",
	"OneTapFeedResponse",
	"OnsiteNotifications_ListNotificationsRequest",
	"OnsiteNotifications_ListNotificationsResponse",
	"OnsiteNotifications_SummaryRequest",
	"OnsiteNotifications_SummaryResponse",
	"OnsiteNotifications_ViewRequest",
	"OnsiteNotifications_ViewResponse",
	"PaidPinnedChatRequest",
	"PaidPinnedChatResponse",
	"PartnerPlusPublicQueryRequest",
	"PartnerPlusPublicQueryResponse",
	"PaymentMethodsTab_UserPaymentMethodsRequest",
	"PaymentMethodsTab_UserPaymentMethodsResponse",
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
	"PlatformNotificationSettings_UserRequest",
	"PlatformNotificationSettings_UserResponse",
	"PlaybackAccessTokenRequest",
	"PlaybackAccessTokenResponse1",
	"PlaybackAccessTokenResponse2",
	"PlayerTrackingContextQueryRequest1",
	"PlayerTrackingContextQueryRequest2",
	"PlayerTrackingContextQueryResponse1",
	"PlayerTrackingContextQueryResponse2",
	"PlayerTrackingContextQueryResponse3",
	"PollChannelSettingsRequest",
	"PollChannelSettingsResponse",
	"PrefetchPlaybackAccessTokenRequest",
	"PrefetchPlaybackAccessTokenResponse",
	"Prime_PrimeOfferList_PrimeOffers_EligibilityRequest",
	"Prime_PrimeOfferList_PrimeOffers_EligibilityResponse",
	"Prime_PrimeOffers_CurrentUserRequest",
	"Prime_PrimeOffers_CurrentUserResponse",
	"Prime_PrimeOffers_PrimeOfferIds_EligibilityRequest",
	"Prime_PrimeOffers_PrimeOfferIds_EligibilityResponse",
	"ProductConsentRequest",
	"ProductConsentResponse",
	"ProfileBannerSettingRequest",
	"ProfileBannerSettingResponse",
	"ProfileImageSettingRequest",
	"ProfileImageSettingResponse",
	"RealtimeStreamTagListRequest",
	"RealtimeStreamTagListResponse",
	"RecapEligibilityQueryRequest",
	"RecapEligibilityQueryResponse",
	"ReportMenuItemRequest",
	"ReportMenuItemResponse",
	"ReportUserModal_ReportWizardDataRequest",
	"ReportUserModal_ReportWizardDataResponse",
	"RewardCenter_BitsBalanceRequest",
	"RewardCenter_BitsBalanceResponse",
	"RewardListRequest",
	"RewardListResponse",
	"RoleRestrictedRequest",
	"RoleRestrictedResponse",
	"SearchResultsPage_SearchResultsRequest",
	"SearchResultsPage_SearchResultsResponse",
	"SearchTray_SearchSuggestionsRequest",
	"SearchTray_SearchSuggestionsResponse",
	"SettingsNotificationsPage_UserRequest",
	"SettingsNotificationsPage_UserResponse",
	"SettingsTabs_UserRequest",
	"SettingsTabs_UserResponse",
	"Settings_ChannelClipsSettingsRequest",
	"Settings_ChannelClipsSettingsResponse",
	"Settings_ProfilePage_AccountInfoSettingsRequest",
	"Settings_ProfilePage_AccountInfoSettingsResponse",
	"ShareClipRenderStatusRequest",
	"ShareClipRenderStatusResponse",
	"SharedChatModeratorStrikesRequest",
	"SharedChatModeratorStrikesResponse",
	"SharedChatSessionRequest",
	"SharedChatSessionResponse",
	"ShelvesRequest1",
	"ShelvesRequest2",
	"ShelvesResponse",
	"ShieldModeStateRequest",
	"ShieldModeStateResponse",
	"ShoutoutHighlightServiceQueryRequest",
	"ShoutoutHighlightServiceQueryResponse",
	"SideNavRequest",
	"SideNavResponse",
	"SmartNotificationSettings_UserRequest",
	"SmartNotificationSettings_UserResponse",
	"SocialMediaRequest",
	"SocialMediaResponse",
	"SponsorshipChannelSettingsRequest",
	"SponsorshipChannelSettingsResponse",
	"StoryChannelQueryRequest",
	"StoryChannelQueryResponse",
	"StoryPreviewChannelRequest",
	"StoryPreviewChannelResponse",
	"StoryPreviewsWithOrderRequest",
	"StoryPreviewsWithOrderResponse",
	"StreamChatRequest",
	"StreamChatResponse",
	"StreamEventCelebrationsChannelPageBadgeRequest",
	"StreamEventCelebrationsChannelPageBadgeResponse",
	"StreamEventsActiveCelebrationCalloutQueryRequest",
	"StreamEventsActiveCelebrationCalloutQueryResponse",
	"StreamMetadataRequest",
	"StreamMetadataResponse",
	"StreamRefetchManagerRequest",
	"StreamRefetchManagerResponse",
	"StreamScheduleRequest",
	"StreamScheduleResponse",
	"StreamSummaryPage_GetRecentStreamSessionsRequest",
	"StreamSummaryPage_GetRecentStreamSessionsResponse",
	"StreamTagsTrackingChannelRequest",
	"StreamTagsTrackingChannelResponse",
	"Sub_AnalyticsRequest",
	"Sub_AnalyticsResponse",
	"SubscribedContextRequest",
	"SubscribedContextResponse",
	"SubscriptionRewardPreviewsRequest",
	"SubscriptionRewardPreviewsResponse",
	"SubscriptionsManagement_ExpiredSubscriptionsRequest",
	"SubscriptionsManagement_ExpiredSubscriptionsResponse",
	"SubscriptionsManagement_SubscriptionBenefitsRequest",
	"SubscriptionsManagement_SubscriptionBenefitsResponse",
	"SubsidizedSubscriptionsRequest1",
	"SubsidizedSubscriptionsRequest2",
	"SubsidizedSubscriptionsResponse",
	"SunlightHomePageCardsRequest",
	"SunlightHomePageCardsResponse",
	"SunlightHomePageRequest",
	"SunlightHomePageResponse",
	"SunlightLoggedInUserMenuQueryRequest",
	"SunlightLoggedInUserMenuQueryResponse",
	"SupportPanelCheckoutServiceRequest",
	"SupportPanelCheckoutServiceResponse",
	"SupportPanelCommunityGifting_GifterBadgeProgressRequest",
	"SupportPanelCommunityGifting_GifterBadgeProgressResponse",
	"SupportPanelCommunityGifting_GiftingOptionsRequest",
	"SupportPanelCommunityGifting_GiftingOptionsResponse",
	"SupportPanelFooterPrimeStatusRequest",
	"SupportPanelFooterPrimeStatusResponse",
	"SupportPanelSubTokenBalanceRequest",
	"SupportPanelSubTokenBalanceResponse",
	"SupportPanelSubTokenOffersRequest",
	"SupportPanelSubTokenOffersResponse",
	"SupportPanelSubscribeViewFooterPrimeRequest",
	"SupportPanelSubscribeViewFooterPrimeResponse",
	"SupportPanelTitleSectionAvatarRequest",
	"SupportPanelTitleSectionAvatarResponse",
	"SupportPanelTrackingServiceRequest",
	"SupportPanelTrackingServiceResponse",
	"SyncedSettingsCelebrationsRequest",
	"SyncedSettingsCelebrationsResponse",
	"SyncedSettingsChatPauseSettingRequest",
	"SyncedSettingsChatPauseSettingResponse",
	"SyncedSettingsDeletedMessageDisplaySettingRequest",
	"SyncedSettingsDeletedMessageDisplaySettingResponse",
	"SyncedSettingsEmoteAnimationsRequest",
	"SyncedSettingsEmoteAnimationsResponse",
	"SyncedSettingsReadableChatColorsRequest",
	"SyncedSettingsReadableChatColorsResponse",
	"TaxExpiryQueryRequest",
	"TaxExpiryQueryResponse",
	"TitleMentionsRequest",
	"TitleMentionsResponse",
	"TopNav_CurrentUserRequest",
	"TopNav_CurrentUserResponse",
	"TrackingManager_RequestInfoRequest",
	"TrackingManager_RequestInfoResponse",
	"TurboAndSubUpsellRequest",
	"TurboAndSubUpsellResponse",
	"TurboProductInformationRequest",
	"TurboProductInformationResponse",
	"UnbanRequestsListCtxRequest",
	"UnbanRequestsListCtxResponse",
	"UpcomingScheduleRequest",
	"UpcomingScheduleResponse",
	"UpgradeTermsBannerQueryRequest",
	"UpgradeTermsBannerQueryResponse",
	"UseCreatorHomeActionDataQueryRequest",
	"UseCreatorHomeActionDataQueryResponse",
	"UseLiveBroadcastRequest",
	"UseLiveBroadcastResponse",
	"UseLiveRequest",
	"UseLiveResponse",
	"UseViewCountRequest",
	"UseViewCountResponse",
	"UserDJStatusQueryRequest",
	"UserDJStatusQueryResponse",
	"UserEmotesRequest",
	"UserEmotesResponse",
	"UserEmoticonPrefix_QueryRequest",
	"UserEmoticonPrefix_QueryResponse",
	"UserMenuCurrentUserRequest",
	"UserMenuCurrentUserResponse",
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
	"VideoAdBannerRequest",
	"VideoAdBannerResponse",
	"VideoAdRequestDeclineRequest",
	"VideoAdRequestDeclineResponse",
	"VideoCommentsByOffsetOrCursorRequest1",
	"VideoCommentsByOffsetOrCursorRequest2",
	"VideoCommentsByOffsetOrCursorResponse",
	"VideoCommentsRequest",
	"VideoCommentsResponse",
	"VideoMarkersChatCommandRequest",
	"VideoMarkersChatCommandResponse",
	"VideoMetadataRequest",
	"VideoMetadataResponse",
	"VideoPlayerClipsButtonBroadcasterRequest",
	"VideoPlayerClipsButtonBroadcasterResponse",
	"VideoPlayerOfflineRecommendationsOverlayRequest",
	"VideoPlayerOfflineRecommendationsOverlayResponse",
	"VideoPlayerPixelAnalyticsUrlsRequest",
	"VideoPlayerPixelAnalyticsUrlsResponse",
	"VideoPlayerStatusOverlayChannelRequest",
	"VideoPlayerStatusOverlayChannelResponse",
	"VideoPlayerStreamInfoOverlayChannelRequest",
	"VideoPlayerStreamInfoOverlayChannelResponse",
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
	"WalletBalancesRequest",
	"WalletBalancesResponse",
	"WatchStreakExperimentRequest",
	"WatchStreakExperimentResponse",
	"WatchTrackQueryRequest",
	"WatchTrackQueryResponse1",
	"WatchTrackQueryResponse2",
	"Whispers_Thread_User_ActivityRequest",
	"Whispers_Thread_User_ActivityResponse",
	"Whispers_Thread_WhisperThreadRequest1",
	"Whispers_Thread_WhisperThreadRequest2",
	"Whispers_Thread_WhisperThreadResponse",
	"Whispers_Whispers_UserWhisperThreadsRequest1",
	"Whispers_Whispers_UserWhisperThreadsRequest2",
	"Whispers_Whispers_UserWhisperThreadsResponse",
	"WithIsStreamLiveQueryRequest",
	"WithIsStreamLiveQueryResponse",
	"broadcastLanguageQueryRequest",
	"broadcastLanguageQueryResponse",
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

	def build_query(self, variables: Dict = {}):
		"""Build the query for the endpoint."""
		...

class ConsentRequest(TypedDict):
	id: str
	includeNewCookieConsentFields: Optional[bool]
	includeTCData: Optional[bool]

class ConsentResponseConsentDataDmauserpreferencesData(TypedDict):
	__typename: str
	hasDmaOptIn: Optional[bool]

class ConsentResponseConsentDataGdpruserpreferencesDataFeaturesItem(TypedDict):
	__typename: str
	description: str
	id: str
	illustrations: List[Any]
	name: str

class ConsentResponseConsentDataGdpruserpreferencesDataPurposeItemIabinformationData(TypedDict):
	__typename: str
	description: str
	id: str
	illustrations: List[str]
	name: str

class ConsentResponseConsentDataGdpruserpreferencesDataPurposeItem(TypedDict):
	__typename: str
	consentStatus: str
	hasUserSetConsent: Optional[bool]
	iabInformation: ConsentResponseConsentDataGdpruserpreferencesDataPurposeItemIabinformationData

class ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsItemIabinformationData(TypedDict):
	__typename: str
	description: str
	id: str
	illustrations: List[Any]
	name: str

class ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsItem(TypedDict):
	__typename: str
	consentStatus: str
	hasUserSetConsent: Optional[bool]
	iabInformation: ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsItemIabinformationData

class ConsentResponseConsentDataGdpruserpreferencesDataSpecialpurposeItem(TypedDict):
	__typename: str
	description: str
	id: str
	illustrations: List[str]
	name: str

class ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataPurposeData(TypedDict):
	__typename: str
	consents: Optional[NoneType]
	legitimateInterests: Optional[NoneType]

class ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataVendorData(TypedDict):
	__typename: str
	consents: Optional[NoneType]
	legitimateInterests: Optional[NoneType]

class ConsentResponseConsentDataGdpruserpreferencesDataTcdataData(TypedDict):
	__typename: str
	cmpID: Optional[str]
	cmpVersion: Optional[int]
	hasNonStandardStacks: Optional[bool]
	hasPurposeOneTreatment: Optional[bool]
	ifGDPRApplies: Optional[bool]
	isServiceSpecific: Optional[bool]
	publisherCountryCode: Optional[str]
	purpose: ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataPurposeData
	specialFeatureOptins: Optional[NoneType]
	tcString: Optional[str]
	tcfPolicyVersion: Optional[int]
	vendor: ConsentResponseConsentDataGdpruserpreferencesDataTcdataDataVendorData

class ConsentResponseConsentDataGdpruserpreferencesData(TypedDict):
	__typename: str
	features: List[ConsentResponseConsentDataGdpruserpreferencesDataFeaturesItem]
	hasUserSetPurposeConsent: Optional[bool]
	purpose: List[ConsentResponseConsentDataGdpruserpreferencesDataPurposeItem]
	specialFeatureOptIns: List[ConsentResponseConsentDataGdpruserpreferencesDataSpecialfeatureoptinsItem]
	specialPurpose: List[ConsentResponseConsentDataGdpruserpreferencesDataSpecialpurposeItem]
	tcData: ConsentResponseConsentDataGdpruserpreferencesDataTcdataData

class ConsentResponseConsentDataVendorconsentstatusDataStatusItem(TypedDict):
	__typename: str
	consentStatus: str
	cookieMaxAgeSeconds: Optional[int]
	cookieVendorType: str
	features: List[str]
	flexiblePurposes: List[str]
	hasUserSetConsent: Optional[bool]
	isVisible: Optional[bool]
	name: str
	policyURL: str
	purposes: Optional[NoneType]
	specialFeatures: Optional[NoneType]
	specialPurposes: List[str]

class ConsentResponseConsentDataVendorconsentstatusData(TypedDict):
	__typename: str
	status: List[ConsentResponseConsentDataVendorconsentstatusDataStatusItem]

class ConsentResponseConsentDataVendorstatusItem(TypedDict):
	__typename: str
	consentStatus: str
	hasUserSetConsent: Optional[bool]
	isVisible: Optional[bool]
	name: str

class ConsentResponseConsentData(TypedDict):
	__typename: str
	dmaUserPreferences: ConsentResponseConsentDataDmauserpreferencesData
	gdprUserPreferences: ConsentResponseConsentDataGdpruserpreferencesData
	id: str
	isDeniedUnderage: Optional[bool]
	privacyLawName: str
	shouldShowDismissButton: Optional[bool]
	shouldShowNotification: Optional[bool]
	shouldShowSettingsPage: Optional[bool]
	shouldSkipDmaBanner: Optional[bool]
	vendorConsentStatus: ConsentResponseConsentDataVendorconsentstatusData
	vendorStatus: List[ConsentResponseConsentDataVendorstatusItem]

class ConsentResponse(TypedDict):
	consent: ConsentResponseConsentData

class Ads_Components_AdManager_UserRequest(TypedDict):
	...

class Ads_Components_AdManager_UserResponseCurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str

class Ads_Components_AdManager_UserResponse(TypedDict):
	currentUser: Ads_Components_AdManager_UserResponseCurrentuserData

class Prime_PrimeOffers_CurrentUserRequest(TypedDict):
	...

class Prime_PrimeOffers_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	hasPrime: Optional[bool]
	id: str

class Prime_PrimeOffers_CurrentUserResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class Prime_PrimeOffers_CurrentUserResponse(TypedDict):
	currentUser: Prime_PrimeOffers_CurrentUserResponseCurrentuserData
	requestInfo: Prime_PrimeOffers_CurrentUserResponseRequestinfoData

class UserMenuCurrentUserRequest(TypedDict):
	...

class UserMenuCurrentUserResponseCurrentuserDataSettingsData(TypedDict):
	__typename: str
	isSharingActivity: Optional[bool]
	visibility: str

class UserMenuCurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	availability: Optional[NoneType]
	id: str
	profileImageURL: str
	settings: UserMenuCurrentUserResponseCurrentuserDataSettingsData

class UserMenuCurrentUserResponse(TypedDict):
	currentUser: UserMenuCurrentUserResponseCurrentuserData

class TopNav_CurrentUserRequest(TypedDict):
	...

class TopNav_CurrentUserResponseCurrentuserDataTurbostatusData(TypedDict):
	__typename: str
	hasActiveTurbo: Optional[bool]
	hasUsedFreeTrial: Optional[bool]

class TopNav_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	createdAt: str
	hasPresto: Optional[bool]
	id: str
	turboStatus: TopNav_CurrentUserResponseCurrentuserDataTurbostatusData

class TopNav_CurrentUserResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class TopNav_CurrentUserResponse(TypedDict):
	currentUser: TopNav_CurrentUserResponseCurrentuserData
	requestInfo: TopNav_CurrentUserResponseRequestinfoData

class StoryPreviewsWithOrderRequestInputData(TypedDict):
	capabilities: List[str]
	limit: int
	offset: Optional[int]

class StoryPreviewsWithOrderRequest(TypedDict):
	input: StoryPreviewsWithOrderRequestInputData

class StoryPreviewsWithOrderResponseStorypreviewswithorderData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]
	isFresh: Optional[bool]
	previews: List[Any]

class StoryPreviewsWithOrderResponse(TypedDict):
	storyPreviewsWithOrder: StoryPreviewsWithOrderResponseStorypreviewswithorderData

class SideNavRequestInputDataRecommendationcontextData(TypedDict):
	categorySlug: Optional[NoneType]
	channelName: Optional[NoneType]
	clientApp: str
	lastCategorySlug: Optional[NoneType]
	lastChannelName: Optional[NoneType]
	pageviewContent: Optional[NoneType]
	pageviewContentType: Optional[NoneType]
	pageviewLocation: Optional[NoneType]
	pageviewMedium: Optional[NoneType]
	platform: str
	previousPageviewContent: Optional[NoneType]
	previousPageviewContentType: Optional[NoneType]
	previousPageviewLocation: Optional[NoneType]
	previousPageviewMedium: Optional[NoneType]

class SideNavRequestInputData(TypedDict):
	followSortOrder: str
	recommendationContext: SideNavRequestInputDataRecommendationcontextData
	sectionInputs: List[str]

class SideNavRequest(TypedDict):
	input: SideNavRequestInputData
	creatorAnniversariesFeature: Optional[bool]
	withFreeformTags: Optional[bool]

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	broadcastSettings: SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterDataBroadcastsettingsData
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	slug: str

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterData
	collaborationViewersCount: Optional[NoneType]
	game: SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeDataGameData
	hasHypeTrain: Optional[bool]
	id: str
	type: str
	viewersCount: int

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[str]
	label: str
	node: SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItemNodeData
	promotionsCampaignID: Optional[str]
	socialCue: Optional[str]
	trackingID: str

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentData(TypedDict):
	__typename: str
	edges: List[SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentDataEdgesItem]

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataTitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	text: str

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataTitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataTitleDataLocalizedtitletokensItemNodeData

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataTitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataTitleDataLocalizedtitletokensItem]

class SideNavResponseSidenavDataSectionsDataEdgesItemNodeData(TypedDict):
	__typename: str
	content: SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataContentData
	id: str
	title: SideNavResponseSidenavDataSectionsDataEdgesItemNodeDataTitleData

class SideNavResponseSidenavDataSectionsDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[str]
	node: SideNavResponseSidenavDataSectionsDataEdgesItemNodeData

class SideNavResponseSidenavDataSectionsData(TypedDict):
	__typename: str
	edges: List[SideNavResponseSidenavDataSectionsDataEdgesItem]

class SideNavResponseSidenavData(TypedDict):
	__typename: str
	sections: SideNavResponseSidenavDataSectionsData

class SideNavResponse(TypedDict):
	sideNav: SideNavResponseSidenavData

class FrontPageNew_UserRequest(TypedDict):
	limit: int

class FrontPageNew_UserResponseCurrentuserDataFollowedgamesData(TypedDict):
	__typename: str
	nodes: List[Any]

class FrontPageNew_UserResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]
	isStaff: Optional[NoneType]

class FrontPageNew_UserResponseCurrentuserData(TypedDict):
	__typename: str
	createdAt: str
	followedGames: FrontPageNew_UserResponseCurrentuserDataFollowedgamesData
	id: str
	roles: FrontPageNew_UserResponseCurrentuserDataRolesData

class FrontPageNew_UserResponse(TypedDict):
	currentUser: FrontPageNew_UserResponseCurrentuserData

class ShelvesRequest1ContextData(TypedDict):
	clientApp: str
	location: str
	referrerDomain: Optional[str]
	viewportHeight: int
	viewportWidth: int

class ShelvesRequest1(TypedDict):
	imageWidth: int
	itemsPerRow: int
	platform: str
	limit: int
	requestID: Optional[str]
	includeIsDJ: Optional[bool]
	context: ShelvesRequest1ContextData
	verbose: Optional[bool]

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
	requestID: Optional[str]
	includeIsDJ: Optional[bool]
	context: ShelvesRequest2ContextData
	verbose: Optional[bool]

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	broadcastSettings: ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterDataBroadcastsettingsData
	displayName: str
	id: str
	largeProfileImageURL: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterDataRolesData

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataGameDataGametagsItem(TypedDict):
	__typename: str
	id: str
	isLanguageTag: Optional[bool]
	localizedName: str
	tagName: str

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	categorySlug: str
	displayName: str
	gameTags: List[ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataGameDataGametagsItem]
	id: str
	name: str
	originalReleaseDate: str
	viewersCount: int

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataBroadcasterData
	createdAt: str
	freeformTags: List[ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataFreeformtagsItem]
	game: ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeDataGameData
	id: str
	previewImageURL: str
	type: str
	viewersCount: int

class ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[str]
	node: ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItemNodeData
	promotionsCampaignID: Optional[str]
	sourceType: str
	trackingID: str

class ShelvesResponseShelvesDataEdgesItemNodeDataContentData(TypedDict):
	__typename: str
	edges: List[ShelvesResponseShelvesDataEdgesItemNodeDataContentDataEdgesItem]

class ShelvesResponseShelvesDataEdgesItemNodeDataTitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	location: str
	text: str

class ShelvesResponseShelvesDataEdgesItemNodeDataTitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: ShelvesResponseShelvesDataEdgesItemNodeDataTitleDataLocalizedtitletokensItemNodeData

class ShelvesResponseShelvesDataEdgesItemNodeDataTitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[ShelvesResponseShelvesDataEdgesItemNodeDataTitleDataLocalizedtitletokensItem]

class ShelvesResponseShelvesDataEdgesItemNodeDataTrackinginfoData(TypedDict):
	__typename: str
	reasonTarget: Optional[NoneType]
	reasonTargetType: Optional[NoneType]
	reasonType: Optional[str]
	rowName: str

class ShelvesResponseShelvesDataEdgesItemNodeData(TypedDict):
	__typename: str
	content: ShelvesResponseShelvesDataEdgesItemNodeDataContentData
	id: str
	title: ShelvesResponseShelvesDataEdgesItemNodeDataTitleData
	trackingInfo: ShelvesResponseShelvesDataEdgesItemNodeDataTrackinginfoData

class ShelvesResponseShelvesDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: ShelvesResponseShelvesDataEdgesItemNodeData

class ShelvesResponseShelvesDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class ShelvesResponseShelvesData(TypedDict):
	__typename: str
	edges: List[ShelvesResponseShelvesDataEdgesItem]
	pageInfo: ShelvesResponseShelvesDataPageinfoData
	verboseResults: Optional[NoneType]

class ShelvesResponse(TypedDict):
	shelves: ShelvesResponseShelvesData

class PrefetchPlaybackAccessTokenRequest(TypedDict):
	login: str
	playerType: str
	platform: str

class PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenDataAuthorizationData(TypedDict):
	__typename: str
	forbiddenReasonCode: str
	isForbidden: Optional[bool]

class PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenData(TypedDict):
	__typename: str
	authorization: PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenDataAuthorizationData
	expiresAt: str
	signature: str
	value: str

class PrefetchPlaybackAccessTokenResponse(TypedDict):
	streamPlaybackAccessToken: PrefetchPlaybackAccessTokenResponseStreamplaybackaccesstokenData

class GuestStarBatchCollaborationQueryRequestOptionsData(TypedDict):
	channelIDs: List[str]

class GuestStarBatchCollaborationQueryRequest(TypedDict):
	options: GuestStarBatchCollaborationQueryRequestOptionsData
	canDropInFlagEnabled: Optional[bool]
	openCallingFlagEnabled: Optional[bool]

class GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationItem(TypedDict):
	__typename: str
	canJoinStatus: str
	id: str
	isFavorite: Optional[bool]
	session: Optional[NoneType]

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsItem(TypedDict):
	__typename: str
	canJoinStatus: str
	id: str
	isFavorite: Optional[bool]
	session: Optional[NoneType]

class GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesData(TypedDict):
	__typename: str
	channelCollabs: List[GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsItem]
	shouldRefetch: Optional[bool]
	shouldSubscribeToUpdates: Optional[bool]

class GuestStarBatchCollaborationQueryResponse(TypedDict):
	guestStarChannelCollaboration: List[GuestStarBatchCollaborationQueryResponseGueststarchannelcollaborationItem]
	guestStarCollaborationStatuses: GuestStarBatchCollaborationQueryResponseGueststarcollaborationstatusesData

class CoreActionsCurrentUserRequest(TypedDict):
	...

class CoreActionsCurrentUserResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isStaff: Optional[NoneType]

class CoreActionsCurrentUserResponseCurrentuserDataSettingsData(TypedDict):
	__typename: str
	preferredLanguageTag: str

class CoreActionsCurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	roles: CoreActionsCurrentUserResponseCurrentuserDataRolesData
	settings: CoreActionsCurrentUserResponseCurrentuserDataSettingsData

class CoreActionsCurrentUserResponse(TypedDict):
	currentUser: CoreActionsCurrentUserResponseCurrentuserData

class FeaturedContentCarouselStreamsRequest(TypedDict):
	language: str
	first: int
	acceptedMature: Optional[bool]

class FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	slug: str

class FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamData(TypedDict):
	__typename: str
	broadcaster: FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamDataBroadcasterData
	freeformTags: List[FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamDataFreeformtagsItem]
	game: FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamDataGameData
	id: str
	previewImageURL: str
	type: str
	viewersCount: int

class FeaturedContentCarouselStreamsResponseFeaturedstreamsItem(TypedDict):
	__typename: str
	description: Optional[str]
	isScheduled: Optional[bool]
	isSponsored: Optional[bool]
	itemTrackingID: str
	priorityLevel: int
	stream: FeaturedContentCarouselStreamsResponseFeaturedstreamsItemStreamData
	title: Optional[str]
	version: int

class FeaturedContentCarouselStreamsResponse(TypedDict):
	featuredStreams: List[FeaturedContentCarouselStreamsResponseFeaturedstreamsItem]

class TrackingManager_RequestInfoRequest(TypedDict):
	...

class TrackingManager_RequestInfoResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str
	ipAddress: str

class TrackingManager_RequestInfoResponse(TypedDict):
	requestInfo: TrackingManager_RequestInfoResponseRequestinfoData

class Prime_PrimeOffers_PrimeOfferIds_EligibilityRequest(TypedDict):
	...

class Prime_PrimeOffers_PrimeOfferIds_EligibilityResponsePrimeofferswithouteligibilityItem(TypedDict):
	__typename: str
	catalogOfferID: str
	id: str

class Prime_PrimeOffers_PrimeOfferIds_EligibilityResponse(TypedDict):
	primeOffersWithoutEligibility: List[Prime_PrimeOffers_PrimeOfferIds_EligibilityResponsePrimeofferswithouteligibilityItem]

class ChannelPage_SetSessionStatusRequestInputData(TypedDict):
	activity: Optional[NoneType]
	availability: str
	sessionID: str

class ChannelPage_SetSessionStatusRequest(TypedDict):
	input: ChannelPage_SetSessionStatusRequestInputData

class ChannelPage_SetSessionStatusResponseSetsessionstatusData(TypedDict):
	__typename: str
	setAgainInSeconds: int

class ChannelPage_SetSessionStatusResponse(TypedDict):
	setSessionStatus: ChannelPage_SetSessionStatusResponseSetsessionstatusData

class Core_Services_Spade_CurrentUserRequest(TypedDict):
	...

class Core_Services_Spade_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	hasPrime: Optional[bool]
	hasTurbo: Optional[bool]
	id: str
	language: str
	login: str

class Core_Services_Spade_CurrentUserResponse(TypedDict):
	currentUser: Core_Services_Spade_CurrentUserResponseCurrentuserData

class DMCAViolationCountBannerRequest(TypedDict):
	id: str

class DMCAViolationCountBannerResponseUserData(TypedDict):
	__typename: str
	dmcaViolationCount: Optional[NoneType]
	id: str
	login: str

class DMCAViolationCountBannerResponse(TypedDict):
	user: DMCAViolationCountBannerResponseUserData

class VerifyEmail_CurrentUserRequest(TypedDict):
	...

class VerifyEmail_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	displayName: str
	email: str
	hasPrime: Optional[bool]
	id: str
	isEmailVerified: Optional[bool]

class VerifyEmail_CurrentUserResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class VerifyEmail_CurrentUserResponse(TypedDict):
	currentUser: VerifyEmail_CurrentUserResponseCurrentuserData
	requestInfo: VerifyEmail_CurrentUserResponseRequestinfoData

class OnsiteNotifications_SummaryRequest(TypedDict):
	...

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataCreatorunreadsummaryData(TypedDict):
	__typename: str
	unreadCount: Optional[int]

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataViewerunreadsummaryData(TypedDict):
	__typename: str
	lastReadAllAt: Optional[NoneType]
	unreadCount: Optional[int]

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryData(TypedDict):
	__typename: str
	creatorUnreadSummary: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataCreatorunreadsummaryData
	lastSeenAt: Optional[NoneType]
	unseenCount: Optional[int]
	viewerUnreadSummary: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryDataViewerunreadsummaryData

class OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsData(TypedDict):
	__typename: str
	summary: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsDataSummaryData

class OnsiteNotifications_SummaryResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	notifications: OnsiteNotifications_SummaryResponseCurrentuserDataNotificationsData

class OnsiteNotifications_SummaryResponse(TypedDict):
	currentUser: OnsiteNotifications_SummaryResponseCurrentuserData

class Whispers_Whispers_UserWhisperThreadsRequest1(TypedDict):
	...

class Whispers_Whispers_UserWhisperThreadsRequest2(TypedDict):
	cursor: Optional[NoneType]

class Whispers_Whispers_UserWhisperThreadsResponseCurrentuserDataWhisperthreadsData(TypedDict):
	__typename: str
	edges: List[Any]

class Whispers_Whispers_UserWhisperThreadsResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str
	whisperThreads: Whispers_Whispers_UserWhisperThreadsResponseCurrentuserDataWhisperthreadsData

class Whispers_Whispers_UserWhisperThreadsResponse(TypedDict):
	currentUser: Whispers_Whispers_UserWhisperThreadsResponseCurrentuserData

class ConnectAdIdentityMutationRequestInputData(TypedDict):
	targetDeviceID: str

class ConnectAdIdentityMutationRequest(TypedDict):
	input: ConnectAdIdentityMutationRequestInputData

class ConnectAdIdentityMutationResponseConnectadidentityData(TypedDict):
	__typename: str
	identityURL: str

class ConnectAdIdentityMutationResponse(TypedDict):
	connectAdIdentity: ConnectAdIdentityMutationResponseConnectadidentityData

class VideoPreviewOverlayRequest(TypedDict):
	login: str

class VideoPreviewOverlayResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str
	previewImageURL: str
	restrictionType: Optional[NoneType]

class VideoPreviewOverlayResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: VideoPreviewOverlayResponseUserDataStreamData

class VideoPreviewOverlayResponse(TypedDict):
	user: VideoPreviewOverlayResponseUserData

class VideoAdBannerRequestInputData(TypedDict):
	login: str
	ownsCollectionID: Optional[str]
	ownsVideoID: Optional[str]

class VideoAdBannerRequest(TypedDict):
	input: VideoAdBannerRequestInputData

class VideoAdBannerResponseUserbyattributeDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]

class VideoAdBannerResponseUserbyattributeData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str
	roles: VideoAdBannerResponseUserbyattributeDataRolesData

class VideoAdBannerResponse(TypedDict):
	userByAttribute: VideoAdBannerResponseUserbyattributeData

class ContentPolicyPropertiesQueryRequest(TypedDict):
	login: str
	vodID: Optional[str]
	isLive: Optional[bool]
	isVOD: Optional[bool]

class ContentPolicyPropertiesQueryResponse1UserDataStreamDataContentpolicypropertiesData(TypedDict):
	__typename: str
	hasBrandedContent: Optional[bool]

class ContentPolicyPropertiesQueryResponse1UserDataStreamData(TypedDict):
	__typename: str
	contentPolicyProperties: ContentPolicyPropertiesQueryResponse1UserDataStreamDataContentpolicypropertiesData
	id: str

class ContentPolicyPropertiesQueryResponse1UserData(TypedDict):
	__typename: str
	id: str
	stream: ContentPolicyPropertiesQueryResponse1UserDataStreamData

class ContentPolicyPropertiesQueryResponse1(TypedDict):
	user: ContentPolicyPropertiesQueryResponse1UserData

class ContentPolicyPropertiesQueryResponse2VideoDataContentpolicypropertiesData(TypedDict):
	__typename: str
	hasBrandedContent: Optional[bool]

class ContentPolicyPropertiesQueryResponse2VideoDataOwnerData(TypedDict):
	__typename: str
	id: str
	login: str

class ContentPolicyPropertiesQueryResponse2VideoData(TypedDict):
	__typename: str
	broadcastType: str
	contentPolicyProperties: ContentPolicyPropertiesQueryResponse2VideoDataContentpolicypropertiesData
	id: str
	owner: ContentPolicyPropertiesQueryResponse2VideoDataOwnerData

class ContentPolicyPropertiesQueryResponse2(TypedDict):
	video: ContentPolicyPropertiesQueryResponse2VideoData

class GetUserIDRequest(TypedDict):
	login: str
	lookupType: str

class GetUserIDResponseUserData(TypedDict):
	__typename: str
	id: str

class GetUserIDResponse(TypedDict):
	user: GetUserIDResponseUserData

class VideoPlayer_AgeGateOverlayBroadcasterRequestInputData(TypedDict):
	login: str
	ownsVideoID: Optional[NoneType]

class VideoPlayer_AgeGateOverlayBroadcasterRequest(TypedDict):
	input: VideoPlayer_AgeGateOverlayBroadcasterRequestInputData

class VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeDataAdpropertiesData(TypedDict):
	__typename: str
	requiredAge: Optional[int]

class VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeData(TypedDict):
	__typename: str
	adProperties: VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeDataAdpropertiesData
	id: str
	login: str

class VideoPlayer_AgeGateOverlayBroadcasterResponse(TypedDict):
	userByAttribute: VideoPlayer_AgeGateOverlayBroadcasterResponseUserbyattributeData

class VideoPlayer_VideoSourceManagerRequestInputData(TypedDict):
	broadcasterOfClipSlug: Optional[NoneType]
	login: str
	ownsCollectionID: Optional[NoneType]
	ownsVideoID: Optional[NoneType]

class VideoPlayer_VideoSourceManagerRequest(TypedDict):
	input: VideoPlayer_VideoSourceManagerRequestInputData

class VideoPlayer_VideoSourceManagerResponseUserbyattributeData(TypedDict):
	__typename: str
	id: str

class VideoPlayer_VideoSourceManagerResponse(TypedDict):
	userByAttribute: VideoPlayer_VideoSourceManagerResponseUserbyattributeData

class VideoPlayerPixelAnalyticsUrlsRequest(TypedDict):
	login: str
	allowAmazon: Optional[bool]
	allowComscore: Optional[bool]
	allowGoogle: Optional[bool]
	allowNielsen: Optional[bool]

class VideoPlayerPixelAnalyticsUrlsResponseChannelDataAdpropertiesData(TypedDict):
	__typename: str
	trackingPixels: List[Any]

class VideoPlayerPixelAnalyticsUrlsResponseChannelData(TypedDict):
	__typename: str
	adProperties: VideoPlayerPixelAnalyticsUrlsResponseChannelDataAdpropertiesData
	id: str

class VideoPlayerPixelAnalyticsUrlsResponse(TypedDict):
	channel: VideoPlayerPixelAnalyticsUrlsResponseChannelData

class StreamRefetchManagerRequest(TypedDict):
	channel: str

class StreamRefetchManagerResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str
	isEncrypted: Optional[bool]

class StreamRefetchManagerResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: StreamRefetchManagerResponseUserDataStreamData

class StreamRefetchManagerResponse(TypedDict):
	user: StreamRefetchManagerResponseUserData

class AdRequestHandlingRequest(TypedDict):
	isLive: Optional[bool]
	login: str
	isVOD: Optional[bool]
	vodID: Optional[str]
	isCollection: Optional[bool]
	collectionID: Optional[str]

class AdRequestHandlingResponse1CurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str

class AdRequestHandlingResponse1UserDataAdpropertiesData(TypedDict):
	__typename: str
	adServerDefault: str
	hasPostrollsDisabled: Optional[bool]
	hasPrerollsDisabled: Optional[bool]
	hasVodAdsEnabled: Optional[bool]
	vodArchiveMidrolls: str

class AdRequestHandlingResponse1UserDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	isMature: Optional[bool]

class AdRequestHandlingResponse1UserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]

class AdRequestHandlingResponse1UserDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class AdRequestHandlingResponse1UserDataStreamDataGameDataTagsItem(TypedDict):
	__typename: str
	id: str
	tagName: str

class AdRequestHandlingResponse1UserDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str
	tags: List[AdRequestHandlingResponse1UserDataStreamDataGameDataTagsItem]

class AdRequestHandlingResponse1UserDataStreamData(TypedDict):
	__typename: str
	broadcasterSoftware: str
	game: AdRequestHandlingResponse1UserDataStreamDataGameData
	id: str
	tags: List[Any]

class AdRequestHandlingResponse1UserData(TypedDict):
	__typename: str
	adProperties: AdRequestHandlingResponse1UserDataAdpropertiesData
	broadcastSettings: AdRequestHandlingResponse1UserDataBroadcastsettingsData
	id: str
	login: str
	roles: AdRequestHandlingResponse1UserDataRolesData
	self: AdRequestHandlingResponse1UserDataSelfData
	stream: AdRequestHandlingResponse1UserDataStreamData

class AdRequestHandlingResponse1(TypedDict):
	currentUser: AdRequestHandlingResponse1CurrentuserData
	user: AdRequestHandlingResponse1UserData

class AdRequestHandlingResponse2CurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str

class AdRequestHandlingResponse2VideoDataContentclassificationlabelsItem(TypedDict):
	__typename: str
	id: str
	isEnabled: Optional[bool]

class AdRequestHandlingResponse2VideoDataGameDataTagsItem(TypedDict):
	__typename: str
	id: str
	tagName: str

class AdRequestHandlingResponse2VideoDataGameData(TypedDict):
	__typename: str
	id: str
	name: str
	tags: List[AdRequestHandlingResponse2VideoDataGameDataTagsItem]

class AdRequestHandlingResponse2VideoDataOwnerDataAdpropertiesData(TypedDict):
	__typename: str
	adServerDefault: str
	hasPostrollsDisabled: Optional[bool]
	hasPrerollsDisabled: Optional[bool]
	hasVodAdsEnabled: Optional[bool]
	vodArchiveMidrolls: str

class AdRequestHandlingResponse2VideoDataOwnerDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	isMature: Optional[bool]

class AdRequestHandlingResponse2VideoDataOwnerDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]

class AdRequestHandlingResponse2VideoDataOwnerDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class AdRequestHandlingResponse2VideoDataOwnerDataStreamDataGameDataTagsItem(TypedDict):
	__typename: str
	id: str
	tagName: str

class AdRequestHandlingResponse2VideoDataOwnerDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str
	tags: List[AdRequestHandlingResponse2VideoDataOwnerDataStreamDataGameDataTagsItem]

class AdRequestHandlingResponse2VideoDataOwnerDataStreamData(TypedDict):
	__typename: str
	broadcasterSoftware: str
	game: AdRequestHandlingResponse2VideoDataOwnerDataStreamDataGameData
	id: str
	tags: List[Any]

class AdRequestHandlingResponse2VideoDataOwnerData(TypedDict):
	__typename: str
	adProperties: AdRequestHandlingResponse2VideoDataOwnerDataAdpropertiesData
	broadcastSettings: AdRequestHandlingResponse2VideoDataOwnerDataBroadcastsettingsData
	id: str
	login: str
	roles: AdRequestHandlingResponse2VideoDataOwnerDataRolesData
	self: AdRequestHandlingResponse2VideoDataOwnerDataSelfData
	stream: AdRequestHandlingResponse2VideoDataOwnerDataStreamData

class AdRequestHandlingResponse2VideoData(TypedDict):
	__typename: str
	broadcastType: str
	contentClassificationLabels: List[AdRequestHandlingResponse2VideoDataContentclassificationlabelsItem]
	contentTags: List[Any]
	game: AdRequestHandlingResponse2VideoDataGameData
	id: str
	lengthSeconds: int
	owner: AdRequestHandlingResponse2VideoDataOwnerData
	title: str

class AdRequestHandlingResponse2(TypedDict):
	currentUser: AdRequestHandlingResponse2CurrentuserData
	video: AdRequestHandlingResponse2VideoData

class NielsenContentMetadataRequest(TypedDict):
	isCollectionContent: Optional[bool]
	isLiveContent: Optional[bool]
	isVODContent: Optional[bool]
	collectionID: Optional[str]
	login: str
	vodID: Optional[str]

class NielsenContentMetadataResponse1UserDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class NielsenContentMetadataResponse1UserDataStreamDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str

class NielsenContentMetadataResponse1UserDataStreamData(TypedDict):
	__typename: str
	createdAt: str
	game: NielsenContentMetadataResponse1UserDataStreamDataGameData
	id: str

class NielsenContentMetadataResponse1UserData(TypedDict):
	__typename: str
	broadcastSettings: NielsenContentMetadataResponse1UserDataBroadcastsettingsData
	id: str
	stream: NielsenContentMetadataResponse1UserDataStreamData

class NielsenContentMetadataResponse1(TypedDict):
	user: NielsenContentMetadataResponse1UserData

class NielsenContentMetadataResponse2VideoDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str

class NielsenContentMetadataResponse2VideoDataOwnerData(TypedDict):
	__typename: str
	id: str
	login: str

class NielsenContentMetadataResponse2VideoData(TypedDict):
	__typename: str
	createdAt: str
	game: NielsenContentMetadataResponse2VideoDataGameData
	id: str
	owner: NielsenContentMetadataResponse2VideoDataOwnerData
	title: str

class NielsenContentMetadataResponse2(TypedDict):
	video: NielsenContentMetadataResponse2VideoData

class ChannelSkinsRequestSponsorshipsparamsDataPreviewoverrideData(TypedDict):
	campaignOverride: Optional[str]
	dspCreativeOverride: Optional[str]
	productInstanceOverride: Optional[str]

class ChannelSkinsRequestSponsorshipsparamsData(TypedDict):
	deviceMake: Optional[str]
	deviceOS: Optional[str]
	deviceType: str
	platform: str
	previewOverride: ChannelSkinsRequestSponsorshipsparamsDataPreviewoverrideData

class ChannelSkinsRequest(TypedDict):
	channelLogin: str
	sponsorshipsParams: ChannelSkinsRequestSponsorshipsparamsData

class ChannelSkinsResponseChannelData(TypedDict):
	__typename: str
	id: str
	sponsorships: Optional[NoneType]

class ChannelSkinsResponseUserDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class ChannelSkinsResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	self: ChannelSkinsResponseUserDataSelfData

class ChannelSkinsResponseCurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str

class ChannelSkinsResponseRequestinfoData(TypedDict):
	__typename: str
	countryCodeAlpha2: str

class ChannelSkinsResponse(TypedDict):
	channel: ChannelSkinsResponseChannelData
	user: ChannelSkinsResponseUserData
	currentUser: ChannelSkinsResponseCurrentuserData
	requestInfo: ChannelSkinsResponseRequestinfoData

class ExtensionsUIContext_ChannelIDRequest(TypedDict):
	channelLogin: str

class ExtensionsUIContext_ChannelIDResponseUserData(TypedDict):
	__typename: str
	id: str

class ExtensionsUIContext_ChannelIDResponse(TypedDict):
	user: ExtensionsUIContext_ChannelIDResponseUserData

class PlayerTrackingContextQueryRequest1(TypedDict):
	channel: str
	isLive: Optional[bool]
	hasCollection: Optional[bool]
	collectionID: Optional[str]
	videoID: Optional[str]
	hasVideo: Optional[bool]
	slug: Optional[str]
	hasClip: Optional[bool]

class PlayerTrackingContextQueryRequest2(TypedDict):
	isLive: Optional[bool]
	hasCollection: Optional[bool]
	collectionID: Optional[str]
	videoID: str
	hasVideo: Optional[bool]
	slug: Optional[str]
	hasClip: Optional[bool]

class PlayerTrackingContextQueryResponse1CurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str
	isStaff: Optional[bool]
	login: str

class PlayerTrackingContextQueryResponse1UserDataBroadcastsettingsDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class PlayerTrackingContextQueryResponse1UserDataBroadcastsettingsData(TypedDict):
	__typename: str
	game: PlayerTrackingContextQueryResponse1UserDataBroadcastsettingsDataGameData
	id: str

class PlayerTrackingContextQueryResponse1UserDataSelfData(TypedDict):
	__typename: str
	follower: Optional[NoneType]
	isModerator: Optional[bool]
	subscriptionBenefit: Optional[NoneType]

class PlayerTrackingContextQueryResponse1UserDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class PlayerTrackingContextQueryResponse1UserDataStreamData(TypedDict):
	__typename: str
	broadcasterSoftware: str
	game: PlayerTrackingContextQueryResponse1UserDataStreamDataGameData
	id: str
	restriction: Optional[NoneType]

class PlayerTrackingContextQueryResponse1UserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	hasAdFree: Optional[bool]
	id: str

class PlayerTrackingContextQueryResponse1UserData(TypedDict):
	__typename: str
	broadcastSettings: PlayerTrackingContextQueryResponse1UserDataBroadcastsettingsData
	id: str
	isPartner: Optional[bool]
	login: str
	self: PlayerTrackingContextQueryResponse1UserDataSelfData
	stream: PlayerTrackingContextQueryResponse1UserDataStreamData
	subscriptionProducts: List[PlayerTrackingContextQueryResponse1UserDataSubscriptionproductsItem]

class PlayerTrackingContextQueryResponse1(TypedDict):
	currentUser: PlayerTrackingContextQueryResponse1CurrentuserData
	user: PlayerTrackingContextQueryResponse1UserData

class PlayerTrackingContextQueryResponse2CurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str
	isStaff: Optional[bool]
	login: str

class PlayerTrackingContextQueryResponse2VideoDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class PlayerTrackingContextQueryResponse2VideoDataOwnerData(TypedDict):
	__typename: str
	id: str
	isPartner: Optional[bool]
	login: str

class PlayerTrackingContextQueryResponse2VideoData(TypedDict):
	__typename: str
	broadcastType: str
	game: PlayerTrackingContextQueryResponse2VideoDataGameData
	id: str
	owner: PlayerTrackingContextQueryResponse2VideoDataOwnerData

class PlayerTrackingContextQueryResponse2(TypedDict):
	currentUser: PlayerTrackingContextQueryResponse2CurrentuserData
	video: PlayerTrackingContextQueryResponse2VideoData

class PlayerTrackingContextQueryResponse3CurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str
	isStaff: Optional[bool]
	login: str

class PlayerTrackingContextQueryResponse3ClipDataBroadcasterData(TypedDict):
	__typename: str
	id: str
	isPartner: Optional[bool]
	login: str

class PlayerTrackingContextQueryResponse3ClipDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class PlayerTrackingContextQueryResponse3ClipData(TypedDict):
	__typename: str
	broadcaster: PlayerTrackingContextQueryResponse3ClipDataBroadcasterData
	game: PlayerTrackingContextQueryResponse3ClipDataGameData
	id: str

class PlayerTrackingContextQueryResponse3(TypedDict):
	currentUser: PlayerTrackingContextQueryResponse3CurrentuserData
	clip: PlayerTrackingContextQueryResponse3ClipData

class ContentClassificationContextRequest1(TypedDict):
	clipSlug: Optional[str]
	isStream: Optional[bool]
	isClip: Optional[bool]
	isVOD: Optional[bool]
	login: str

class ContentClassificationContextRequest2(TypedDict):
	clipSlug: Optional[str]
	isStream: Optional[bool]
	isClip: Optional[bool]
	isVOD: Optional[bool]
	vodID: str

class ContentClassificationContextRequest3(TypedDict):
	clipSlug: str
	isStream: Optional[bool]
	isClip: Optional[bool]
	isVOD: Optional[bool]

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	__typename: str
	contentGate: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	__typename: str
	contentClassificationLabels: List[Any]
	signPost: str

class ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesData(TypedDict):
	__typename: str
	contentGateProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData
	signPostProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData

class ContentClassificationContextResponse1UserDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class ContentClassificationContextResponse1UserDataStreamData(TypedDict):
	__typename: str
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse1UserDataStreamDataContentclassificationlabelpolicypropertiesData
	contentClassificationLabels: List[Any]
	game: ContentClassificationContextResponse1UserDataStreamDataGameData
	id: str

class ContentClassificationContextResponse1UserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	stream: ContentClassificationContextResponse1UserDataStreamData

class ContentClassificationContextResponse1(TypedDict):
	user: ContentClassificationContextResponse1UserData

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	__typename: str
	contentGate: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	__typename: str
	contentClassificationLabels: List[str]
	signPost: str

class ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesData(TypedDict):
	__typename: str
	contentGateProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData
	signPostProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData

class ContentClassificationContextResponse2VideoDataContentclassificationlabelsItem(TypedDict):
	__typename: str
	id: str
	localizedName: str

class ContentClassificationContextResponse2VideoDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class ContentClassificationContextResponse2VideoDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ContentClassificationContextResponse2VideoData(TypedDict):
	__typename: str
	broadcastType: str
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse2VideoDataContentclassificationlabelpolicypropertiesData
	contentClassificationLabels: List[ContentClassificationContextResponse2VideoDataContentclassificationlabelsItem]
	game: ContentClassificationContextResponse2VideoDataGameData
	id: str
	owner: ContentClassificationContextResponse2VideoDataOwnerData

class ContentClassificationContextResponse2(TypedDict):
	video: ContentClassificationContextResponse2VideoData

class ContentClassificationContextResponse3ClipDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData(TypedDict):
	__typename: str
	contentGate: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData(TypedDict):
	__typename: str
	contentClassificationLabels: List[str]
	signPost: str

class ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesData(TypedDict):
	__typename: str
	contentGateProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataContentgatepropertiesData
	signPostProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesDataSignpostpropertiesData

class ContentClassificationContextResponse3ClipDataContentclassificationlabelsItem(TypedDict):
	__typename: str
	id: str
	localizedName: str

class ContentClassificationContextResponse3ClipDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class ContentClassificationContextResponse3ClipData(TypedDict):
	__typename: str
	broadcaster: ContentClassificationContextResponse3ClipDataBroadcasterData
	contentClassificationLabelPolicyProperties: ContentClassificationContextResponse3ClipDataContentclassificationlabelpolicypropertiesData
	contentClassificationLabels: List[ContentClassificationContextResponse3ClipDataContentclassificationlabelsItem]
	game: ContentClassificationContextResponse3ClipDataGameData
	id: str
	slug: str

class ContentClassificationContextResponse3(TypedDict):
	clip: ContentClassificationContextResponse3ClipData

class VideoPlayerStreamMetadataRequest(TypedDict):
	channel: str

class VideoPlayerStreamMetadataResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str
	isEncrypted: Optional[bool]

class VideoPlayerStreamMetadataResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: VideoPlayerStreamMetadataResponseUserDataStreamData

class VideoPlayerStreamMetadataResponse(TypedDict):
	user: VideoPlayerStreamMetadataResponseUserData

class ActiveWatchPartyRequest(TypedDict):
	channelLogin: str

class ActiveWatchPartyResponseUserData(TypedDict):
	__typename: str
	id: str
	watchParty: Optional[NoneType]

class ActiveWatchPartyResponse(TypedDict):
	user: ActiveWatchPartyResponseUserData

class VideoPlayerClipsButtonBroadcasterRequestInputData(TypedDict):
	login: str
	ownsVideoID: Optional[NoneType]

class VideoPlayerClipsButtonBroadcasterRequest(TypedDict):
	input: VideoPlayerClipsButtonBroadcasterRequestInputData

class VideoPlayerClipsButtonBroadcasterResponseUserbyattributeDataStreamData(TypedDict):
	__typename: str
	id: str
	isEncrypted: Optional[bool]

class VideoPlayerClipsButtonBroadcasterResponseUserbyattributeData(TypedDict):
	__typename: str
	id: str
	login: str
	stream: VideoPlayerClipsButtonBroadcasterResponseUserbyattributeDataStreamData

class VideoPlayerClipsButtonBroadcasterResponse(TypedDict):
	userByAttribute: VideoPlayerClipsButtonBroadcasterResponseUserbyattributeData

class SyncedSettingsCelebrationsRequest(TypedDict):
	...

class SyncedSettingsCelebrationsResponseCurrentuserDataChatuisettingsData(TypedDict):
	__typename: str
	isCelebrationsEnabled: Optional[bool]

class SyncedSettingsCelebrationsResponseCurrentuserData(TypedDict):
	__typename: str
	chatUISettings: SyncedSettingsCelebrationsResponseCurrentuserDataChatuisettingsData
	id: str

class SyncedSettingsCelebrationsResponse(TypedDict):
	currentUser: SyncedSettingsCelebrationsResponseCurrentuserData

class CelebrationContextChannelIDRequest(TypedDict):
	channelLogin: str

class CelebrationContextChannelIDResponseChannelData(TypedDict):
	__typename: str
	id: str

class CelebrationContextChannelIDResponse(TypedDict):
	channel: CelebrationContextChannelIDResponseChannelData

class GetDisplayNameRequest(TypedDict):
	login: str

class GetDisplayNameResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class GetDisplayNameResponse(TypedDict):
	user: GetDisplayNameResponseUserData

class PlaybackAccessTokenRequest(TypedDict):
	isLive: Optional[bool]
	login: str
	isVod: Optional[bool]
	vodID: Optional[str]
	playerType: str
	platform: str

class PlaybackAccessTokenResponse1StreamplaybackaccesstokenDataAuthorizationData(TypedDict):
	__typename: str
	forbiddenReasonCode: str
	isForbidden: Optional[bool]

class PlaybackAccessTokenResponse1StreamplaybackaccesstokenData(TypedDict):
	__typename: str
	authorization: PlaybackAccessTokenResponse1StreamplaybackaccesstokenDataAuthorizationData
	signature: str
	value: str

class PlaybackAccessTokenResponse1(TypedDict):
	streamPlaybackAccessToken: PlaybackAccessTokenResponse1StreamplaybackaccesstokenData

class PlaybackAccessTokenResponse2VideoplaybackaccesstokenData(TypedDict):
	__typename: str
	signature: str
	value: str

class PlaybackAccessTokenResponse2(TypedDict):
	videoPlaybackAccessToken: PlaybackAccessTokenResponse2VideoplaybackaccesstokenData

class ExtensionsForChannelRequest(TypedDict):
	channelID: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemHelixtokenData(TypedDict):
	__typename: str
	extensionID: str
	jwt: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataAbilitiesData(TypedDict):
	__typename: str
	isBitsEnabled: Optional[bool]
	isChatEnabled: Optional[bool]
	isSubscriptionStatusAvailable: Optional[bool]

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataActivationconfigData(TypedDict):
	__typename: str
	anchor: str
	slot: str
	state: str
	x: Optional[NoneType]
	y: Optional[NoneType]

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataIconurlsData(TypedDict):
	__typename: str
	discoverySplash: str
	square100: str
	square24: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataConfigData(TypedDict):
	__typename: str
	canLinkExternalContent: Optional[bool]
	viewerURL: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataLiveconfigData(TypedDict):
	__typename: str
	canLinkExternalContent: Optional[bool]
	viewerURL: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataMobileData(TypedDict):
	__typename: str
	viewerURL: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataVideooverlayData(TypedDict):
	__typename: str
	canLinkExternalContent: Optional[bool]
	viewerURL: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsData(TypedDict):
	__typename: str
	component: Optional[NoneType]
	config: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataConfigData
	hidden: Optional[NoneType]
	liveConfig: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataLiveconfigData
	mobile: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataMobileData
	panel: Optional[NoneType]
	videoOverlay: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsDataVideooverlayData

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionData(TypedDict):
	__typename: str
	allowlistedConfigURLs: List[Any]
	allowlistedPanelURLs: List[Any]
	authorName: str
	clientID: str
	description: str
	hasIdentityLinking: Optional[bool]
	iconURLs: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataIconurlsData
	id: str
	isBitsEnabled: Optional[bool]
	name: str
	sku: Optional[str]
	state: str
	summary: str
	vendorCode: Optional[str]
	version: str
	views: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionDataViewsData

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataSelfData(TypedDict):
	__typename: str
	canActivate: Optional[bool]

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationData(TypedDict):
	__typename: str
	abilities: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataAbilitiesData
	activationConfig: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataActivationconfigData
	extension: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataExtensionData
	id: str
	self: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationDataSelfData

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemTokenData(TypedDict):
	__typename: str
	extensionID: str
	jwt: str

class ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItem(TypedDict):
	__typename: str
	configuration: Optional[NoneType]
	helixToken: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemHelixtokenData
	installation: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemInstallationData
	issuedAt: str
	token: ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItemTokenData

class ExtensionsForChannelResponseUserDataChannelData(TypedDict):
	__typename: str
	id: str
	selfInstalledExtensions: List[ExtensionsForChannelResponseUserDataChannelDataSelfinstalledextensionsItem]

class ExtensionsForChannelResponseUserData(TypedDict):
	__typename: str
	channel: ExtensionsForChannelResponseUserDataChannelData
	id: str

class ExtensionsForChannelResponse(TypedDict):
	user: ExtensionsForChannelResponseUserData

class CelebrationEmotesRequest(TypedDict):
	channelID: str

class CelebrationEmotesResponseUserDataSubscriptionproductsItemEmotegroupsItemEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	setID: str
	token: str

class CelebrationEmotesResponseUserDataSubscriptionproductsItemEmotegroupsItem(TypedDict):
	__typename: str
	emotes: List[CelebrationEmotesResponseUserDataSubscriptionproductsItemEmotegroupsItemEmotesItem]
	id: str

class CelebrationEmotesResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	emoteGroups: List[CelebrationEmotesResponseUserDataSubscriptionproductsItemEmotegroupsItem]
	id: str
	tier: str

class CelebrationEmotesResponseUserData(TypedDict):
	__typename: str
	id: str
	subscriptionProducts: List[CelebrationEmotesResponseUserDataSubscriptionproductsItem]

class CelebrationEmotesResponse(TypedDict):
	user: CelebrationEmotesResponseUserData

class ChannelProductsWithCommunityGiftOffersRequest(TypedDict):
	channelID: Optional[str]

class ChannelProductsWithCommunityGiftOffersResponse(TypedDict):
	user: Optional[NoneType]

class RecapEligibilityQueryRequest(TypedDict):
	channelLogin: str

class RecapEligibilityQueryResponseUserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]

class RecapEligibilityQueryResponseUserDataSelfData(TypedDict):
	__typename: str
	banStatus: Optional[NoneType]
	subscriptionBenefit: Optional[NoneType]

class RecapEligibilityQueryResponseUserData(TypedDict):
	__typename: str
	id: str
	roles: RecapEligibilityQueryResponseUserDataRolesData
	self: RecapEligibilityQueryResponseUserDataSelfData

class RecapEligibilityQueryResponse(TypedDict):
	user: RecapEligibilityQueryResponseUserData

class BitsConfigContext_GlobalRequest(TypedDict):
	...

class BitsConfigContext_GlobalResponseCheerconfigDataDisplayconfigDataColorsItem(TypedDict):
	__typename: str
	bits: int
	color: str

class BitsConfigContext_GlobalResponseCheerconfigDataDisplayconfigDataTypesItem(TypedDict):
	__typename: str
	animation: str
	extension: str

class BitsConfigContext_GlobalResponseCheerconfigDataDisplayconfigData(TypedDict):
	__typename: str
	backgrounds: List[str]
	colors: List[BitsConfigContext_GlobalResponseCheerconfigDataDisplayconfigDataColorsItem]
	order: List[str]
	scales: List[str]
	types: List[BitsConfigContext_GlobalResponseCheerconfigDataDisplayconfigDataTypesItem]

class BitsConfigContext_GlobalResponseCheerconfigDataGroupsItemNodesItemTiersItem(TypedDict):
	__typename: str
	bits: int
	canShowInBitsCard: Optional[bool]
	id: str

class BitsConfigContext_GlobalResponseCheerconfigDataGroupsItemNodesItem(TypedDict):
	__typename: str
	campaign: Optional[NoneType]
	id: str
	prefix: str
	tiers: List[BitsConfigContext_GlobalResponseCheerconfigDataGroupsItemNodesItemTiersItem]
	type: str

class BitsConfigContext_GlobalResponseCheerconfigDataGroupsItem(TypedDict):
	__typename: str
	nodes: List[BitsConfigContext_GlobalResponseCheerconfigDataGroupsItemNodesItem]
	templateURL: str

class BitsConfigContext_GlobalResponseCheerconfigData(TypedDict):
	__typename: str
	displayConfig: BitsConfigContext_GlobalResponseCheerconfigDataDisplayconfigData
	groups: List[BitsConfigContext_GlobalResponseCheerconfigDataGroupsItem]

class BitsConfigContext_GlobalResponse(TypedDict):
	cheerConfig: BitsConfigContext_GlobalResponseCheerconfigData
	__typename: str

class BitsConfigContext_ChannelRequest(TypedDict):
	login: str

class BitsConfigContext_ChannelResponseChannelDataCheerDataCheergroupsItemNodesItemTiersItem(TypedDict):
	__typename: str
	bits: int
	canShowInBitsCard: Optional[bool]
	id: str

class BitsConfigContext_ChannelResponseChannelDataCheerDataCheergroupsItemNodesItem(TypedDict):
	__typename: str
	campaign: Optional[NoneType]
	id: str
	prefix: str
	tiers: List[BitsConfigContext_ChannelResponseChannelDataCheerDataCheergroupsItemNodesItemTiersItem]
	type: str

class BitsConfigContext_ChannelResponseChannelDataCheerDataCheergroupsItem(TypedDict):
	__typename: str
	nodes: List[BitsConfigContext_ChannelResponseChannelDataCheerDataCheergroupsItemNodesItem]
	templateURL: str

class BitsConfigContext_ChannelResponseChannelDataCheerDataSettingsData(TypedDict):
	__typename: str
	cheerMinimumBits: int
	id: str

class BitsConfigContext_ChannelResponseChannelDataCheerData(TypedDict):
	__typename: str
	cheerGroups: List[BitsConfigContext_ChannelResponseChannelDataCheerDataCheergroupsItem]
	id: str
	isBitsEnabled: Optional[bool]
	settings: BitsConfigContext_ChannelResponseChannelDataCheerDataSettingsData

class BitsConfigContext_ChannelResponseChannelData(TypedDict):
	__typename: str
	cheer: BitsConfigContext_ChannelResponseChannelDataCheerData
	id: str

class BitsConfigContext_ChannelResponse(TypedDict):
	channel: BitsConfigContext_ChannelResponseChannelData

class ChannelShellRequest(TypedDict):
	login: str

class ChannelShellResponseUserorerrorDataChannelDataHomeDataPreferencesData(TypedDict):
	__typename: str
	heroPreset: str

class ChannelShellResponseUserorerrorDataChannelDataHomeData(TypedDict):
	__typename: str
	preferences: ChannelShellResponseUserorerrorDataChannelDataHomeDataPreferencesData

class ChannelShellResponseUserorerrorDataChannelDataSelfData(TypedDict):
	__typename: str
	isAuthorized: Optional[bool]
	restrictionType: Optional[NoneType]

class ChannelShellResponseUserorerrorDataChannelDataTrailerData(TypedDict):
	__typename: str
	video: Optional[NoneType]

class ChannelShellResponseUserorerrorDataChannelData(TypedDict):
	__typename: str
	home: ChannelShellResponseUserorerrorDataChannelDataHomeData
	id: str
	self: ChannelShellResponseUserorerrorDataChannelDataSelfData
	trailer: ChannelShellResponseUserorerrorDataChannelDataTrailerData

class ChannelShellResponseUserorerrorDataStreamData(TypedDict):
	__typename: str
	id: str
	viewersCount: int

class ChannelShellResponseUserorerrorData(TypedDict):
	__typename: str
	bannerImageURL: str
	channel: ChannelShellResponseUserorerrorDataChannelData
	displayName: str
	id: str
	login: str
	primaryColorHex: Optional[NoneType]
	profileImageURL: str
	stream: ChannelShellResponseUserorerrorDataStreamData

class ChannelShellResponse(TypedDict):
	userOrError: ChannelShellResponseUserorerrorData

class UseLiveRequest(TypedDict):
	channelLogin: str

class UseLiveResponseUserDataStreamData(TypedDict):
	__typename: str
	createdAt: str
	id: str

class UseLiveResponseUserData(TypedDict):
	__typename: str
	id: str
	login: str
	stream: UseLiveResponseUserDataStreamData

class UseLiveResponse(TypedDict):
	user: UseLiveResponseUserData

class UseViewCountRequest(TypedDict):
	channelLogin: str

class UseViewCountResponseUserDataStreamData(TypedDict):
	__typename: str
	collaborationViewersCount: Optional[NoneType]
	id: str
	viewersCount: int

class UseViewCountResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: UseViewCountResponseUserDataStreamData

class UseViewCountResponse(TypedDict):
	user: UseViewCountResponseUserData

class ExtensionsOverlayRequest(TypedDict):
	channelLogin: str

class ExtensionsOverlayResponseUserDataSelfData(TypedDict):
	__typename: str
	banStatus: Optional[NoneType]

class ExtensionsOverlayResponseUserDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class ExtensionsOverlayResponseUserDataStreamData(TypedDict):
	__typename: str
	game: ExtensionsOverlayResponseUserDataStreamDataGameData
	id: str

class ExtensionsOverlayResponseUserData(TypedDict):
	__typename: str
	id: str
	self: ExtensionsOverlayResponseUserDataSelfData
	stream: ExtensionsOverlayResponseUserDataStreamData

class ExtensionsOverlayResponse(TypedDict):
	user: ExtensionsOverlayResponseUserData

class StreamTagsTrackingChannelRequest(TypedDict):
	channel: str

class StreamTagsTrackingChannelResponseUserDataStreamDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class StreamTagsTrackingChannelResponseUserDataStreamData(TypedDict):
	__typename: str
	freeformTags: List[StreamTagsTrackingChannelResponseUserDataStreamDataFreeformtagsItem]
	id: str

class StreamTagsTrackingChannelResponseUserData(TypedDict):
	__typename: str
	id: str
	login: str
	stream: StreamTagsTrackingChannelResponseUserDataStreamData

class StreamTagsTrackingChannelResponse(TypedDict):
	user: StreamTagsTrackingChannelResponseUserData

class VideoPlayerStatusOverlayChannelRequest(TypedDict):
	channel: str

class VideoPlayerStatusOverlayChannelResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str
	type: str

class VideoPlayerStatusOverlayChannelResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: VideoPlayerStatusOverlayChannelResponseUserDataStreamData

class VideoPlayerStatusOverlayChannelResponse(TypedDict):
	user: VideoPlayerStatusOverlayChannelResponseUserData

class DropCurrentSessionContextRequest(TypedDict):
	channelLogin: str

class DropCurrentSessionContextResponseCurrentuserDataDropcurrentsessionData(TypedDict):
	__typename: str
	channel: Optional[NoneType]
	currentMinutesWatched: Optional[int]
	dropID: Optional[str]
	game: Optional[NoneType]
	requiredMinutesWatched: Optional[int]

class DropCurrentSessionContextResponseCurrentuserData(TypedDict):
	__typename: str
	dropCurrentSession: DropCurrentSessionContextResponseCurrentuserDataDropcurrentsessionData
	id: str

class DropCurrentSessionContextResponse(TypedDict):
	currentUser: DropCurrentSessionContextResponseCurrentuserData

class GetIDFromLoginRequest(TypedDict):
	login: str

class GetIDFromLoginResponseUserData(TypedDict):
	__typename: str
	id: str

class GetIDFromLoginResponse(TypedDict):
	user: GetIDFromLoginResponseUserData

class SubsidizedSubscriptionsRequest1SponsorshipsparamsDataPreviewoverrideData(TypedDict):
	campaignOverride: Optional[str]
	dspCreativeOverride: Optional[str]
	productInstanceOverride: Optional[str]

class SubsidizedSubscriptionsRequest1SponsorshipsparamsData(TypedDict):
	deviceMake: Optional[str]
	deviceOS: Optional[str]
	deviceType: str
	platform: str
	previewOverride: SubsidizedSubscriptionsRequest1SponsorshipsparamsDataPreviewoverrideData

class SubsidizedSubscriptionsRequest1(TypedDict):
	channelLogin: str
	progressType: str
	shouldFetchUserProgress: Optional[bool]
	sponsorshipsParams: SubsidizedSubscriptionsRequest1SponsorshipsparamsData

class SubsidizedSubscriptionsRequest2SponsorshipsparamsDataPreviewoverrideData(TypedDict):
	campaignOverride: Optional[str]
	dspCreativeOverride: Optional[str]
	productInstanceOverride: Optional[str]

class SubsidizedSubscriptionsRequest2SponsorshipsparamsData(TypedDict):
	deviceMake: Optional[str]
	deviceOS: Optional[str]
	deviceType: str
	platform: str
	previewOverride: SubsidizedSubscriptionsRequest2SponsorshipsparamsDataPreviewoverrideData

class SubsidizedSubscriptionsRequest2(TypedDict):
	channelID: str
	progressType: str
	shouldFetchUserProgress: Optional[bool]
	sponsorshipsParams: SubsidizedSubscriptionsRequest2SponsorshipsparamsData

class SubsidizedSubscriptionsResponseChannelData(TypedDict):
	__typename: str
	id: str
	sponsorships: Optional[NoneType]

class SubsidizedSubscriptionsResponseUserDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class SubsidizedSubscriptionsResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str
	self: SubsidizedSubscriptionsResponseUserDataSelfData

class SubsidizedSubscriptionsResponseCurrentuserData(TypedDict):
	__typename: str
	hasTurbo: Optional[bool]
	id: str

class SubsidizedSubscriptionsResponseRequestinfoData(TypedDict):
	__typename: str
	countryCodeAlpha2: str

class SubsidizedSubscriptionsResponse(TypedDict):
	channel: SubsidizedSubscriptionsResponseChannelData
	user: SubsidizedSubscriptionsResponseUserData
	currentUser: SubsidizedSubscriptionsResponseCurrentuserData
	requestInfo: SubsidizedSubscriptionsResponseRequestinfoData

class ChatScreenReaderAutoAnnounceRequest(TypedDict):
	...

class ChatScreenReaderAutoAnnounceResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	isChatScreenReaderAutoAnnounceEnabled: Optional[bool]

class ChatScreenReaderAutoAnnounceResponse(TypedDict):
	currentUser: ChatScreenReaderAutoAnnounceResponseCurrentuserData

class SharedChatModeratorStrikesRequest(TypedDict):
	channelIDs: List[Any]

class SharedChatModeratorStrikesResponse(TypedDict):
	users: List[Any]

class ChatInputRequest(TypedDict):
	channelLogin: str
	isEmbedded: Optional[bool]

class ChatInputResponseCurrentuserData(TypedDict):
	__typename: str
	bitsBalance: Optional[int]
	id: str

class ChatInputResponseChannelDataCheerDataSettingsData(TypedDict):
	__typename: str
	cheerMinimumBits: int
	emoteMinimumBits: int
	event: Optional[NoneType]
	id: str

class ChatInputResponseChannelDataCheerData(TypedDict):
	__typename: str
	id: str
	settings: ChatInputResponseChannelDataCheerDataSettingsData

class ChatInputResponseChannelDataSelfDataChatmoderatorstrikestatusData(TypedDict):
	__typename: str
	banDetails: Optional[NoneType]
	id: str
	timeoutDetails: Optional[NoneType]
	warningDetails: Optional[NoneType]

class ChatInputResponseChannelDataSelfData(TypedDict):
	__typename: str
	chatModeratorStrikeStatus: ChatInputResponseChannelDataSelfDataChatmoderatorstrikestatusData

class ChatInputResponseChannelData(TypedDict):
	__typename: str
	cheer: ChatInputResponseChannelDataCheerData
	displayName: str
	id: str
	profileImageURL: str
	self: ChatInputResponseChannelDataSelfData

class ChatInputResponse(TypedDict):
	currentUser: ChatInputResponseCurrentuserData
	channel: ChatInputResponseChannelData

class CurrentUserBannedStatusRequest(TypedDict):
	channelLogin: str

class CurrentUserBannedStatusResponseChannelDataSelfData(TypedDict):
	__typename: str
	banStatus: Optional[NoneType]

class CurrentUserBannedStatusResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: CurrentUserBannedStatusResponseChannelDataSelfData

class CurrentUserBannedStatusResponse(TypedDict):
	channel: CurrentUserBannedStatusResponseChannelData

class ChatList_ActiveCharityCampaignRequest(TypedDict):
	channelLogin: str

class ChatList_ActiveCharityCampaignResponseChannelData(TypedDict):
	__typename: str
	activeCharityCampaign: Optional[NoneType]
	id: str

class ChatList_ActiveCharityCampaignResponse(TypedDict):
	channel: ChatList_ActiveCharityCampaignResponseChannelData

class GlobalBadgesRequest(TypedDict):
	...

class GlobalBadgesResponseBadgesItem(TypedDict):
	__typename: str
	clickAction: str
	clickURL: str
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class GlobalBadgesResponse(TypedDict):
	badges: List[GlobalBadgesResponseBadgesItem]

class ChatList_BadgesRequest(TypedDict):
	channelLogin: str

class ChatList_BadgesResponseUserDataSelfData(TypedDict):
	__typename: str
	displayBadges: List[Any]
	selectedBadge: Optional[NoneType]

class ChatList_BadgesResponseUserData(TypedDict):
	__typename: str
	broadcastBadges: List[Any]
	id: str
	primaryColorHex: Optional[NoneType]
	self: ChatList_BadgesResponseUserDataSelfData

class ChatList_BadgesResponse(TypedDict):
	user: ChatList_BadgesResponseUserData

class ChatRestrictionsRequest(TypedDict):
	channelLogin: str

class ChatRestrictionsResponseChannelDataChatsettingsData(TypedDict):
	__typename: str
	requireVerifiedAccount: Optional[bool]

class ChatRestrictionsResponseChannelDataSelfData(TypedDict):
	__typename: str
	banStatus: Optional[NoneType]
	chatRestrictedReasons: List[str]
	follower: Optional[NoneType]
	isFirstTimeChatter: Optional[bool]
	isModerator: Optional[bool]
	isVIP: Optional[bool]
	lastRecentChatMessageAt: Optional[NoneType]
	subscriptionBenefit: Optional[NoneType]

class ChatRestrictionsResponseChannelData(TypedDict):
	__typename: str
	chatSettings: ChatRestrictionsResponseChannelDataChatsettingsData
	id: str
	self: ChatRestrictionsResponseChannelDataSelfData

class ChatRestrictionsResponseCurrentuserData(TypedDict):
	__typename: str
	createdAt: str
	id: str
	isEmailVerified: Optional[bool]
	isPhoneNumberVerified: Optional[bool]

class ChatRestrictionsResponse(TypedDict):
	channel: ChatRestrictionsResponseChannelData
	currentUser: ChatRestrictionsResponseCurrentuserData

class BlockedUsersRequest(TypedDict):
	...

class BlockedUsersResponseCurrentuserData(TypedDict):
	__typename: str
	blockedUsers: List[Any]
	id: str

class BlockedUsersResponse(TypedDict):
	currentUser: BlockedUsersResponseCurrentuserData

class MessageBufferChatHistoryRequest1(TypedDict):
	channelLogin: str

class MessageBufferChatHistoryRequest2(TypedDict):
	channelID: str
	channelLogin: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItemContentDataFragmentsItem(TypedDict):
	__typename: str
	content: Optional[NoneType]
	text: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItemContentData(TypedDict):
	__typename: str
	fragments: List[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItemContentDataFragmentsItem]
	text: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItemSenderData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItem(TypedDict):
	__typename: str
	content: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItemContentData
	deletedAt: Optional[NoneType]
	id: str
	parentMessage: Optional[NoneType]
	sender: MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItemSenderData
	senderBadges: List[Any]
	senderChatColor: Optional[NoneType]
	sentAt: str
	sourceChannel: Optional[NoneType]
	sourceSenderBadges: Optional[NoneType]
	threadParentMessage: Optional[NoneType]

class MessageBufferChatHistoryResponseChannelData(TypedDict):
	__typename: str
	id: str
	recentChatMessages: List[MessageBufferChatHistoryResponseChannelDataRecentchatmessagesItem]

class MessageBufferChatHistoryResponse(TypedDict):
	channel: MessageBufferChatHistoryResponseChannelData

class MessageBuffer_ChannelRequest(TypedDict):
	channelLogin: str

class MessageBuffer_ChannelResponseUserDataChatsettingsData(TypedDict):
	__typename: str
	chatDelayMs: Optional[int]

class MessageBuffer_ChannelResponseUserData(TypedDict):
	__typename: str
	chatSettings: MessageBuffer_ChannelResponseUserDataChatsettingsData
	id: str

class MessageBuffer_ChannelResponse(TypedDict):
	user: MessageBuffer_ChannelResponseUserData

class PollChannelSettingsRequest(TypedDict):
	channelLogin: str

class PollChannelSettingsResponsePollchannelsettingsData(TypedDict):
	__typename: str
	hasPollsAccess: Optional[bool]

class PollChannelSettingsResponse(TypedDict):
	pollChannelSettings: PollChannelSettingsResponsePollchannelsettingsData

class CommunityPointsRewardRedemptionContextRequest(TypedDict):
	channelLogin: str

class CommunityPointsRewardRedemptionContextResponseCommunityDataSelfData(TypedDict):
	__typename: str
	isModerator: Optional[bool]
	subscriptionBenefit: Optional[NoneType]

class CommunityPointsRewardRedemptionContextResponseCommunityData(TypedDict):
	__typename: str
	id: str
	self: CommunityPointsRewardRedemptionContextResponseCommunityDataSelfData

class CommunityPointsRewardRedemptionContextResponse(TypedDict):
	community: CommunityPointsRewardRedemptionContextResponseCommunityData

class ChannelPointsPredictionContextRequest(TypedDict):
	count: int
	channelLogin: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataPredictionsettingsData(TypedDict):
	__typename: str
	isEligibleForPredictions: Optional[bool]

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataCreatedbyData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItemBadgeData(TypedDict):
	__typename: str
	clickAction: Optional[NoneType]
	clickURL: Optional[NoneType]
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItemToppredictorsItemUserData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItemToppredictorsItem(TypedDict):
	__typename: str
	id: str
	points: int
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItemToppredictorsItemUserData

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItem(TypedDict):
	__typename: str
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItemBadgeData
	color: str
	id: str
	title: str
	topPredictors: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItemToppredictorsItem]
	totalPoints: int
	totalUsers: int

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeDataBadgeData(TypedDict):
	__typename: str
	clickAction: Optional[NoneType]
	clickURL: Optional[NoneType]
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeDataToppredictorsItemUserData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeDataToppredictorsItem(TypedDict):
	__typename: str
	id: str
	points: int
	user: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeDataToppredictorsItemUserData

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeData(TypedDict):
	__typename: str
	badge: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeDataBadgeData
	color: str
	id: str
	title: str
	topPredictors: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeDataToppredictorsItem]
	totalPoints: int
	totalUsers: int

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeData(TypedDict):
	__typename: str
	createdAt: str
	createdBy: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataCreatedbyData
	endedAt: str
	id: str
	lockedAt: str
	outcomes: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataOutcomesItem]
	predictionWindowSeconds: int
	status: str
	title: str
	winningOutcome: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeDataWinningoutcomeData

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItem(TypedDict):
	__typename: str
	node: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItemNodeData

class ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsData(TypedDict):
	__typename: str
	edges: List[ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsDataEdgesItem]

class ChannelPointsPredictionContextResponseCommunityDataChannelDataSelfData(TypedDict):
	__typename: str
	recentPredictions: List[Any]

class ChannelPointsPredictionContextResponseCommunityDataChannelData(TypedDict):
	__typename: str
	activePredictionEvents: List[Any]
	id: str
	lockedPredictionEvents: List[Any]
	predictionSettings: ChannelPointsPredictionContextResponseCommunityDataChannelDataPredictionsettingsData
	resolvedPredictionEvents: ChannelPointsPredictionContextResponseCommunityDataChannelDataResolvedpredictioneventsData
	self: ChannelPointsPredictionContextResponseCommunityDataChannelDataSelfData

class ChannelPointsPredictionContextResponseCommunityData(TypedDict):
	__typename: str
	channel: ChannelPointsPredictionContextResponseCommunityDataChannelData
	id: str

class ChannelPointsPredictionContextResponseCurrentuserDataPredictionssettingsData(TypedDict):
	__typename: str
	hasAcceptedTOS: Optional[bool]
	isTemporaryChatBadgeEnabled: Optional[bool]

class ChannelPointsPredictionContextResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	predictionsSettings: ChannelPointsPredictionContextResponseCurrentuserDataPredictionssettingsData

class ChannelPointsPredictionContextResponse(TypedDict):
	community: ChannelPointsPredictionContextResponseCommunityData
	currentUser: ChannelPointsPredictionContextResponseCurrentuserData

class ChannelPointsContextRequest(TypedDict):
	channelLogin: str
	includeGoalTypes: List[str]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemDefaultimageData(TypedDict):
	__typename: str
	url: str
	url2x: str
	url4x: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemGlobalcooldownsettingData(TypedDict):
	__typename: str
	globalCooldownSeconds: Optional[int]
	isEnabled: Optional[bool]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperstreamsettingData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	maxPerStream: Optional[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperuserperstreamsettingData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	maxPerUserPerStream: Optional[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItem(TypedDict):
	__typename: str
	backgroundColor: Optional[NoneType]
	bitsCost: Optional[NoneType]
	cooldownExpiresAt: Optional[NoneType]
	cost: Optional[NoneType]
	defaultBackgroundColor: str
	defaultBitsCost: Optional[int]
	defaultCost: int
	defaultImage: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemDefaultimageData
	globalCooldownSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemGlobalcooldownsettingData
	globallyUpdatedForIndicatorAt: str
	id: str
	image: Optional[NoneType]
	isEnabled: Optional[bool]
	isHiddenForSubs: Optional[bool]
	isInStock: Optional[bool]
	maxPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperstreamsettingData
	maxPerUserPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperuserperstreamsettingData
	minimumCost: int
	pricingType: str
	redemptionsRedeemedCurrentStream: Optional[NoneType]
	type: str
	updatedForIndicatorAt: Optional[NoneType]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemDefaultimageData(TypedDict):
	__typename: str
	url: str
	url2x: str
	url4x: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemGlobalcooldownsettingData(TypedDict):
	__typename: str
	globalCooldownSeconds: Optional[int]
	isEnabled: Optional[bool]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemMaxperstreamsettingData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	maxPerStream: Optional[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemMaxperuserperstreamsettingData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	maxPerUserPerStream: Optional[int]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItem(TypedDict):
	__typename: str
	backgroundColor: str
	cooldownExpiresAt: Optional[NoneType]
	cost: int
	defaultImage: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemDefaultimageData
	globalCooldownSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemGlobalcooldownsettingData
	id: str
	image: Optional[NoneType]
	isEnabled: Optional[bool]
	isInStock: Optional[bool]
	isPaused: Optional[bool]
	isSubOnly: Optional[bool]
	isUserInputRequired: Optional[bool]
	maxPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemMaxperstreamsettingData
	maxPerUserPerStreamSetting: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItemMaxperuserperstreamsettingData
	prompt: str
	redemptionsRedeemedCurrentStream: Optional[NoneType]
	shouldRedemptionsSkipRequestQueue: Optional[bool]
	title: str
	updatedForIndicatorAt: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataMultipliersItem(TypedDict):
	__typename: str
	factor: float
	reasonCode: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataWatchstreakpointsItem(TypedDict):
	__typename: str
	points: int

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningData(TypedDict):
	__typename: str
	averagePointsPerHour: int
	cheerPoints: int
	claimPoints: int
	followPoints: int
	id: str
	multipliers: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataMultipliersItem]
	passiveWatchPoints: int
	raidPoints: int
	subscriptionGiftPoints: int
	watchStreakPoints: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningDataWatchstreakpointsItem]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemEmoteData(TypedDict):
	__typename: str
	id: str
	token: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemModificationsItemEmoteData(TypedDict):
	__typename: str
	id: str
	token: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemModificationsItemModifierData(TypedDict):
	__typename: str
	id: str

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemModificationsItem(TypedDict):
	__typename: str
	emote: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemModificationsItemEmoteData
	globallyUpdatedForIndicatorAt: str
	id: str
	modifier: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemModificationsItemModifierData

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItem(TypedDict):
	__typename: str
	emote: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemEmoteData
	id: str
	isUnlockable: Optional[bool]
	modifications: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItemModificationsItem]

class ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsData(TypedDict):
	__typename: str
	automaticRewards: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataAutomaticrewardsItem]
	customRewards: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataCustomrewardsItem]
	earning: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEarningData
	emoteVariants: List[ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsDataEmotevariantsItem]
	goals: List[Any]
	image: Optional[NoneType]
	isEnabled: Optional[bool]
	name: Optional[NoneType]
	raidPointAmount: int

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataLastviewedcontentItem(TypedDict):
	__typename: str
	contentType: str
	lastViewedAt: str

class ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsData(TypedDict):
	__typename: str
	activeMultipliers: List[Any]
	availableClaim: Optional[NoneType]
	balance: Optional[int]
	canRedeemRewardsForFree: Optional[bool]
	lastViewedContent: List[ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsDataLastviewedcontentItem]
	userRedemptions: List[Any]

class ChannelPointsContextResponseCommunityDataChannelDataSelfData(TypedDict):
	__typename: str
	communityPoints: ChannelPointsContextResponseCommunityDataChannelDataSelfDataCommunitypointsData

class ChannelPointsContextResponseCommunityDataChannelData(TypedDict):
	__typename: str
	communityPointsSettings: ChannelPointsContextResponseCommunityDataChannelDataCommunitypointssettingsData
	id: str
	self: ChannelPointsContextResponseCommunityDataChannelDataSelfData

class ChannelPointsContextResponseCommunityDataSelfData(TypedDict):
	__typename: str
	isModerator: Optional[bool]

class ChannelPointsContextResponseCommunityData(TypedDict):
	__typename: str
	channel: ChannelPointsContextResponseCommunityDataChannelData
	displayName: str
	id: str
	profileImageURL: str
	self: ChannelPointsContextResponseCommunityDataSelfData

class ChannelPointsContextResponseCurrentuserDataCommunitypointsDataLastviewedcontentItem(TypedDict):
	__typename: str
	contentID: str
	contentType: str
	lastViewedAt: str

class ChannelPointsContextResponseCurrentuserDataCommunitypointsData(TypedDict):
	__typename: str
	lastViewedContent: List[ChannelPointsContextResponseCurrentuserDataCommunitypointsDataLastviewedcontentItem]

class ChannelPointsContextResponseCurrentuserData(TypedDict):
	__typename: str
	communityPoints: ChannelPointsContextResponseCurrentuserDataCommunitypointsData
	id: str

class ChannelPointsContextResponse(TypedDict):
	community: ChannelPointsContextResponseCommunityData
	currentUser: ChannelPointsContextResponseCurrentuserData

class ChannelPointsGlobalContextRequest(TypedDict):
	...

class ChannelPointsGlobalContextResponseEmotemodifiersItemIcondarkData(TypedDict):
	__typename: str
	url: str
	url2x: str
	url4x: str

class ChannelPointsGlobalContextResponseEmotemodifiersItemIconlightData(TypedDict):
	__typename: str
	url: str
	url2x: str
	url4x: str

class ChannelPointsGlobalContextResponseEmotemodifiersItem(TypedDict):
	__typename: str
	iconDark: ChannelPointsGlobalContextResponseEmotemodifiersItemIcondarkData
	iconLight: ChannelPointsGlobalContextResponseEmotemodifiersItemIconlightData
	id: str
	title: str

class ChannelPointsGlobalContextResponse(TypedDict):
	emoteModifiers: List[ChannelPointsGlobalContextResponseEmotemodifiersItem]

class SyncedSettingsChatPauseSettingRequest(TypedDict):
	...

class SyncedSettingsChatPauseSettingResponseCurrentuserDataChatuisettingsData(TypedDict):
	__typename: str
	chatPauseSetting: Optional[NoneType]

class SyncedSettingsChatPauseSettingResponseCurrentuserData(TypedDict):
	__typename: str
	chatUISettings: SyncedSettingsChatPauseSettingResponseCurrentuserDataChatuisettingsData
	id: str

class SyncedSettingsChatPauseSettingResponse(TypedDict):
	currentUser: SyncedSettingsChatPauseSettingResponseCurrentuserData

class SyncedSettingsDeletedMessageDisplaySettingRequest(TypedDict):
	...

class SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserDataChatuisettingsData(TypedDict):
	__typename: str
	deletedMessageDisplaySetting: Optional[NoneType]

class SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserData(TypedDict):
	__typename: str
	chatUISettings: SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserDataChatuisettingsData
	id: str

class SyncedSettingsDeletedMessageDisplaySettingResponse(TypedDict):
	currentUser: SyncedSettingsDeletedMessageDisplaySettingResponseCurrentuserData

class SyncedSettingsEmoteAnimationsRequest(TypedDict):
	...

class SyncedSettingsEmoteAnimationsResponseCurrentuserDataChatuisettingsData(TypedDict):
	__typename: str
	isEmoteAnimationsEnabled: Optional[bool]

class SyncedSettingsEmoteAnimationsResponseCurrentuserData(TypedDict):
	__typename: str
	chatUISettings: SyncedSettingsEmoteAnimationsResponseCurrentuserDataChatuisettingsData
	id: str

class SyncedSettingsEmoteAnimationsResponse(TypedDict):
	currentUser: SyncedSettingsEmoteAnimationsResponseCurrentuserData

class SyncedSettingsReadableChatColorsRequest(TypedDict):
	...

class SyncedSettingsReadableChatColorsResponseCurrentuserDataChatuisettingsData(TypedDict):
	__typename: str
	isReadableChatColorsEnabled: Optional[bool]

class SyncedSettingsReadableChatColorsResponseCurrentuserData(TypedDict):
	__typename: str
	chatUISettings: SyncedSettingsReadableChatColorsResponseCurrentuserDataChatuisettingsData
	id: str

class SyncedSettingsReadableChatColorsResponse(TypedDict):
	currentUser: SyncedSettingsReadableChatColorsResponseCurrentuserData

class ChatRoomStateRequest(TypedDict):
	login: str

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialemailverificationconfigData(TypedDict):
	__typename: str
	minimumAccountAgeInMinutes: int
	minimumFollowerAgeInMinutes: int
	shouldRestrictBasedOnAccountAge: Optional[bool]
	shouldRestrictBasedOnFollowerAge: Optional[bool]
	shouldRestrictFirstTimeChatters: Optional[bool]

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialphoneverificationconfigData(TypedDict):
	__typename: str
	minimumAccountAgeInMinutes: int
	minimumFollowerAgeInMinutes: int
	shouldRestrictBasedOnAccountAge: Optional[bool]
	shouldRestrictBasedOnFollowerAge: Optional[bool]
	shouldRestrictFirstTimeChatters: Optional[bool]

class ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsData(TypedDict):
	__typename: str
	emailVerificationMode: str
	isModeratorExempt: Optional[bool]
	isSubscriberExempt: Optional[bool]
	isVIPExempt: Optional[bool]
	partialEmailVerificationConfig: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialemailverificationconfigData
	partialPhoneVerificationConfig: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsDataPartialphoneverificationconfigData
	phoneVerificationMode: str

class ChatRoomStateResponseChannelDataChatsettingsData(TypedDict):
	__typename: str
	accountVerificationOptions: ChatRoomStateResponseChannelDataChatsettingsDataAccountverificationoptionsData
	followersOnlyDurationMinutes: Optional[NoneType]
	isEmoteOnlyModeEnabled: Optional[bool]
	slowModeDurationSeconds: Optional[NoneType]

class ChatRoomStateResponseChannelDataSubscriptionproductsItem(TypedDict):
	__typename: str
	hasSubOnlyChat: Optional[bool]
	id: str

class ChatRoomStateResponseChannelData(TypedDict):
	__typename: str
	chatSettings: ChatRoomStateResponseChannelDataChatsettingsData
	id: str
	subscriptionProducts: List[ChatRoomStateResponseChannelDataSubscriptionproductsItem]

class ChatRoomStateResponse(TypedDict):
	channel: ChatRoomStateResponseChannelData

class Chat_UserDataRequest(TypedDict):
	...

class Chat_UserDataResponseUserDataRolesData(TypedDict):
	__typename: str
	isGlobalMod: Optional[NoneType]
	isSiteAdmin: Optional[NoneType]
	isStaff: Optional[NoneType]

class Chat_UserDataResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	roles: Chat_UserDataResponseUserDataRolesData

class Chat_UserDataResponse(TypedDict):
	user: Chat_UserDataResponseUserData

class Chat_ChannelDataRequest(TypedDict):
	channelLogin: str

class Chat_ChannelDataResponseChannelDataChatsettingsData(TypedDict):
	__typename: str
	rules: List[Any]

class Chat_ChannelDataResponseChannelDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]
	isModerator: Optional[bool]
	isVIP: Optional[bool]

class Chat_ChannelDataResponseChannelData(TypedDict):
	__typename: str
	chatSettings: Chat_ChannelDataResponseChannelDataChatsettingsData
	displayName: str
	id: str
	login: str
	self: Chat_ChannelDataResponseChannelDataSelfData

class Chat_ChannelDataResponse(TypedDict):
	channel: Chat_ChannelDataResponseChannelData

class CommonHooks_BlockedUsersRequest(TypedDict):
	...

class CommonHooks_BlockedUsersResponseCurrentuserData(TypedDict):
	__typename: str
	blockedUsers: List[Any]
	id: str

class CommonHooks_BlockedUsersResponse(TypedDict):
	currentUser: CommonHooks_BlockedUsersResponseCurrentuserData

class PinnedCheersSettingsRequest(TypedDict):
	login: str

class PinnedCheersSettingsResponseUserDataCheerDataSettingsData(TypedDict):
	__typename: str
	id: str
	isPinnedCheersEnabled: Optional[bool]

class PinnedCheersSettingsResponseUserDataCheerData(TypedDict):
	__typename: str
	id: str
	settings: PinnedCheersSettingsResponseUserDataCheerDataSettingsData

class PinnedCheersSettingsResponseUserData(TypedDict):
	__typename: str
	cheer: PinnedCheersSettingsResponseUserDataCheerData
	id: str

class PinnedCheersSettingsResponse(TypedDict):
	user: PinnedCheersSettingsResponseUserData

class CurrentUserStrikeStatusRequest(TypedDict):
	channelLogin: str

class CurrentUserStrikeStatusResponseChannelDataSelfDataChatmoderatorstrikestatusData(TypedDict):
	__typename: str
	banDetails: Optional[NoneType]
	id: str
	timeoutDetails: Optional[NoneType]
	warningDetails: Optional[NoneType]

class CurrentUserStrikeStatusResponseChannelDataSelfData(TypedDict):
	__typename: str
	chatModeratorStrikeStatus: CurrentUserStrikeStatusResponseChannelDataSelfDataChatmoderatorstrikestatusData

class CurrentUserStrikeStatusResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: CurrentUserStrikeStatusResponseChannelDataSelfData

class CurrentUserStrikeStatusResponse(TypedDict):
	channel: CurrentUserStrikeStatusResponseChannelData

class StreamChatRequest(TypedDict):
	login: str

class StreamChatResponseChannelDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]

class StreamChatResponseChannelDataSelfData(TypedDict):
	__typename: str
	banStatus: Optional[NoneType]
	isChannelMember: Optional[bool]
	isModerator: Optional[bool]
	subscriptionBenefit: Optional[NoneType]

class StreamChatResponseChannelDataStreamData(TypedDict):
	__typename: str
	id: str

class StreamChatResponseChannelData(TypedDict):
	__typename: str
	displayName: str
	id: str
	roles: StreamChatResponseChannelDataRolesData
	self: StreamChatResponseChannelDataSelfData
	stream: StreamChatResponseChannelDataStreamData

class StreamChatResponse(TypedDict):
	channel: StreamChatResponseChannelData

class OneTapFeedRequest(TypedDict):
	channelID: str

class OneTapFeedResponseOnetapfeedData(TypedDict):
	__typename: str
	items: List[Any]

class OneTapFeedResponse(TypedDict):
	oneTapFeed: OneTapFeedResponseOnetapfeedData

class SharedChatSessionRequest(TypedDict):
	channelID: str

class SharedChatSessionResponse(TypedDict):
	sharedChatSession: Optional[NoneType]

class ChannelCollaborationEligibilityQueryRequestOptionsData(TypedDict):
	channelIDs: List[str]

class ChannelCollaborationEligibilityQueryRequest(TypedDict):
	options: ChannelCollaborationEligibilityQueryRequestOptionsData

class ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesDataChannelcollabsItem(TypedDict):
	__typename: str
	canJoinStatus: str
	id: str

class ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesData(TypedDict):
	__typename: str
	channelCollabs: List[ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesDataChannelcollabsItem]

class ChannelCollaborationEligibilityQueryResponse(TypedDict):
	guestStarCollaborationStatuses: ChannelCollaborationEligibilityQueryResponseGueststarcollaborationstatusesData

class GetHypeTrainExecutionV2Request(TypedDict):
	userLogin: str

class GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainData(TypedDict):
	__typename: str
	approaching: Optional[NoneType]
	execution: Optional[NoneType]

class GetHypeTrainExecutionV2ResponseUserDataChannelData(TypedDict):
	__typename: str
	hypeTrain: GetHypeTrainExecutionV2ResponseUserDataChannelDataHypetrainData
	id: str

class GetHypeTrainExecutionV2ResponseUserData(TypedDict):
	__typename: str
	channel: GetHypeTrainExecutionV2ResponseUserDataChannelData
	displayName: str
	id: str

class GetHypeTrainExecutionV2Response(TypedDict):
	user: GetHypeTrainExecutionV2ResponseUserData

class StoryPreviewChannelRequest(TypedDict):
	channelID: str
	capabilities: List[str]

class StoryPreviewChannelResponse(TypedDict):
	storyPreviewForChannel: Optional[NoneType]

class StreamEventCelebrationsChannelPageBadgeRequest(TypedDict):
	channelLogin: str

class StreamEventCelebrationsChannelPageBadgeResponseChannelData(TypedDict):
	__typename: str
	activeStreamEventCelebration: Optional[NoneType]
	id: str

class StreamEventCelebrationsChannelPageBadgeResponse(TypedDict):
	channel: StreamEventCelebrationsChannelPageBadgeResponseChannelData

class GuestStarActiveJoinRequestRequest(TypedDict):
	...

class GuestStarActiveJoinRequestResponse(TypedDict):
	guestStarActiveJoinRequest: Optional[NoneType]

class GuestStarChannelPageCollaborationQueryRequestOptionsData(TypedDict):
	channelIDs: List[str]

class GuestStarChannelPageCollaborationQueryRequest(TypedDict):
	options: GuestStarChannelPageCollaborationQueryRequestOptionsData
	openCallingIsEnabled: Optional[bool]

class GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsItem(TypedDict):
	__typename: str
	canJoinStatus: str
	id: str
	isFavorite: Optional[bool]
	session: Optional[NoneType]

class GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesData(TypedDict):
	__typename: str
	channelCollabs: List[GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesDataChannelcollabsItem]
	shouldRefetch: Optional[bool]
	shouldSubscribeToUpdates: Optional[bool]

class GuestStarChannelPageCollaborationQueryResponse(TypedDict):
	guestStarCollaborationStatuses: GuestStarChannelPageCollaborationQueryResponseGueststarcollaborationstatusesData

class ChatRoomBanStatusRequest(TypedDict):
	targetUserID: str
	channelID: str

class ChatRoomBanStatusResponseTargetuserData(TypedDict):
	__typename: str
	id: str
	login: str

class ChatRoomBanStatusResponse(TypedDict):
	chatRoomBanStatus: Optional[NoneType]
	targetUser: ChatRoomBanStatusResponseTargetuserData

class GuestListQueryRequest(TypedDict):
	channelID: str

class GuestListQueryResponseChannelData(TypedDict):
	__typename: str
	guestStarSessionCall: Optional[NoneType]
	id: str

class GuestListQueryResponse(TypedDict):
	channel: GuestListQueryResponseChannelData

class ChannelPage_SubscribeButton_UserRequest1(TypedDict):
	login: str
	includeExpiredDunning: Optional[bool]

class ChannelPage_SubscribeButton_UserRequest2(TypedDict):
	login: str

class ChannelPage_SubscribeButton_UserResponseUserDataSelfDataCumulativetenureData(TypedDict):
	__typename: str
	daysRemaining: Optional[int]
	months: Optional[int]

class ChannelPage_SubscribeButton_UserResponseUserDataSelfData(TypedDict):
	__typename: str
	canPrimeSubscribe: Optional[bool]
	cumulativeTenure: ChannelPage_SubscribeButton_UserResponseUserDataSelfDataCumulativetenureData
	follower: Optional[NoneType]
	subscriptionBenefit: Optional[NoneType]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData
	previewPrice: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData(TypedDict):
	__typename: str
	internal: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData(TypedDict):
	__typename: str
	chargeModel: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData(TypedDict):
	__typename: str
	eligibility: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData
	giftType: str
	id: str
	listing: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataQuantityData
	tagBindings: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataTagbindingsItem]
	tplr: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem(TypedDict):
	__typename: str
	offer: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingData(TypedDict):
	__typename: str
	community: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanData
	previewPrice: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelData(TypedDict):
	__typename: str
	internal: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingData(TypedDict):
	__typename: str
	chargeModel: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelData

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItem(TypedDict):
	__typename: str
	eligibility: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemEligibilityData
	giftType: Optional[NoneType]
	id: str
	listing: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemQuantityData
	tagBindings: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItemTagbindingsItem]
	tplr: str

class ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	emoteSetID: str
	gifting: ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemGiftingData
	hasAdFree: Optional[bool]
	id: str
	name: str
	offers: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItemOffersItem]
	tier: str

class ChannelPage_SubscribeButton_UserResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	primaryColorHex: Optional[NoneType]
	self: ChannelPage_SubscribeButton_UserResponseUserDataSelfData
	subscriptionProducts: List[ChannelPage_SubscribeButton_UserResponseUserDataSubscriptionproductsItem]

class ChannelPage_SubscribeButton_UserResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class ChannelPage_SubscribeButton_UserResponse(TypedDict):
	user: ChannelPage_SubscribeButton_UserResponseUserData
	requestInfo: ChannelPage_SubscribeButton_UserResponseRequestinfoData

class ChannelActiveCharityCampaignRequest(TypedDict):
	channelID: str

class ChannelActiveCharityCampaignResponseChannelData(TypedDict):
	__typename: str
	activeCharityCampaign: Optional[NoneType]
	id: str

class ChannelActiveCharityCampaignResponse(TypedDict):
	channel: ChannelActiveCharityCampaignResponseChannelData

class RealtimeStreamTagListRequest(TypedDict):
	channelLogin: str

class RealtimeStreamTagListResponseUserDataStreamDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class RealtimeStreamTagListResponseUserDataStreamData(TypedDict):
	__typename: str
	freeformTags: List[RealtimeStreamTagListResponseUserDataStreamDataFreeformtagsItem]
	id: str

class RealtimeStreamTagListResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: RealtimeStreamTagListResponseUserDataStreamData

class RealtimeStreamTagListResponse(TypedDict):
	user: RealtimeStreamTagListResponseUserData

class StreamMetadataRequest(TypedDict):
	channelLogin: str
	includeIsDJ: Optional[bool]

class StreamMetadataResponseUserDataChannelData(TypedDict):
	__typename: str
	id: str

class StreamMetadataResponseUserDataLastbroadcastData(TypedDict):
	__typename: str
	id: str
	title: str

class StreamMetadataResponseUserDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class StreamMetadataResponseUserDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str
	slug: str

class StreamMetadataResponseUserDataStreamData(TypedDict):
	__typename: str
	createdAt: str
	game: StreamMetadataResponseUserDataStreamDataGameData
	id: str
	type: str

class StreamMetadataResponseUserData(TypedDict):
	__typename: str
	channel: StreamMetadataResponseUserDataChannelData
	id: str
	lastBroadcast: StreamMetadataResponseUserDataLastbroadcastData
	primaryColorHex: Optional[NoneType]
	primaryTeam: Optional[NoneType]
	profileImageURL: str
	roles: StreamMetadataResponseUserDataRolesData
	stream: StreamMetadataResponseUserDataStreamData

class StreamMetadataResponse(TypedDict):
	user: StreamMetadataResponseUserData

class UseLiveBroadcastRequest(TypedDict):
	channelLogin: str

class UseLiveBroadcastResponseUserDataLastbroadcastDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	slug: str

class UseLiveBroadcastResponseUserDataLastbroadcastData(TypedDict):
	__typename: str
	game: UseLiveBroadcastResponseUserDataLastbroadcastDataGameData
	id: str
	title: str

class UseLiveBroadcastResponseUserData(TypedDict):
	__typename: str
	id: str
	lastBroadcast: UseLiveBroadcastResponseUserDataLastbroadcastData

class UseLiveBroadcastResponse(TypedDict):
	user: UseLiveBroadcastResponseUserData

class WatchTrackQueryRequest(TypedDict):
	channelLogin: str
	videoID: Optional[NoneType]
	hasVideoID: Optional[bool]

class WatchTrackQueryResponse1UserDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	language: str

class WatchTrackQueryResponse1UserDataLastbroadcastDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class WatchTrackQueryResponse1UserDataLastbroadcastData(TypedDict):
	__typename: str
	game: WatchTrackQueryResponse1UserDataLastbroadcastDataGameData
	id: str

class WatchTrackQueryResponse1UserDataSelfData(TypedDict):
	__typename: str
	follower: Optional[NoneType]

class WatchTrackQueryResponse1UserDataStreamData(TypedDict):
	__typename: str
	id: str

class WatchTrackQueryResponse1UserData(TypedDict):
	__typename: str
	broadcastSettings: WatchTrackQueryResponse1UserDataBroadcastsettingsData
	id: str
	lastBroadcast: WatchTrackQueryResponse1UserDataLastbroadcastData
	self: WatchTrackQueryResponse1UserDataSelfData
	stream: WatchTrackQueryResponse1UserDataStreamData

class WatchTrackQueryResponse1(TypedDict):
	user: WatchTrackQueryResponse1UserData

class WatchTrackQueryResponse2UserDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	language: str

class WatchTrackQueryResponse2UserDataLastbroadcastDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class WatchTrackQueryResponse2UserDataLastbroadcastData(TypedDict):
	__typename: str
	game: WatchTrackQueryResponse2UserDataLastbroadcastDataGameData
	id: str

class WatchTrackQueryResponse2UserDataSelfDataFollowerDataNodeData(TypedDict):
	__typename: str
	id: str

class WatchTrackQueryResponse2UserDataSelfDataFollowerData(TypedDict):
	__typename: str
	node: WatchTrackQueryResponse2UserDataSelfDataFollowerDataNodeData

class WatchTrackQueryResponse2UserDataSelfData(TypedDict):
	__typename: str
	follower: WatchTrackQueryResponse2UserDataSelfDataFollowerData

class WatchTrackQueryResponse2UserDataStreamData(TypedDict):
	__typename: str
	id: str

class WatchTrackQueryResponse2UserData(TypedDict):
	__typename: str
	broadcastSettings: WatchTrackQueryResponse2UserDataBroadcastsettingsData
	id: str
	lastBroadcast: WatchTrackQueryResponse2UserDataLastbroadcastData
	self: WatchTrackQueryResponse2UserDataSelfData
	stream: WatchTrackQueryResponse2UserDataStreamData

class WatchTrackQueryResponse2VideoDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class WatchTrackQueryResponse2VideoData(TypedDict):
	__typename: str
	broadcastType: str
	game: WatchTrackQueryResponse2VideoDataGameData
	id: str
	language: str

class WatchTrackQueryResponse2(TypedDict):
	user: WatchTrackQueryResponse2UserData
	video: WatchTrackQueryResponse2VideoData

class TurboAndSubUpsellRequest(TypedDict):
	channelLogin: str

class TurboAndSubUpsellResponseUserDataSubscriptionproductsItemEmotesItem(TypedDict):
	__typename: str
	id: str
	token: str

class TurboAndSubUpsellResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	emotes: List[TurboAndSubUpsellResponseUserDataSubscriptionproductsItemEmotesItem]
	id: str
	name: str

class TurboAndSubUpsellResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str
	subscriptionProducts: List[TurboAndSubUpsellResponseUserDataSubscriptionproductsItem]

class TurboAndSubUpsellResponse(TypedDict):
	user: TurboAndSubUpsellResponseUserData

class UserModStatusRequest(TypedDict):
	channelID: str
	userID: str

class UserModStatusResponseUserData(TypedDict):
	__typename: str
	id: str
	isModerator: Optional[bool]
	login: str

class UserModStatusResponse(TypedDict):
	user: UserModStatusResponseUserData

class CommunityOnboardingAllowlistRequest(TypedDict):
	channelID: str

class CommunityOnboardingAllowlistResponseCommunityonboardingData(TypedDict):
	__typename: str
	channelAllowLists: List[Any]

class CommunityOnboardingAllowlistResponse(TypedDict):
	communityOnboarding: CommunityOnboardingAllowlistResponseCommunityonboardingData

class GetPinnedChatRequest(TypedDict):
	channelID: str
	count: int

class GetPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class GetPinnedChatResponseChannelDataPinnedchatmessagesData(TypedDict):
	__typename: str
	edges: List[Any]
	pageInfo: GetPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData

class GetPinnedChatResponseChannelData(TypedDict):
	__typename: str
	id: str
	pinnedChatMessages: GetPinnedChatResponseChannelDataPinnedchatmessagesData

class GetPinnedChatResponse(TypedDict):
	channel: GetPinnedChatResponseChannelData

class PinnedChatSettingsRequest(TypedDict):
	channelID: str

class PinnedChatSettingsResponseChannelDataPinnedchatsettingsData(TypedDict):
	__typename: str
	isModAccessEnabled: Optional[bool]

class PinnedChatSettingsResponseChannelData(TypedDict):
	__typename: str
	id: str
	pinnedChatSettings: PinnedChatSettingsResponseChannelDataPinnedchatsettingsData

class PinnedChatSettingsResponse(TypedDict):
	channel: PinnedChatSettingsResponseChannelData

class AvailableEmotesForChannelPaginatedRequest(TypedDict):
	channelID: str
	withOwner: Optional[bool]
	pageLimit: int

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesItemNodeDataEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	modifiers: Optional[NoneType]
	setID: str
	token: str
	type: str

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesItemNodeData(TypedDict):
	__typename: str
	emotes: List[AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesItemNodeDataEmotesItem]
	id: str
	owner: Optional[NoneType]

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[str]
	node: AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesItemNodeData

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedData(TypedDict):
	__typename: str
	edges: List[AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataEdgesItem]
	pageInfo: AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedDataPageinfoData

class AvailableEmotesForChannelPaginatedResponseChannelDataSelfData(TypedDict):
	__typename: str
	availableEmoteSetsPaginated: AvailableEmotesForChannelPaginatedResponseChannelDataSelfDataAvailableemotesetspaginatedData

class AvailableEmotesForChannelPaginatedResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: AvailableEmotesForChannelPaginatedResponseChannelDataSelfData

class AvailableEmotesForChannelPaginatedResponse(TypedDict):
	channel: AvailableEmotesForChannelPaginatedResponseChannelData

class EmotesForChannelFollowStatusRequest(TypedDict):
	channelID: str

class EmotesForChannelFollowStatusResponseUserDataSelfData(TypedDict):
	__typename: str
	follower: Optional[NoneType]

class EmotesForChannelFollowStatusResponseUserData(TypedDict):
	__typename: str
	id: str
	self: EmotesForChannelFollowStatusResponseUserDataSelfData

class EmotesForChannelFollowStatusResponse(TypedDict):
	user: EmotesForChannelFollowStatusResponseUserData

class CurrentUserModeratorStatusRequest1(TypedDict):
	channelID: str

class CurrentUserModeratorStatusRequest2(TypedDict):
	channelLogin: str

class CurrentUserModeratorStatusResponseUserDataSelfData(TypedDict):
	__typename: str
	isModerator: Optional[bool]

class CurrentUserModeratorStatusResponseUserData(TypedDict):
	__typename: str
	id: str
	self: CurrentUserModeratorStatusResponseUserDataSelfData

class CurrentUserModeratorStatusResponseCurrentuserData(TypedDict):
	__typename: str
	id: str

class CurrentUserModeratorStatusResponse(TypedDict):
	user: CurrentUserModeratorStatusResponseUserData
	currentUser: CurrentUserModeratorStatusResponseCurrentuserData

class WithIsStreamLiveQueryRequest(TypedDict):
	id: str

class WithIsStreamLiveQueryResponseUserDataStreamData(TypedDict):
	__typename: str
	createdAt: str
	id: str

class WithIsStreamLiveQueryResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: WithIsStreamLiveQueryResponseUserDataStreamData

class WithIsStreamLiveQueryResponse(TypedDict):
	user: WithIsStreamLiveQueryResponseUserData

class ChannelPollContext_GetViewablePollRequest(TypedDict):
	login: str

class ChannelPollContext_GetViewablePollResponseChannelDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]
	isModerator: Optional[bool]

class ChannelPollContext_GetViewablePollResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: ChannelPollContext_GetViewablePollResponseChannelDataSelfData
	viewablePoll: Optional[NoneType]

class ChannelPollContext_GetViewablePollResponseCurrentuserData(TypedDict):
	__typename: str
	id: str

class ChannelPollContext_GetViewablePollResponse(TypedDict):
	channel: ChannelPollContext_GetViewablePollResponseChannelData
	currentUser: ChannelPollContext_GetViewablePollResponseCurrentuserData

class LastUnbanRequestRequest(TypedDict):
	channelID: str
	includeCanRequestUnban: Optional[bool]

class LastUnbanRequestResponseChannelDataSelfData(TypedDict):
	__typename: str
	lastUnbanRequest: Optional[NoneType]

class LastUnbanRequestResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: LastUnbanRequestResponseChannelDataSelfData

class LastUnbanRequestResponse(TypedDict):
	channel: LastUnbanRequestResponseChannelData

class EmotePicker_EmotePicker_UserSubscriptionProductsRequest(TypedDict):
	channelOwnerID: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseCurrentuserData(TypedDict):
	__typename: str
	bitsBalance: Optional[int]
	id: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseChannelDataLocalemotesetsItemEmotesItem(TypedDict):
	__typename: str
	id: str
	setID: str
	token: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseChannelDataLocalemotesetsItem(TypedDict):
	__typename: str
	emotes: List[EmotePicker_EmotePicker_UserSubscriptionProductsResponseChannelDataLocalemotesetsItemEmotesItem]
	id: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseChannelData(TypedDict):
	__typename: str
	id: str
	localEmoteSets: List[EmotePicker_EmotePicker_UserSubscriptionProductsResponseChannelDataLocalemotesetsItem]

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataCheerData(TypedDict):
	__typename: str
	badgeTierEmotes: List[Any]
	id: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSelfDataCumulativetenureData(TypedDict):
	__typename: str
	months: Optional[int]

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSelfData(TypedDict):
	__typename: str
	cumulativeTenure: EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSelfDataCumulativetenureData
	follower: Optional[NoneType]
	subscriptionBenefit: Optional[NoneType]

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSubscriptionproductsItemEmotegroupsItem(TypedDict):
	__typename: str
	id: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSubscriptionproductsItemEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	setID: str
	token: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	emoteGroups: List[EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSubscriptionproductsItemEmotegroupsItem]
	emoteSetID: str
	emotes: List[EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSubscriptionproductsItemEmotesItem]
	id: str
	name: str
	price: str
	tier: str
	url: str

class EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserData(TypedDict):
	__typename: str
	cheer: EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataCheerData
	displayName: str
	id: str
	login: str
	profileImageURL: str
	self: EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSelfData
	subscriptionProducts: List[EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserDataSubscriptionproductsItem]

class EmotePicker_EmotePicker_UserSubscriptionProductsResponse(TypedDict):
	currentUser: EmotePicker_EmotePicker_UserSubscriptionProductsResponseCurrentuserData
	channel: EmotePicker_EmotePicker_UserSubscriptionProductsResponseChannelData
	user: EmotePicker_EmotePicker_UserSubscriptionProductsResponseUserData

class BitsCard_BitsRequest(TypedDict):
	...

class BitsCard_BitsResponseCurrentuserDataBitsusersettingsDataFirstcheertutorialData(TypedDict):
	__typename: str
	hasAbandoned: Optional[bool]
	hasSkipped: Optional[bool]

class BitsCard_BitsResponseCurrentuserDataBitsusersettingsData(TypedDict):
	__typename: str
	firstCheerTutorial: BitsCard_BitsResponseCurrentuserDataBitsusersettingsDataFirstcheertutorialData

class BitsCard_BitsResponseCurrentuserData(TypedDict):
	__typename: str
	bitsBalance: Optional[int]
	bitsUserSettings: BitsCard_BitsResponseCurrentuserDataBitsusersettingsData
	bitsUserState: str
	id: str
	login: str

class BitsCard_BitsResponse(TypedDict):
	currentUser: BitsCard_BitsResponseCurrentuserData

class ChatModeratorStrikeStatusRequest(TypedDict):
	channelID: str
	targetUserID: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataModerateduserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataRoomownerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusData(TypedDict):
	__typename: str
	banDetails: Optional[NoneType]
	id: str
	moderatedUser: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataModerateduserData
	roomOwner: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusDataRoomownerData
	timeoutDetails: Optional[NoneType]
	warningDetails: Optional[NoneType]

class ChatModeratorStrikeStatusResponse(TypedDict):
	chatModeratorStrikeStatus: ChatModeratorStrikeStatusResponseChatmoderatorstrikestatusData

class Chat_OrbisPresetTextRequest(TypedDict):
	login: str

class Chat_OrbisPresetTextResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str
	platform: Optional[NoneType]

class Chat_OrbisPresetTextResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: Chat_OrbisPresetTextResponseUserDataStreamData

class Chat_OrbisPresetTextResponse(TypedDict):
	user: Chat_OrbisPresetTextResponseUserData

class CommunitySupportSettingsRequest(TypedDict):
	channelID: str

class CommunitySupportSettingsResponseUserDataSettingsDataLeaderboardData(TypedDict):
	__typename: str
	defaultLeaderboard: str
	isCheerEnabled: Optional[bool]
	isClipEnabled: Optional[bool]
	isSubGiftEnabled: Optional[bool]
	timePeriod: str

class CommunitySupportSettingsResponseUserDataSettingsDataRecentchannelsupporteventsData(TypedDict):
	__typename: str
	isOptedOut: Optional[bool]

class CommunitySupportSettingsResponseUserDataSettingsData(TypedDict):
	__typename: str
	leaderboard: CommunitySupportSettingsResponseUserDataSettingsDataLeaderboardData
	recentChannelSupportEvents: CommunitySupportSettingsResponseUserDataSettingsDataRecentchannelsupporteventsData

class CommunitySupportSettingsResponseUserData(TypedDict):
	__typename: str
	id: str
	login: str
	settings: CommunitySupportSettingsResponseUserDataSettingsData

class CommunitySupportSettingsResponse(TypedDict):
	user: CommunitySupportSettingsResponseUserData

class ClipsExperimentEnrollmentStatusRequest(TypedDict):
	channelID: str

class ClipsExperimentEnrollmentStatusResponseIsenrolledinclipsexperimentData(TypedDict):
	__typename: str
	id: str
	isEnrolled: Optional[bool]

class ClipsExperimentEnrollmentStatusResponse(TypedDict):
	isEnrolledInClipsExperiment: ClipsExperimentEnrollmentStatusResponseIsenrolledinclipsexperimentData

class PaidPinnedChatRequest(TypedDict):
	channelID: str
	count: int
	messageType: str

class PaidPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class PaidPinnedChatResponseChannelDataPinnedchatmessagesData(TypedDict):
	__typename: str
	edges: List[Any]
	pageInfo: PaidPinnedChatResponseChannelDataPinnedchatmessagesDataPageinfoData

class PaidPinnedChatResponseChannelData(TypedDict):
	__typename: str
	id: str
	pinnedChatMessages: PaidPinnedChatResponseChannelDataPinnedchatmessagesData

class PaidPinnedChatResponse(TypedDict):
	channel: PaidPinnedChatResponseChannelData

class ChannelRoot_AboutPanelRequest(TypedDict):
	channelLogin: str
	skipSchedule: Optional[bool]
	includeIsDJ: Optional[bool]

class ChannelRoot_AboutPanelResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str

class ChannelRoot_AboutPanelResponseUserDataChannelDataSocialmediasItem(TypedDict):
	__typename: str
	id: str
	name: str
	title: str
	url: str

class ChannelRoot_AboutPanelResponseUserDataChannelData(TypedDict):
	__typename: str
	id: str
	schedule: Optional[NoneType]
	socialMedias: List[ChannelRoot_AboutPanelResponseUserDataChannelDataSocialmediasItem]

class ChannelRoot_AboutPanelResponseUserDataFollowersData(TypedDict):
	__typename: str
	totalCount: int

class ChannelRoot_AboutPanelResponseUserDataLastbroadcastDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ChannelRoot_AboutPanelResponseUserDataLastbroadcastData(TypedDict):
	__typename: str
	game: ChannelRoot_AboutPanelResponseUserDataLastbroadcastDataGameData
	id: str

class ChannelRoot_AboutPanelResponseUserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]
	isStaff: Optional[NoneType]

class ChannelRoot_AboutPanelResponseUserDataVideosDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ChannelRoot_AboutPanelResponseUserDataVideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	game: ChannelRoot_AboutPanelResponseUserDataVideosDataEdgesItemNodeDataGameData
	id: str
	status: str

class ChannelRoot_AboutPanelResponseUserDataVideosDataEdgesItem(TypedDict):
	__typename: str
	node: ChannelRoot_AboutPanelResponseUserDataVideosDataEdgesItemNodeData

class ChannelRoot_AboutPanelResponseUserDataVideosData(TypedDict):
	__typename: str
	edges: List[ChannelRoot_AboutPanelResponseUserDataVideosDataEdgesItem]

class ChannelRoot_AboutPanelResponseUserData(TypedDict):
	__typename: str
	channel: ChannelRoot_AboutPanelResponseUserDataChannelData
	description: str
	displayName: str
	followers: ChannelRoot_AboutPanelResponseUserDataFollowersData
	id: str
	lastBroadcast: ChannelRoot_AboutPanelResponseUserDataLastbroadcastData
	primaryColorHex: Optional[NoneType]
	primaryTeam: Optional[NoneType]
	profileImageURL: str
	roles: ChannelRoot_AboutPanelResponseUserDataRolesData
	videos: ChannelRoot_AboutPanelResponseUserDataVideosData

class ChannelRoot_AboutPanelResponse(TypedDict):
	currentUser: ChannelRoot_AboutPanelResponseCurrentuserData
	user: ChannelRoot_AboutPanelResponseUserData

class ActiveGoalsRequest(TypedDict):
	channelLogin: str

class ActiveGoalsResponseChannelDataGoalsDataEdgesItemNodeDataCustomizationsData(TypedDict):
	__typename: str
	progressBarAccentColor: Optional[NoneType]
	progressBarBackgroundColor: Optional[NoneType]

class ActiveGoalsResponseChannelDataGoalsDataEdgesItemNodeData(TypedDict):
	__typename: str
	contributionType: str
	createdAt: str
	currentContributions: int
	customizations: ActiveGoalsResponseChannelDataGoalsDataEdgesItemNodeDataCustomizationsData
	description: Optional[NoneType]
	id: str
	shouldAutoIncrement: Optional[bool]
	state: str
	targetContributions: int

class ActiveGoalsResponseChannelDataGoalsDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[str]
	node: ActiveGoalsResponseChannelDataGoalsDataEdgesItemNodeData

class ActiveGoalsResponseChannelDataGoalsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class ActiveGoalsResponseChannelDataGoalsData(TypedDict):
	__typename: str
	edges: List[ActiveGoalsResponseChannelDataGoalsDataEdgesItem]
	pageInfo: ActiveGoalsResponseChannelDataGoalsDataPageinfoData

class ActiveGoalsResponseChannelData(TypedDict):
	__typename: str
	goals: ActiveGoalsResponseChannelDataGoalsData
	id: str

class ActiveGoalsResponse(TypedDict):
	channel: ActiveGoalsResponseChannelData

class DropsHighlightService_AvailableDropsRequest(TypedDict):
	channelID: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemGameData(TypedDict):
	__typename: str
	id: str
	name: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemSummaryData(TypedDict):
	__typename: str
	includesMWRequirement: Optional[bool]
	includesSubRequirement: Optional[bool]
	isPermanentlyDismissible: Optional[bool]
	isRewardCampaign: Optional[bool]
	isSitewide: Optional[bool]

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItemBenefitedgesItemBenefitDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItemBenefitedgesItemBenefitData(TypedDict):
	__typename: str
	game: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItemBenefitedgesItemBenefitDataGameData
	id: str
	imageAssetURL: str
	name: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItemBenefitedgesItem(TypedDict):
	__typename: str
	benefit: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItemBenefitedgesItemBenefitData
	entitlementLimit: int

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItem(TypedDict):
	__typename: str
	benefitEdges: List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItemBenefitedgesItem]
	endAt: str
	id: str
	name: str
	requiredMinutesWatched: int
	requiredSubs: Optional[int]
	startAt: str

class DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItem(TypedDict):
	__typename: str
	detailsURL: str
	endAt: str
	eventBasedDrops: List[Any]
	game: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemGameData
	id: str
	imageURL: str
	name: str
	summary: DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemSummaryData
	timeBasedDrops: List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItemTimebaseddropsItem]

class DropsHighlightService_AvailableDropsResponseChannelData(TypedDict):
	__typename: str
	id: str
	viewerDropCampaigns: List[DropsHighlightService_AvailableDropsResponseChannelDataViewerdropcampaignsItem]

class DropsHighlightService_AvailableDropsResponse(TypedDict):
	channel: DropsHighlightService_AvailableDropsResponseChannelData

class ShoutoutHighlightServiceQueryRequest(TypedDict):
	targetLogin: Optional[str]
	isLoggedOut: Optional[bool]

class ShoutoutHighlightServiceQueryResponse(TypedDict):
	user: Optional[NoneType]

class ChatInput_BadgesRequest(TypedDict):
	...

class ChatInput_BadgesResponseCurrentuserData(TypedDict):
	__typename: str
	chatColor: Optional[NoneType]
	displayName: str
	id: str
	login: str

class ChatInput_BadgesResponse(TypedDict):
	currentUser: ChatInput_BadgesResponseCurrentuserData

class TitleMentionsRequest(TypedDict):
	logins: List[Any]

class TitleMentionsResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isGlobalMod: Optional[NoneType]
	isSiteAdmin: Optional[NoneType]
	isStaff: Optional[NoneType]

class TitleMentionsResponseCurrentuserData(TypedDict):
	__typename: str
	blockedUsers: List[Any]
	id: str
	login: str
	roles: TitleMentionsResponseCurrentuserDataRolesData

class TitleMentionsResponse(TypedDict):
	users: List[Any]
	currentUser: TitleMentionsResponseCurrentuserData

class FollowButton_UserRequest(TypedDict):
	login: str

class FollowButton_UserResponseUserDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: Optional[NoneType]

class FollowButton_UserResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	self: FollowButton_UserResponseUserDataSelfData

class FollowButton_UserResponse(TypedDict):
	user: FollowButton_UserResponseUserData

class PartnerPlusPublicQueryRequest(TypedDict):
	channelID: str

class PartnerPlusPublicQueryResponsePlusstatusDataCreatorpartnerpluswidgetsettingData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]

class PartnerPlusPublicQueryResponsePlusstatusDataPartnerplusprogramDataSubpointsItem(TypedDict):
	__typename: str
	count: int
	month: int
	updatedAt: str
	year: int

class PartnerPlusPublicQueryResponsePlusstatusDataPartnerplusprogramData(TypedDict):
	__typename: str
	canShowWidget: Optional[bool]
	isQualified: Optional[bool]
	subPoints: List[PartnerPlusPublicQueryResponsePlusstatusDataPartnerplusprogramDataSubpointsItem]
	threshold: int
	widgetSetting: str

class PartnerPlusPublicQueryResponsePlusstatusData(TypedDict):
	__typename: str
	creatorPartnerPlusWidgetSetting: PartnerPlusPublicQueryResponsePlusstatusDataCreatorpartnerpluswidgetsettingData
	partnerPlusProgram: PartnerPlusPublicQueryResponsePlusstatusDataPartnerplusprogramData

class PartnerPlusPublicQueryResponse(TypedDict):
	plusStatus: PartnerPlusPublicQueryResponsePlusstatusData

class CanCreateClipRequest(TypedDict):
	broadcasterID: Optional[str]
	vodID: Optional[NoneType]

class CanCreateClipResponseCancreateclipData(TypedDict):
	__typename: str
	errorCode: Optional[NoneType]
	isAllowed: Optional[bool]
	requiredFollowingLengthMinutes: Optional[int]

class CanCreateClipResponse(TypedDict):
	canCreateClip: CanCreateClipResponseCancreateclipData

class PersistentGoalFollowButton_UserRequest(TypedDict):
	login: str

class PersistentGoalFollowButton_UserResponseUserDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: Optional[NoneType]

class PersistentGoalFollowButton_UserResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	self: PersistentGoalFollowButton_UserResponseUserDataSelfData

class PersistentGoalFollowButton_UserResponse(TypedDict):
	user: PersistentGoalFollowButton_UserResponseUserData

class WatchStreakExperimentRequest(TypedDict):
	channelID: str

class WatchStreakExperimentResponseChannelviewermilestonesettingsData(TypedDict):
	__typename: str
	id: str
	isInWatchStreakProgressExperiment: Optional[bool]
	isWatchStreakOptOut: Optional[bool]

class WatchStreakExperimentResponse(TypedDict):
	channelViewerMilestoneSettings: WatchStreakExperimentResponseChannelviewermilestonesettingsData

class Chat_ShareBitsBadgeTier_ChannelDataRequest(TypedDict):
	channelLogin: str

class Chat_ShareBitsBadgeTier_ChannelDataResponseUserDataSelfDataBitsbadgeData(TypedDict):
	__typename: str
	id: str
	tierNotification: Optional[NoneType]

class Chat_ShareBitsBadgeTier_ChannelDataResponseUserDataSelfData(TypedDict):
	__typename: str
	bitsBadge: Chat_ShareBitsBadgeTier_ChannelDataResponseUserDataSelfDataBitsbadgeData

class Chat_ShareBitsBadgeTier_ChannelDataResponseUserData(TypedDict):
	__typename: str
	id: str
	self: Chat_ShareBitsBadgeTier_ChannelDataResponseUserDataSelfData

class Chat_ShareBitsBadgeTier_ChannelDataResponse(TypedDict):
	user: Chat_ShareBitsBadgeTier_ChannelDataResponseUserData

class Chat_ShareResub_ChannelDataRequest(TypedDict):
	channelLogin: str

class Chat_ShareResub_ChannelDataResponseUserDataSelfData(TypedDict):
	__typename: str
	resubNotification: Optional[NoneType]

class Chat_ShareResub_ChannelDataResponseUserData(TypedDict):
	__typename: str
	id: str
	self: Chat_ShareResub_ChannelDataResponseUserDataSelfData

class Chat_ShareResub_ChannelDataResponse(TypedDict):
	user: Chat_ShareResub_ChannelDataResponseUserData

class GetGuestSessionBlocksAndBansRequestSessionoptionsData(TypedDict):
	channelID: str

class GetGuestSessionBlocksAndBansRequest(TypedDict):
	channelID: str
	sessionOptions: GetGuestSessionBlocksAndBansRequestSessionoptionsData

class GetGuestSessionBlocksAndBansResponseUserDataSelfData(TypedDict):
	__typename: str
	banStatus: Optional[NoneType]
	canFollow: Optional[bool]

class GetGuestSessionBlocksAndBansResponseUserData(TypedDict):
	__typename: str
	id: str
	self: GetGuestSessionBlocksAndBansResponseUserDataSelfData

class GetGuestSessionBlocksAndBansResponse(TypedDict):
	user: GetGuestSessionBlocksAndBansResponseUserData
	guestStarSession: Optional[NoneType]

class ChannelPointsAutomaticRewardsRequest(TypedDict):
	login: str

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemDefaultimageData(TypedDict):
	__typename: str
	url: str
	url2x: str
	url4x: str

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemGlobalcooldownsettingData(TypedDict):
	__typename: str
	globalCooldownSeconds: Optional[int]
	isEnabled: Optional[bool]

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperstreamsettingData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	maxPerStream: Optional[int]

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperuserperstreamsettingData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	maxPerUserPerStream: Optional[int]

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItem(TypedDict):
	__typename: str
	backgroundColor: Optional[NoneType]
	bitsCost: Optional[NoneType]
	cooldownExpiresAt: Optional[NoneType]
	cost: Optional[NoneType]
	defaultBackgroundColor: str
	defaultBitsCost: Optional[int]
	defaultCost: int
	defaultImage: ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemDefaultimageData
	globalCooldownSetting: ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemGlobalcooldownsettingData
	globallyUpdatedForIndicatorAt: str
	id: str
	image: Optional[NoneType]
	isEnabled: Optional[bool]
	isHiddenForSubs: Optional[bool]
	isInStock: Optional[bool]
	maxPerStreamSetting: ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperstreamsettingData
	maxPerUserPerStreamSetting: ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItemMaxperuserperstreamsettingData
	minimumCost: int
	pricingType: str
	redemptionsRedeemedCurrentStream: Optional[NoneType]
	type: str
	updatedForIndicatorAt: Optional[NoneType]

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataEarningDataMultipliersItem(TypedDict):
	__typename: str
	factor: float
	reasonCode: str

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataEarningDataWatchstreakpointsItem(TypedDict):
	__typename: str
	points: int

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataEarningData(TypedDict):
	__typename: str
	averagePointsPerHour: int
	cheerPoints: int
	claimPoints: int
	followPoints: int
	id: str
	multipliers: List[ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataEarningDataMultipliersItem]
	passiveWatchPoints: int
	raidPoints: int
	subscriptionGiftPoints: int
	watchStreakPoints: List[ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataEarningDataWatchstreakpointsItem]

class ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsData(TypedDict):
	__typename: str
	automaticRewards: List[ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataAutomaticrewardsItem]
	earning: ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsDataEarningData
	smartCostsAcknowledgements: Optional[NoneType]

class ChannelPointsAutomaticRewardsResponseUserDataChannelData(TypedDict):
	__typename: str
	communityPointsSettings: ChannelPointsAutomaticRewardsResponseUserDataChannelDataCommunitypointssettingsData
	id: str

class ChannelPointsAutomaticRewardsResponseUserData(TypedDict):
	__typename: str
	channel: ChannelPointsAutomaticRewardsResponseUserDataChannelData
	id: str

class ChannelPointsAutomaticRewardsResponse(TypedDict):
	user: ChannelPointsAutomaticRewardsResponseUserData

class ChannelLeaderboardsRequest(TypedDict):
	first: int
	isClipLeaderboardEnabled: Optional[bool]
	channelID: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesItemNodeDataUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesItemNodeData(TypedDict):
	__typename: str
	id: str
	rank: int
	score: int
	user: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesItemNodeDataUserData

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesItemNodeData

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsData(TypedDict):
	__typename: str
	edges: List[ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsDataEdgesItem]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsData(TypedDict):
	__typename: str
	id: str
	items: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsDataItemsData
	myPosition: Optional[NoneType]
	secondsRemaining: Optional[int]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesItemNodeDataUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesItemNodeData(TypedDict):
	__typename: str
	id: str
	rank: int
	score: int
	user: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesItemNodeDataUserData

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesItemNodeData

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsData(TypedDict):
	__typename: str
	edges: List[ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsDataEdgesItem]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftData(TypedDict):
	__typename: str
	id: str
	items: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftDataItemsData
	myPosition: Optional[NoneType]
	secondsRemaining: Optional[int]

class ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetData(TypedDict):
	__typename: str
	bits: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataBitsData
	subGift: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetDataSubgiftData

class ChannelLeaderboardsResponseUserDataChannelData(TypedDict):
	__typename: str
	id: str
	leaderboardSet: ChannelLeaderboardsResponseUserDataChannelDataLeaderboardsetData
	leaderboardTimePeriod: str

class ChannelLeaderboardsResponseUserDataCheerDataSettingsData(TypedDict):
	__typename: str
	cheerMinimumBits: int
	id: str

class ChannelLeaderboardsResponseUserDataCheerData(TypedDict):
	__typename: str
	id: str
	settings: ChannelLeaderboardsResponseUserDataCheerDataSettingsData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData
	previewPrice: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData(TypedDict):
	__typename: str
	internal: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData(TypedDict):
	__typename: str
	chargeModel: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData(TypedDict):
	__typename: str
	eligibility: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData
	giftType: str
	id: str
	listing: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataQuantityData
	tagBindings: List[ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataTagbindingsItem]
	tplr: str

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem(TypedDict):
	__typename: str
	offer: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingData(TypedDict):
	__typename: str
	community: List[ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem]

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItemPriceinfoData(TypedDict):
	__typename: str
	currency: str
	exponent: int
	id: str
	price: int

class ChannelLeaderboardsResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	gifting: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemGiftingData
	id: str
	name: str
	price: str
	priceInfo: ChannelLeaderboardsResponseUserDataSubscriptionproductsItemPriceinfoData

class ChannelLeaderboardsResponseUserData(TypedDict):
	__typename: str
	channel: ChannelLeaderboardsResponseUserDataChannelData
	cheer: ChannelLeaderboardsResponseUserDataCheerData
	displayName: str
	id: str
	login: str
	subscriptionProducts: List[ChannelLeaderboardsResponseUserDataSubscriptionproductsItem]

class ChannelLeaderboardsResponseCurrentuserData(TypedDict):
	__typename: str
	id: str

class ChannelLeaderboardsResponse(TypedDict):
	user: ChannelLeaderboardsResponseUserData
	currentUser: ChannelLeaderboardsResponseCurrentuserData

class BannerNotificationQueryRequest(TypedDict):
	platform: str

class BannerNotificationQueryResponseMoneybannernotificationsItem(TypedDict):
	__typename: str
	id: str
	location: str
	metadata: Optional[NoneType]
	position: str
	priority: int

class BannerNotificationQueryResponse(TypedDict):
	moneyBannerNotifications: List[BannerNotificationQueryResponseMoneybannernotificationsItem]

class StoryChannelQueryRequest(TypedDict):
	channelLogin: str

class StoryChannelQueryResponseUserData(TypedDict):
	__typename: str
	id: str

class StoryChannelQueryResponse(TypedDict):
	user: StoryChannelQueryResponseUserData

class ChannelSupportButtonsRequest(TypedDict):
	channelLogin: str

class ChannelSupportButtonsResponseUserDataSelfDataFollowerData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]

class ChannelSupportButtonsResponseUserDataSelfData(TypedDict):
	__typename: str
	follower: ChannelSupportButtonsResponseUserDataSelfDataFollowerData

class ChannelSupportButtonsResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	self: ChannelSupportButtonsResponseUserDataSelfData

class ChannelSupportButtonsResponse(TypedDict):
	user: ChannelSupportButtonsResponseUserData

class AcknowledgeUnbanRequestPromptRequest(TypedDict):
	channelLogin: str

class AcknowledgeUnbanRequestPromptResponseChannelData(TypedDict):
	__typename: str
	id: str
	profileImageURL: str

class AcknowledgeUnbanRequestPromptResponse(TypedDict):
	channel: AcknowledgeUnbanRequestPromptResponseChannelData

class VideoMarkersChatCommandRequest(TypedDict):
	channelLogin: str

class VideoMarkersChatCommandResponseUserDataStreamData(TypedDict):
	__typename: str
	createdAt: str
	id: str

class VideoMarkersChatCommandResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: VideoMarkersChatCommandResponseUserDataStreamData

class VideoMarkersChatCommandResponse(TypedDict):
	user: VideoMarkersChatCommandResponseUserData

class CommercialCommandHandler_ChannelDataRequest(TypedDict):
	channelLogin: str

class CommercialCommandHandler_ChannelDataResponseChannelDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]

class CommercialCommandHandler_ChannelDataResponseChannelData(TypedDict):
	__typename: str
	id: str
	roles: CommercialCommandHandler_ChannelDataResponseChannelDataRolesData

class CommercialCommandHandler_ChannelDataResponse(TypedDict):
	channel: CommercialCommandHandler_ChannelDataResponseChannelData

class AccessIsAffiliateQueryRequest(TypedDict):
	channelLogin: str
	isChannelLoginSameAsUserLogin: Optional[bool]

class AccessIsAffiliateQueryResponseUserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]

class AccessIsAffiliateQueryResponseUserData(TypedDict):
	__typename: str
	id: str
	roles: AccessIsAffiliateQueryResponseUserDataRolesData

class AccessIsAffiliateQueryResponse(TypedDict):
	user: AccessIsAffiliateQueryResponseUserData

class AccessIsPartnerQueryRequest(TypedDict):
	channelLogin: str
	isChannelLoginSameAsUserLogin: Optional[bool]

class AccessIsPartnerQueryResponseUserDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class AccessIsPartnerQueryResponseUserData(TypedDict):
	__typename: str
	id: str
	roles: AccessIsPartnerQueryResponseUserDataRolesData

class AccessIsPartnerQueryResponse(TypedDict):
	user: AccessIsPartnerQueryResponseUserData

class CommunityPointsChatPrivateCalloutUserRequest(TypedDict):
	login: str

class CommunityPointsChatPrivateCalloutUserResponseUserDataSelfData(TypedDict):
	__typename: str
	isModerator: Optional[bool]
	subscriptionBenefit: Optional[NoneType]

class CommunityPointsChatPrivateCalloutUserResponseUserData(TypedDict):
	__typename: str
	id: str
	self: CommunityPointsChatPrivateCalloutUserResponseUserDataSelfData

class CommunityPointsChatPrivateCalloutUserResponse(TypedDict):
	user: CommunityPointsChatPrivateCalloutUserResponseUserData

class Chat_EarnedBadges_InitialSubStatusRequest(TypedDict):
	channelLogin: str

class Chat_EarnedBadges_InitialSubStatusResponseUserDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class Chat_EarnedBadges_InitialSubStatusResponseUserData(TypedDict):
	__typename: str
	id: str
	self: Chat_EarnedBadges_InitialSubStatusResponseUserDataSelfData

class Chat_EarnedBadges_InitialSubStatusResponse(TypedDict):
	user: Chat_EarnedBadges_InitialSubStatusResponseUserData

class StreamEventsActiveCelebrationCalloutQueryRequest(TypedDict):
	channelID: str

class StreamEventsActiveCelebrationCalloutQueryResponseChannelData(TypedDict):
	__typename: str
	activeStreamEventCelebration: Optional[NoneType]
	id: str

class StreamEventsActiveCelebrationCalloutQueryResponse(TypedDict):
	channel: StreamEventsActiveCelebrationCalloutQueryResponseChannelData

class CollaborationPromoPrivateCalloutRequest(TypedDict):
	channelID: str

class CollaborationPromoPrivateCalloutResponse(TypedDict):
	sharedChatSession: Optional[NoneType]

class CommunityPointsAvailableClaimRequest(TypedDict):
	channelID: str

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData(TypedDict):
	__typename: str
	id: str

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsData(TypedDict):
	__typename: str
	activeMultipliers: List[Any]
	availableClaim: CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsDataAvailableclaimData
	balance: int
	canRedeemRewardsForFree: Optional[bool]

class CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfData(TypedDict):
	__typename: str
	communityPoints: CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfDataCommunitypointsData

class CommunityPointsAvailableClaimResponseCommunityDataChannelData(TypedDict):
	__typename: str
	id: str
	self: CommunityPointsAvailableClaimResponseCommunityDataChannelDataSelfData

class CommunityPointsAvailableClaimResponseCommunityData(TypedDict):
	__typename: str
	channel: CommunityPointsAvailableClaimResponseCommunityDataChannelData
	id: str
	login: str

class CommunityPointsAvailableClaimResponse(TypedDict):
	community: CommunityPointsAvailableClaimResponseCommunityData

class ExtensionsInfoBalloonRequest(TypedDict):
	extensionID: str
	extensionVersion: str

class ExtensionsInfoBalloonResponseExtensionData(TypedDict):
	__typename: str
	id: str
	screenshotURLs: List[str]

class ExtensionsInfoBalloonResponse(TypedDict):
	extension: ExtensionsInfoBalloonResponseExtensionData

class updateUserViewedVideoRequestInputData(TypedDict):
	position: int
	userID: str
	videoID: str
	videoType: str

class updateUserViewedVideoRequest(TypedDict):
	input: updateUserViewedVideoRequestInputData

class updateUserViewedVideoResponseUpdateuserviewedvideoData(TypedDict):
	__typename: str
	video: Optional[NoneType]

class updateUserViewedVideoResponse(TypedDict):
	updateUserViewedVideo: updateUserViewedVideoResponseUpdateuserviewedvideoData

class ChannelPanelsRequest(TypedDict):
	id: str

class ChannelPanelsResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isSiteAdmin: Optional[NoneType]
	isStaff: Optional[NoneType]

class ChannelPanelsResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str
	roles: ChannelPanelsResponseCurrentuserDataRolesData

class ChannelPanelsResponseUserDataCheerData(TypedDict):
	__typename: str
	id: str

class ChannelPanelsResponseUserDataPanelsItem(TypedDict):
	__typename: str
	altText: Optional[NoneType]
	description: Optional[NoneType]
	id: str
	imageURL: str
	linkURL: str
	title: str
	type: str

class ChannelPanelsResponseUserDataSelfData(TypedDict):
	__typename: str
	banStatus: Optional[NoneType]

class ChannelPanelsResponseUserData(TypedDict):
	__typename: str
	cheer: ChannelPanelsResponseUserDataCheerData
	id: str
	login: str
	panels: List[ChannelPanelsResponseUserDataPanelsItem]
	self: ChannelPanelsResponseUserDataSelfData

class ChannelPanelsResponse(TypedDict):
	currentUser: ChannelPanelsResponseCurrentuserData
	user: ChannelPanelsResponseUserData

class ExtensionProductsRequest(TypedDict):
	extensionID: str
	version: str

class ExtensionProductsResponseExtensionDataProductsItemCostData(TypedDict):
	__typename: str
	amount: int
	type: str

class ExtensionProductsResponseExtensionDataProductsItem(TypedDict):
	__typename: str
	cost: ExtensionProductsResponseExtensionDataProductsItemCostData
	displayName: str
	isInDevelopment: Optional[bool]
	sku: str

class ExtensionProductsResponseExtensionData(TypedDict):
	__typename: str
	products: List[ExtensionProductsResponseExtensionDataProductsItem]

class ExtensionProductsResponse(TypedDict):
	extension: ExtensionProductsResponseExtensionData

class HomeOfflineCarouselRequest(TypedDict):
	channelLogin: str
	includeTrailerUpsell: Optional[bool]
	trailerUpsellVideoID: str

class HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str

class HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItemNodeDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	description: Optional[NoneType]
	game: HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItemNodeDataGameData
	id: str
	owner: HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItemNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	title: str

class HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItem(TypedDict):
	__typename: str
	node: HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItemNodeData

class HomeOfflineCarouselResponse1UserDataArchivevideosData(TypedDict):
	__typename: str
	edges: List[HomeOfflineCarouselResponse1UserDataArchivevideosDataEdgesItem]

class HomeOfflineCarouselResponse1UserDataChannelDataHomeData(TypedDict):
	__typename: str
	autohostCarouselCard: Optional[NoneType]

class HomeOfflineCarouselResponse1UserDataChannelDataScheduleDataNextsegmentData(TypedDict):
	__typename: str
	id: str
	startAt: str

class HomeOfflineCarouselResponse1UserDataChannelDataScheduleData(TypedDict):
	__typename: str
	id: str
	nextSegment: HomeOfflineCarouselResponse1UserDataChannelDataScheduleDataNextsegmentData

class HomeOfflineCarouselResponse1UserDataChannelDataSocialmediasItem(TypedDict):
	__typename: str
	id: str
	name: str
	title: str
	url: str

class HomeOfflineCarouselResponse1UserDataChannelDataTrailerData(TypedDict):
	__typename: str
	video: Optional[NoneType]

class HomeOfflineCarouselResponse1UserDataChannelData(TypedDict):
	__typename: str
	home: HomeOfflineCarouselResponse1UserDataChannelDataHomeData
	id: str
	schedule: HomeOfflineCarouselResponse1UserDataChannelDataScheduleData
	socialMedias: List[HomeOfflineCarouselResponse1UserDataChannelDataSocialmediasItem]
	trailer: HomeOfflineCarouselResponse1UserDataChannelDataTrailerData

class HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str

class HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItemNodeDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	description: Optional[NoneType]
	game: HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItemNodeDataGameData
	id: str
	owner: HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItemNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	title: str

class HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItem(TypedDict):
	__typename: str
	node: HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItemNodeData

class HomeOfflineCarouselResponse1UserDataHighlightvideosData(TypedDict):
	__typename: str
	edges: List[HomeOfflineCarouselResponse1UserDataHighlightvideosDataEdgesItem]

class HomeOfflineCarouselResponse1UserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]
	isStaff: Optional[NoneType]

class HomeOfflineCarouselResponse1UserDataSelfDataFollowerData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]

class HomeOfflineCarouselResponse1UserDataSelfData(TypedDict):
	__typename: str
	follower: HomeOfflineCarouselResponse1UserDataSelfDataFollowerData
	isEditor: Optional[bool]
	subscriptionBenefit: Optional[NoneType]

class HomeOfflineCarouselResponse1UserData(TypedDict):
	__typename: str
	archiveVideos: HomeOfflineCarouselResponse1UserDataArchivevideosData
	channel: HomeOfflineCarouselResponse1UserDataChannelData
	description: str
	displayName: str
	highlightVideos: HomeOfflineCarouselResponse1UserDataHighlightvideosData
	id: str
	login: str
	roles: HomeOfflineCarouselResponse1UserDataRolesData
	self: HomeOfflineCarouselResponse1UserDataSelfData

class HomeOfflineCarouselResponse1(TypedDict):
	user: HomeOfflineCarouselResponse1UserData

class HomeOfflineCarouselResponse2UserDataArchivevideosData(TypedDict):
	__typename: str
	edges: List[Any]

class HomeOfflineCarouselResponse2UserDataChannelDataHomeData(TypedDict):
	__typename: str
	autohostCarouselCard: Optional[NoneType]

class HomeOfflineCarouselResponse2UserDataChannelDataTrailerData(TypedDict):
	__typename: str
	video: Optional[NoneType]

class HomeOfflineCarouselResponse2UserDataChannelData(TypedDict):
	__typename: str
	home: HomeOfflineCarouselResponse2UserDataChannelDataHomeData
	id: str
	schedule: Optional[NoneType]
	socialMedias: List[Any]
	trailer: HomeOfflineCarouselResponse2UserDataChannelDataTrailerData

class HomeOfflineCarouselResponse2UserDataHighlightvideosData(TypedDict):
	__typename: str
	edges: List[Any]

class HomeOfflineCarouselResponse2UserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]
	isStaff: Optional[NoneType]

class HomeOfflineCarouselResponse2UserDataSelfData(TypedDict):
	__typename: str
	follower: Optional[NoneType]
	isEditor: Optional[bool]
	subscriptionBenefit: Optional[NoneType]

class HomeOfflineCarouselResponse2UserData(TypedDict):
	__typename: str
	archiveVideos: HomeOfflineCarouselResponse2UserDataArchivevideosData
	channel: HomeOfflineCarouselResponse2UserDataChannelData
	description: Optional[NoneType]
	displayName: str
	highlightVideos: HomeOfflineCarouselResponse2UserDataHighlightvideosData
	id: str
	login: str
	roles: HomeOfflineCarouselResponse2UserDataRolesData
	self: HomeOfflineCarouselResponse2UserDataSelfData

class HomeOfflineCarouselResponse2TrailerupsellvideoDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class HomeOfflineCarouselResponse2TrailerupsellvideoData(TypedDict):
	__typename: str
	description: Optional[NoneType]
	game: Optional[NoneType]
	id: str
	owner: HomeOfflineCarouselResponse2TrailerupsellvideoDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	title: str

class HomeOfflineCarouselResponse2(TypedDict):
	user: HomeOfflineCarouselResponse2UserData
	trailerUpsellVideo: HomeOfflineCarouselResponse2TrailerupsellvideoData

class ChannelAvatarRequest(TypedDict):
	channelLogin: str
	includeIsDJ: Optional[bool]

class ChannelAvatarResponseUserDataFollowersData(TypedDict):
	__typename: str
	totalCount: int

class ChannelAvatarResponseUserDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class ChannelAvatarResponseUserData(TypedDict):
	__typename: str
	followers: ChannelAvatarResponseUserDataFollowersData
	id: str
	primaryColorHex: str
	roles: ChannelAvatarResponseUserDataRolesData

class ChannelAvatarResponse(TypedDict):
	user: ChannelAvatarResponseUserData

class LowerHomeHeaderRequest(TypedDict):
	channelLogin: str

class LowerHomeHeaderResponseUserDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class LowerHomeHeaderResponseUserData(TypedDict):
	__typename: str
	id: str
	self: LowerHomeHeaderResponseUserDataSelfData

class LowerHomeHeaderResponse(TypedDict):
	user: LowerHomeHeaderResponseUserData

class RoleRestrictedRequest(TypedDict):
	contentOwnerLogin: str

class RoleRestrictedResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isStaff: Optional[NoneType]

class RoleRestrictedResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	roles: RoleRestrictedResponseCurrentuserDataRolesData

class RoleRestrictedResponseUserDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class RoleRestrictedResponseUserData(TypedDict):
	__typename: str
	id: str
	self: RoleRestrictedResponseUserDataSelfData

class RoleRestrictedResponse(TypedDict):
	currentUser: RoleRestrictedResponseCurrentuserData
	user: RoleRestrictedResponseUserData

class ChannelVideoShelvesQueryRequest(TypedDict):
	includePreviewBlur: Optional[bool]
	channelLogin: str
	first: int

class ChannelVideoShelvesQueryResponseCurrentuserData(TypedDict):
	__typename: str
	id: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterDataRolesData

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemClipgameData(TypedDict):
	__typename: str
	boxArtURL: str
	id: str
	name: str
	slug: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemCuratorData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemGueststarparticipantsData(TypedDict):
	__typename: str
	guests: List[Any]
	sessionIdentifier: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItem(TypedDict):
	__typename: str
	broadcaster: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterData
	clipGame: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemClipgameData
	clipTitle: str
	clipViewCount: int
	createdAt: str
	curator: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemCuratorData
	durationSeconds: int
	guestStarParticipants: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemGueststarparticipantsData
	id: str
	isFeatured: Optional[bool]
	slug: str
	thumbnailURL: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeData(TypedDict):
	__typename: str
	collection: Optional[NoneType]
	description: Optional[NoneType]
	id: str
	items: List[ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItem]
	title: str
	type: str

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItemNodeData

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class ChannelVideoShelvesQueryResponseUserDataVideoshelvesData(TypedDict):
	__typename: str
	edges: List[ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataEdgesItem]
	pageInfo: ChannelVideoShelvesQueryResponseUserDataVideoshelvesDataPageinfoData

class ChannelVideoShelvesQueryResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	primaryColorHex: str
	videoShelves: ChannelVideoShelvesQueryResponseUserDataVideoshelvesData

class ChannelVideoShelvesQueryResponse(TypedDict):
	currentUser: ChannelVideoShelvesQueryResponseCurrentuserData
	user: ChannelVideoShelvesQueryResponseUserData

class HomeTrackQueryRequest(TypedDict):
	channelLogin: str

class HomeTrackQueryResponseUserDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	language: str

class HomeTrackQueryResponseUserDataLastbroadcastDataGameData(TypedDict):
	__typename: str
	id: str
	name: str

class HomeTrackQueryResponseUserDataLastbroadcastData(TypedDict):
	__typename: str
	game: HomeTrackQueryResponseUserDataLastbroadcastDataGameData
	id: str

class HomeTrackQueryResponseUserDataSelfDataFollowerDataNodeData(TypedDict):
	__typename: str
	id: str

class HomeTrackQueryResponseUserDataSelfDataFollowerData(TypedDict):
	__typename: str
	node: HomeTrackQueryResponseUserDataSelfDataFollowerDataNodeData

class HomeTrackQueryResponseUserDataSelfData(TypedDict):
	__typename: str
	follower: HomeTrackQueryResponseUserDataSelfDataFollowerData

class HomeTrackQueryResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str

class HomeTrackQueryResponseUserData(TypedDict):
	__typename: str
	broadcastSettings: HomeTrackQueryResponseUserDataBroadcastsettingsData
	id: str
	lastBroadcast: HomeTrackQueryResponseUserDataLastbroadcastData
	self: HomeTrackQueryResponseUserDataSelfData
	stream: HomeTrackQueryResponseUserDataStreamData

class HomeTrackQueryResponse(TypedDict):
	user: HomeTrackQueryResponseUserData

class ChatFilterContextManager_UserRequest(TypedDict):
	...

class ChatFilterContextManager_UserResponseCurrentuserData(TypedDict):
	__typename: str
	createdAt: str
	id: str

class ChatFilterContextManager_UserResponse(TypedDict):
	currentUser: ChatFilterContextManager_UserResponseCurrentuserData

class PbyPGameRequest(TypedDict):
	channelLogin: str
	tagType: str

class PbyPGameResponseUserDataStreamDataGameDataTagsItem(TypedDict):
	__typename: str
	id: str
	tagName: str

class PbyPGameResponseUserDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str
	tags: List[PbyPGameResponseUserDataStreamDataGameDataTagsItem]

class PbyPGameResponseUserDataStreamData(TypedDict):
	__typename: str
	game: PbyPGameResponseUserDataStreamDataGameData
	id: str

class PbyPGameResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: PbyPGameResponseUserDataStreamData

class PbyPGameResponse(TypedDict):
	user: PbyPGameResponseUserData

class FeaturedClipsShelfCoverRequest(TypedDict):
	channelID: str

class FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsItemEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	order: Optional[int]
	subscriptionTier: str
	token: str

class FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	emotes: List[FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsItemEmotesItem]
	id: str

class FeaturedClipsShelfCoverResponseUserData(TypedDict):
	__typename: str
	id: str
	subscriptionProducts: List[FeaturedClipsShelfCoverResponseUserDataSubscriptionproductsItem]

class FeaturedClipsShelfCoverResponse(TypedDict):
	user: FeaturedClipsShelfCoverResponseUserData

class VideoPreviewCard__VideoMomentsRequest(TypedDict):
	videoId: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeDataDetailsDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	slug: str

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeDataDetailsData(TypedDict):
	__typename: str
	game: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeDataDetailsDataGameData

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeDataVideoData(TypedDict):
	__typename: str
	id: str
	lengthSeconds: int

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeData(TypedDict):
	__typename: str
	description: str
	details: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeDataDetailsData
	durationMilliseconds: int
	id: str
	positionMilliseconds: Optional[int]
	thumbnailURL: Optional[str]
	type: str
	video: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeDataVideoData

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[str]
	node: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItemNodeData

class VideoPreviewCard__VideoMomentsResponseVideoDataMomentsData(TypedDict):
	__typename: str
	edges: List[VideoPreviewCard__VideoMomentsResponseVideoDataMomentsDataEdgesItem]

class VideoPreviewCard__VideoMomentsResponseVideoData(TypedDict):
	__typename: str
	id: str
	moments: VideoPreviewCard__VideoMomentsResponseVideoDataMomentsData

class VideoPreviewCard__VideoMomentsResponse(TypedDict):
	video: VideoPreviewCard__VideoMomentsResponseVideoData

class ClipsCards__UserRequestCriteriaData(TypedDict):
	filter: str
	shouldFilterByDiscoverySetting: Optional[bool]

class ClipsCards__UserRequest(TypedDict):
	login: str
	limit: int
	criteria: ClipsCards__UserRequestCriteriaData
	cursor: Optional[NoneType]

class ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataBroadcasterDataRolesData

class ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataCuratorData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	id: str
	name: str
	slug: str

class ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataBroadcasterData
	champBadge: Optional[NoneType]
	createdAt: str
	curator: ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataCuratorData
	durationSeconds: int
	embedURL: str
	game: ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeDataGameData
	guestStarParticipants: Optional[NoneType]
	id: str
	isFeatured: Optional[bool]
	language: str
	slug: str
	thumbnailURL: str
	title: str
	url: str
	viewCount: int

class ClipsCards__UserResponseUserDataClipsDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[NoneType]
	node: ClipsCards__UserResponseUserDataClipsDataEdgesItemNodeData

class ClipsCards__UserResponseUserDataClipsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class ClipsCards__UserResponseUserDataClipsData(TypedDict):
	__typename: str
	edges: List[ClipsCards__UserResponseUserDataClipsDataEdgesItem]
	pageInfo: ClipsCards__UserResponseUserDataClipsDataPageinfoData

class ClipsCards__UserResponseUserData(TypedDict):
	__typename: str
	clips: ClipsCards__UserResponseUserDataClipsData
	id: str

class ClipsCards__UserResponse(TypedDict):
	user: ClipsCards__UserResponseUserData

class StreamScheduleRequest(TypedDict):
	login: str
	startingWeekday: str
	utcOffsetMinutes: int
	startAt: str
	endAt: str

class StreamScheduleResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str

class StreamScheduleResponseUserDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class StreamScheduleResponseUserDataChannelDataScheduleDataNextsegmentData(TypedDict):
	__typename: str
	id: str
	startAt: str

class StreamScheduleResponseUserDataChannelDataScheduleDataSegmentsItem(TypedDict):
	__typename: str
	baseSegmentID: str
	cancelledUntil: Optional[NoneType]
	categories: List[Any]
	endAt: Optional[NoneType]
	hasReminder: Optional[bool]
	id: str
	isCancelled: Optional[bool]
	repeatEndsAfterCount: Optional[int]
	startAt: str
	title: str

class StreamScheduleResponseUserDataChannelDataScheduleData(TypedDict):
	__typename: str
	id: str
	interruption: Optional[NoneType]
	nextSegment: StreamScheduleResponseUserDataChannelDataScheduleDataNextsegmentData
	segments: List[StreamScheduleResponseUserDataChannelDataScheduleDataSegmentsItem]

class StreamScheduleResponseUserDataChannelData(TypedDict):
	__typename: str
	id: str
	schedule: StreamScheduleResponseUserDataChannelDataScheduleData

class StreamScheduleResponseUserDataLastbroadcastData(TypedDict):
	__typename: str
	id: str
	startedAt: str

class StreamScheduleResponseUserDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str
	slug: str

class StreamScheduleResponseUserDataStreamData(TypedDict):
	__typename: str
	createdAt: str
	game: StreamScheduleResponseUserDataStreamDataGameData
	id: str
	previewImageURL: str
	viewersCount: int

class StreamScheduleResponseUserDataVideosData(TypedDict):
	__typename: str
	edges: List[Any]

class StreamScheduleResponseUserData(TypedDict):
	__typename: str
	broadcastSettings: StreamScheduleResponseUserDataBroadcastsettingsData
	channel: StreamScheduleResponseUserDataChannelData
	id: str
	lastBroadcast: StreamScheduleResponseUserDataLastbroadcastData
	primaryColorHex: str
	stream: StreamScheduleResponseUserDataStreamData
	videos: StreamScheduleResponseUserDataVideosData

class StreamScheduleResponse(TypedDict):
	currentUser: StreamScheduleResponseCurrentuserData
	user: StreamScheduleResponseUserData

class FilterableVideoTower_VideosRequest1(TypedDict):
	includePreviewBlur: Optional[bool]
	limit: int
	channelOwnerLogin: str
	broadcastType: str
	videoSort: str

class FilterableVideoTower_VideosRequest2(TypedDict):
	includePreviewBlur: Optional[bool]
	limit: int
	channelOwnerLogin: str
	broadcastType: str
	videoSort: str
	cursor: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataOwnerDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataOwnerDataRolesData

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataSelfDataViewinghistoryData(TypedDict):
	__typename: str
	position: int
	updatedAt: str

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataSelfData(TypedDict):
	__typename: str
	isRestricted: Optional[bool]
	viewingHistory: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataSelfDataViewinghistoryData

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	animatedPreviewURL: str
	contentTags: List[Any]
	game: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataGameData
	id: str
	lengthSeconds: int
	owner: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	resourceRestriction: Optional[NoneType]
	self: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeDataSelfData
	title: str
	viewCount: int

class FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItemNodeData

class FilterableVideoTower_VideosResponseUserDataVideosDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class FilterableVideoTower_VideosResponseUserDataVideosData(TypedDict):
	__typename: str
	edges: List[FilterableVideoTower_VideosResponseUserDataVideosDataEdgesItem]
	pageInfo: FilterableVideoTower_VideosResponseUserDataVideosDataPageinfoData

class FilterableVideoTower_VideosResponseUserData(TypedDict):
	__typename: str
	id: str
	videos: FilterableVideoTower_VideosResponseUserDataVideosData

class FilterableVideoTower_VideosResponse(TypedDict):
	user: FilterableVideoTower_VideosResponseUserData

class queryUserViewedVideoRequest(TypedDict):
	...

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesItemHistoryData(TypedDict):
	__typename: str
	position: int

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	id: str

class queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesItem(TypedDict):
	__typename: str
	history: queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesItemHistoryData
	node: queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesItemNodeData

class queryUserViewedVideoResponseCurrentuserDataViewedvideosData(TypedDict):
	__typename: str
	edges: List[queryUserViewedVideoResponseCurrentuserDataViewedvideosDataEdgesItem]

class queryUserViewedVideoResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	viewedVideos: queryUserViewedVideoResponseCurrentuserDataViewedvideosData

class queryUserViewedVideoResponse(TypedDict):
	currentUser: queryUserViewedVideoResponseCurrentuserData

class VODMidrollManagerRequest(TypedDict):
	isVOD: Optional[bool]
	vodID: str
	isCollection: Optional[bool]
	collectionID: Optional[str]

class VODMidrollManagerResponseVideoDataOwnerDataAdpropertiesData(TypedDict):
	__typename: str
	hasVodAdsEnabled: Optional[bool]
	vodArchiveMidrolls: str
	vodArchiveMidrollsBreakLength: int
	vodArchiveMidrollsFrequency: int

class VODMidrollManagerResponseVideoDataOwnerData(TypedDict):
	__typename: str
	adProperties: VODMidrollManagerResponseVideoDataOwnerDataAdpropertiesData
	id: str

class VODMidrollManagerResponseVideoData(TypedDict):
	__typename: str
	broadcastType: str
	id: str
	owner: VODMidrollManagerResponseVideoDataOwnerData

class VODMidrollManagerResponse(TypedDict):
	video: VODMidrollManagerResponseVideoData

class VideoPlayer_VODSeekbarRequest(TypedDict):
	includePrivate: Optional[bool]
	vodID: str

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesItem(TypedDict):
	__typename: str
	duration: int
	offset: int

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionData(TypedDict):
	__typename: str
	nodes: List[VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesItem]

class VideoPlayer_VODSeekbarResponseVideoDataMuteinfoData(TypedDict):
	__typename: str
	mutedSegmentConnection: VideoPlayer_VODSeekbarResponseVideoDataMuteinfoDataMutedsegmentconnectionData

class VideoPlayer_VODSeekbarResponseVideoData(TypedDict):
	__typename: str
	id: str
	lengthSeconds: int
	muteInfo: VideoPlayer_VODSeekbarResponseVideoDataMuteinfoData

class VideoPlayer_VODSeekbarResponse(TypedDict):
	video: VideoPlayer_VODSeekbarResponseVideoData

class VideoPlayer_ChapterSelectButtonVideoRequest(TypedDict):
	includePrivate: Optional[bool]
	videoID: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataDetailsDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataDetailsData(TypedDict):
	__typename: str
	game: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataDetailsDataGameData

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataMomentsData(TypedDict):
	__typename: str
	edges: List[Any]

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataVideoData(TypedDict):
	__typename: str
	id: str
	lengthSeconds: int

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeData(TypedDict):
	__typename: str
	description: str
	details: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataDetailsData
	durationMilliseconds: int
	id: str
	moments: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataMomentsData
	positionMilliseconds: Optional[int]
	subDescription: Optional[str]
	thumbnailURL: Optional[str]
	type: str
	video: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeDataVideoData

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItem(TypedDict):
	__typename: str
	node: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItemNodeData

class VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsData(TypedDict):
	__typename: str
	edges: List[VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsDataEdgesItem]

class VideoPlayer_ChapterSelectButtonVideoResponseVideoData(TypedDict):
	__typename: str
	id: str
	moments: VideoPlayer_ChapterSelectButtonVideoResponseVideoDataMomentsData

class VideoPlayer_ChapterSelectButtonVideoResponse(TypedDict):
	video: VideoPlayer_ChapterSelectButtonVideoResponseVideoData

class VideoCommentsRequest(TypedDict):
	videoID: str
	hasVideoID: Optional[bool]

class VideoCommentsResponseBadgesItem(TypedDict):
	__typename: str
	clickAction: str
	clickURL: str
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class VideoCommentsResponseCheerconfigDataDisplayconfigDataColorsItem(TypedDict):
	__typename: str
	bits: int
	color: str

class VideoCommentsResponseCheerconfigDataDisplayconfigDataTypesItem(TypedDict):
	__typename: str
	animation: str
	extension: str

class VideoCommentsResponseCheerconfigDataDisplayconfigData(TypedDict):
	__typename: str
	backgrounds: List[str]
	colors: List[VideoCommentsResponseCheerconfigDataDisplayconfigDataColorsItem]
	order: List[str]
	scales: List[str]
	types: List[VideoCommentsResponseCheerconfigDataDisplayconfigDataTypesItem]

class VideoCommentsResponseCheerconfigDataGroupsItemNodesItemTiersItem(TypedDict):
	__typename: str
	bits: int
	canShowInBitsCard: Optional[bool]
	id: str

class VideoCommentsResponseCheerconfigDataGroupsItemNodesItem(TypedDict):
	__typename: str
	campaign: Optional[NoneType]
	id: str
	prefix: str
	tiers: List[VideoCommentsResponseCheerconfigDataGroupsItemNodesItemTiersItem]
	type: str

class VideoCommentsResponseCheerconfigDataGroupsItem(TypedDict):
	__typename: str
	nodes: List[VideoCommentsResponseCheerconfigDataGroupsItemNodesItem]
	templateURL: str

class VideoCommentsResponseCheerconfigData(TypedDict):
	__typename: str
	displayConfig: VideoCommentsResponseCheerconfigDataDisplayconfigData
	groups: List[VideoCommentsResponseCheerconfigDataGroupsItem]

class VideoCommentsResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isGlobalMod: Optional[NoneType]
	isSiteAdmin: Optional[NoneType]
	isStaff: Optional[NoneType]

class VideoCommentsResponseCurrentuserData(TypedDict):
	__typename: str
	blockedUsers: List[Any]
	id: str
	roles: VideoCommentsResponseCurrentuserDataRolesData

class VideoCommentsResponseVideoDataOwnerDataBroadcastbadgesItem(TypedDict):
	__typename: str
	clickAction: str
	clickURL: str
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsItemNodesItemTiersItem(TypedDict):
	__typename: str
	bits: int
	canShowInBitsCard: Optional[bool]
	id: str

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsItemNodesItem(TypedDict):
	__typename: str
	campaign: Optional[NoneType]
	id: str
	prefix: str
	tiers: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsItemNodesItemTiersItem]
	type: str

class VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsItem(TypedDict):
	__typename: str
	nodes: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsItemNodesItem]
	templateURL: str

class VideoCommentsResponseVideoDataOwnerDataCheerData(TypedDict):
	__typename: str
	cheerGroups: List[VideoCommentsResponseVideoDataOwnerDataCheerDataCheergroupsItem]
	id: str

class VideoCommentsResponseVideoDataOwnerDataSelfData(TypedDict):
	__typename: str
	isModerator: Optional[bool]

class VideoCommentsResponseVideoDataOwnerData(TypedDict):
	__typename: str
	broadcastBadges: List[VideoCommentsResponseVideoDataOwnerDataBroadcastbadgesItem]
	cheer: VideoCommentsResponseVideoDataOwnerDataCheerData
	id: str
	login: str
	self: VideoCommentsResponseVideoDataOwnerDataSelfData

class VideoCommentsResponseVideoData(TypedDict):
	__typename: str
	broadcastType: str
	id: str
	lengthSeconds: int
	owner: VideoCommentsResponseVideoDataOwnerData

class VideoCommentsResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class VideoCommentsResponse(TypedDict):
	badges: List[VideoCommentsResponseBadgesItem]
	cheerConfig: VideoCommentsResponseCheerconfigData
	__typename: str
	currentUser: VideoCommentsResponseCurrentuserData
	video: VideoCommentsResponseVideoData
	requestInfo: VideoCommentsResponseRequestinfoData

class VideoCommentsByOffsetOrCursorRequest1(TypedDict):
	videoID: str
	contentOffsetSeconds: Optional[int]

class VideoCommentsByOffsetOrCursorRequest2(TypedDict):
	videoID: str
	cursor: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataCommenterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataMessageDataFragmentsItem(TypedDict):
	__typename: str
	emote: Optional[NoneType]
	text: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataMessageDataUserbadgesItem(TypedDict):
	__typename: str
	id: str
	setID: str
	version: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataMessageData(TypedDict):
	__typename: str
	fragments: List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataMessageDataFragmentsItem]
	userBadges: List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataMessageDataUserbadgesItem]
	userColor: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeData(TypedDict):
	__typename: str
	commenter: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataCommenterData
	contentOffsetSeconds: Optional[int]
	createdAt: str
	id: str
	message: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeDataMessageData

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItemNodeData

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]
	hasPreviousPage: Optional[bool]

class VideoCommentsByOffsetOrCursorResponseVideoDataCommentsData(TypedDict):
	__typename: str
	edges: List[VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataEdgesItem]
	pageInfo: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsDataPageinfoData

class VideoCommentsByOffsetOrCursorResponseVideoDataCreatorDataChannelData(TypedDict):
	__typename: str
	id: str

class VideoCommentsByOffsetOrCursorResponseVideoDataCreatorData(TypedDict):
	__typename: str
	channel: VideoCommentsByOffsetOrCursorResponseVideoDataCreatorDataChannelData
	id: str

class VideoCommentsByOffsetOrCursorResponseVideoData(TypedDict):
	__typename: str
	comments: VideoCommentsByOffsetOrCursorResponseVideoDataCommentsData
	creator: VideoCommentsByOffsetOrCursorResponseVideoDataCreatorData
	id: str

class VideoCommentsByOffsetOrCursorResponse(TypedDict):
	video: VideoCommentsByOffsetOrCursorResponseVideoData

class VideoMetadataRequest(TypedDict):
	channelLogin: str
	videoID: str

class VideoMetadataResponseUserDataFollowersData(TypedDict):
	__typename: str
	totalCount: int

class VideoMetadataResponseUserDataLastbroadcastData(TypedDict):
	__typename: str
	id: str
	startedAt: str

class VideoMetadataResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str
	viewersCount: int

class VideoMetadataResponseUserData(TypedDict):
	__typename: str
	followers: VideoMetadataResponseUserDataFollowersData
	id: str
	isPartner: Optional[bool]
	lastBroadcast: VideoMetadataResponseUserDataLastbroadcastData
	primaryColorHex: str
	profileImageURL: str
	stream: VideoMetadataResponseUserDataStreamData

class VideoMetadataResponseCurrentuserData(TypedDict):
	__typename: str
	id: str

class VideoMetadataResponseVideoDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class VideoMetadataResponseVideoDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class VideoMetadataResponseVideoData(TypedDict):
	__typename: str
	broadcastType: str
	createdAt: str
	description: Optional[NoneType]
	game: VideoMetadataResponseVideoDataGameData
	id: str
	lengthSeconds: int
	owner: VideoMetadataResponseVideoDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	title: str
	viewCount: int

class VideoMetadataResponse(TypedDict):
	user: VideoMetadataResponseUserData
	currentUser: VideoMetadataResponseCurrentuserData
	video: VideoMetadataResponseVideoData

class VideoPlayer_VODSeekbarPreviewVideoRequest(TypedDict):
	includePrivate: Optional[bool]
	videoID: str

class VideoPlayer_VODSeekbarPreviewVideoResponseVideoData(TypedDict):
	__typename: str
	id: str
	seekPreviewsURL: str

class VideoPlayer_VODSeekbarPreviewVideoResponse(TypedDict):
	video: VideoPlayer_VODSeekbarPreviewVideoResponseVideoData

class VideoAdRequestDeclineRequestContextDataClientcontextData(TypedDict):
	appVersion: str
	clientApp: str
	isAudioOnly: Optional[bool]
	isMiniTheater: Optional[bool]
	isPIP: Optional[bool]
	isUsingExternalPlayback: Optional[bool]

class VideoAdRequestDeclineRequestContextDataPlayercontextData(TypedDict):
	contentType: str
	isAutoPlay: Optional[bool]
	nauthSig: str
	nauthToken: str
	playerSizeMode: str
	playerType: str

class VideoAdRequestDeclineRequestContextData(TypedDict):
	adFormat: str
	adSessionID: str
	clientContext: VideoAdRequestDeclineRequestContextDataClientcontextData
	commercialID: Optional[str]
	duration: int
	game: str
	isVLM: Optional[bool]
	playerContext: VideoAdRequestDeclineRequestContextDataPlayercontextData
	rollType: str
	twitchCorrelator: str

class VideoAdRequestDeclineRequest(TypedDict):
	context: VideoAdRequestDeclineRequestContextData

class VideoAdRequestDeclineResponseAdcontextDataDeclinestateData(TypedDict):
	__typename: str
	reason: Optional[NoneType]
	shouldDecline: Optional[bool]

class VideoAdRequestDeclineResponseAdcontextData(TypedDict):
	__typename: str
	declineState: VideoAdRequestDeclineResponseAdcontextDataDeclinestateData
	id: str
	radToken: str

class VideoAdRequestDeclineResponse(TypedDict):
	adContext: VideoAdRequestDeclineResponseAdcontextData

class FollowedIndex_CurrentUserRequest(TypedDict):
	...

class FollowedIndex_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	id: str

class FollowedIndex_CurrentUserResponse(TypedDict):
	currentUser: FollowedIndex_CurrentUserResponseCurrentuserData

class FollowedIndex_FollowCountRequest(TypedDict):
	...

class FollowedIndex_FollowCountResponseCurrentuserDataFollowsData(TypedDict):
	__typename: str
	totalCount: int

class FollowedIndex_FollowCountResponseCurrentuserData(TypedDict):
	__typename: str
	follows: FollowedIndex_FollowCountResponseCurrentuserDataFollowsData
	id: str

class FollowedIndex_FollowCountResponse(TypedDict):
	currentUser: FollowedIndex_FollowCountResponseCurrentuserData

class FollowingGames_CurrentUserRequest(TypedDict):
	limit: int
	type: str

class FollowingGames_CurrentUserResponseCurrentuserDataFollowedgamesData(TypedDict):
	__typename: str
	nodes: List[Any]

class FollowingGames_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	followedGames: FollowingGames_CurrentUserResponseCurrentuserDataFollowedgamesData
	id: str

class FollowingGames_CurrentUserResponse(TypedDict):
	currentUser: FollowingGames_CurrentUserResponseCurrentuserData

class FollowingLive_CurrentUserRequest(TypedDict):
	imageWidth: int
	limit: int
	includeIsDJ: Optional[bool]

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterDataChannelDataSelfData(TypedDict):
	__typename: str
	isAuthorized: Optional[bool]

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterDataChannelData(TypedDict):
	__typename: str
	id: str
	self: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterDataChannelDataSelfData

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterData(TypedDict):
	__typename: str
	channel: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterDataChannelData
	id: str
	primaryColorHex: str
	roles: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterDataRolesData

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamData(TypedDict):
	__typename: str
	broadcaster: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataBroadcasterData
	freeformTags: List[FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataFreeformtagsItem]
	game: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamDataGameData
	id: str
	previewImageURL: str
	restriction: Optional[NoneType]
	title: str
	type: str
	viewersCount: int

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str
	stream: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeDataStreamData

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItemNodeData

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersData(TypedDict):
	__typename: str
	edges: List[FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataEdgesItem]
	pageInfo: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersDataPageinfoData

class FollowingLive_CurrentUserResponseCurrentuserDataFollowsData(TypedDict):
	__typename: str
	totalCount: int

class FollowingLive_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	followedLiveUsers: FollowingLive_CurrentUserResponseCurrentuserDataFollowedliveusersData
	follows: FollowingLive_CurrentUserResponseCurrentuserDataFollowsData
	id: str

class FollowingLive_CurrentUserResponse(TypedDict):
	currentUser: FollowingLive_CurrentUserResponseCurrentuserData

class FollowedVideos_CurrentUserRequest(TypedDict):
	includePreviewBlur: Optional[bool]
	limit: int

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataOwnerDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataOwnerDataRolesData

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataSelfDataViewinghistoryData(TypedDict):
	__typename: str
	position: int
	updatedAt: str

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataSelfData(TypedDict):
	__typename: str
	isRestricted: Optional[bool]
	viewingHistory: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataSelfDataViewinghistoryData

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	animatedPreviewURL: str
	contentTags: List[Any]
	game: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataGameData
	id: str
	lengthSeconds: int
	owner: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	resourceRestriction: Optional[NoneType]
	self: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeDataSelfData
	title: str
	viewCount: int

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItemNodeData

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosData(TypedDict):
	__typename: str
	edges: List[FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataEdgesItem]
	pageInfo: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosDataPageinfoData

class FollowedVideos_CurrentUserResponseCurrentuserDataFollowsData(TypedDict):
	__typename: str
	totalCount: int

class FollowedVideos_CurrentUserResponseCurrentuserData(TypedDict):
	__typename: str
	followedVideos: FollowedVideos_CurrentUserResponseCurrentuserDataFollowedvideosData
	follows: FollowedVideos_CurrentUserResponseCurrentuserDataFollowsData
	id: str

class FollowedVideos_CurrentUserResponse(TypedDict):
	currentUser: FollowedVideos_CurrentUserResponseCurrentuserData

class FollowingPage_RecommendedChannelsRequestContextData(TypedDict):
	platform: str

class FollowingPage_RecommendedChannelsRequest(TypedDict):
	imageWidth: int
	context: FollowingPage_RecommendedChannelsRequestContextData
	first: int
	language: Optional[str]
	location: str
	recRequestID: str
	includeIsDJ: Optional[bool]

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataBroadcasterDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	broadcastSettings: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataBroadcasterDataBroadcastsettingsData
	displayName: str
	id: str
	largeProfileImageURL: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataBroadcasterDataRolesData

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataGameDataGametagsItem(TypedDict):
	__typename: str
	id: str
	isLanguageTag: Optional[bool]
	localizedName: str
	tagName: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	categorySlug: str
	displayName: str
	gameTags: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataGameDataGametagsItem]
	id: str
	name: str
	originalReleaseDate: str
	viewersCount: int

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataBroadcasterData
	createdAt: str
	freeformTags: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataFreeformtagsItem]
	game: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataGameData
	id: str
	previewImageURL: str
	previewThumbnailProperties: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	type: str
	viewersCount: int

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItem(TypedDict):
	__typename: str
	node: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItemNodeData
	trackingID: str

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsData(TypedDict):
	__typename: str
	edges: List[FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsDataEdgesItem]

class FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsData(TypedDict):
	__typename: str
	liveRecommendations: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsDataLiverecommendationsData

class FollowingPage_RecommendedChannelsResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	recommendations: FollowingPage_RecommendedChannelsResponseCurrentuserDataRecommendationsData

class FollowingPage_RecommendedChannelsResponse(TypedDict):
	currentUser: FollowingPage_RecommendedChannelsResponseCurrentuserData

class FollowedStreamsContinueWatchingRequest(TypedDict):
	includePreviewBlur: Optional[bool]
	limit: int

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemHistoryData(TypedDict):
	__typename: str
	position: int
	updatedAt: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataOwnerDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataOwnerDataRolesData

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataSelfDataViewinghistoryData(TypedDict):
	__typename: str
	position: int
	updatedAt: str

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataSelfData(TypedDict):
	__typename: str
	isRestricted: Optional[bool]
	viewingHistory: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataSelfDataViewinghistoryData

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	animatedPreviewURL: str
	contentTags: List[Any]
	game: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataGameData
	id: str
	lengthSeconds: int
	owner: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	resourceRestriction: Optional[NoneType]
	self: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeDataSelfData
	title: str
	viewCount: int

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItem(TypedDict):
	__typename: str
	history: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemHistoryData
	node: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItemNodeData

class FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosData(TypedDict):
	__typename: str
	edges: List[FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosDataEdgesItem]

class FollowedStreamsContinueWatchingResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	viewedVideos: FollowedStreamsContinueWatchingResponseCurrentuserDataViewedvideosData

class FollowedStreamsContinueWatchingResponse(TypedDict):
	currentUser: FollowedStreamsContinueWatchingResponseCurrentuserData

class FollowedStreamsRequest(TypedDict):
	userID: str
	limit: int

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelDataOwnerDataSubscriptionproductsItemEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	order: Optional[int]
	subscriptionTier: str
	token: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelDataOwnerDataSubscriptionproductsItem(TypedDict):
	__typename: str
	emotes: List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelDataOwnerDataSubscriptionproductsItemEmotesItem]
	id: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelDataOwnerData(TypedDict):
	__typename: str
	bannerImageURL: str
	displayName: str
	id: str
	isPartner: Optional[bool]
	login: str
	primaryColorHex: str
	profileImageURL: str
	subscriptionProducts: List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelDataOwnerDataSubscriptionproductsItem]

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelData(TypedDict):
	__typename: str
	id: str
	owner: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelDataOwnerData

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeData(TypedDict):
	__typename: str
	baseSegmentID: str
	categories: List[Any]
	channel: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeDataChannelData
	hasReminder: Optional[bool]
	id: str
	repeatEndsAfterCount: Optional[int]
	startAt: str
	title: str

class FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItem(TypedDict):
	__typename: str
	node: FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItemNodeData

class FollowedStreamsResponseFollowedupcomingstreamsData(TypedDict):
	__typename: str
	edges: List[FollowedStreamsResponseFollowedupcomingstreamsDataEdgesItem]

class FollowedStreamsResponse(TypedDict):
	followedUpcomingStreams: FollowedStreamsResponseFollowedupcomingstreamsData

class BrowsePage_AllDirectoriesRequest1OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class BrowsePage_AllDirectoriesRequest1OptionsData(TypedDict):
	recommendationsContext: BrowsePage_AllDirectoriesRequest1OptionsDataRecommendationscontextData
	requestID: str
	sort: str
	tags: List[Any]

class BrowsePage_AllDirectoriesRequest1(TypedDict):
	limit: int
	options: BrowsePage_AllDirectoriesRequest1OptionsData

class BrowsePage_AllDirectoriesRequest2OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class BrowsePage_AllDirectoriesRequest2OptionsData(TypedDict):
	recommendationsContext: BrowsePage_AllDirectoriesRequest2OptionsDataRecommendationscontextData
	requestID: str
	sort: str
	tags: List[Any]

class BrowsePage_AllDirectoriesRequest2(TypedDict):
	limit: int
	options: BrowsePage_AllDirectoriesRequest2OptionsData
	cursor: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesItemNodeDataTagsItem(TypedDict):
	__typename: str
	id: str
	isLanguageTag: Optional[bool]
	localizedName: str
	tagName: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesItemNodeData(TypedDict):
	__typename: str
	avatarURL: str
	displayName: str
	id: str
	name: str
	originalReleaseDate: Optional[NoneType]
	slug: str
	tags: List[BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesItemNodeDataTagsItem]
	viewersCount: int

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesItemNodeData
	trackingID: str

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class BrowsePage_AllDirectoriesResponseDirectorieswithtagsData(TypedDict):
	__typename: str
	edges: List[BrowsePage_AllDirectoriesResponseDirectorieswithtagsDataEdgesItem]
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
	includeIsDJ: Optional[bool]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentDataEdgesItemNodeDataGametagsItem(TypedDict):
	__typename: str
	id: str
	isLanguageTag: Optional[bool]
	localizedName: str
	tagName: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentDataEdgesItemNodeData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	gameTags: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentDataEdgesItemNodeDataGametagsItem]
	id: str
	name: str
	originalReleaseDate: str
	slug: str
	viewersCount: int

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[str]
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentDataEdgesItemNodeData
	trackingID: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentData(TypedDict):
	__typename: str
	edges: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentDataEdgesItem]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemSubtitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	location: str
	text: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemSubtitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemSubtitleDataLocalizedtitletokensItemNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemSubtitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemSubtitleDataLocalizedtitletokensItem]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemTitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	location: str
	text: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemTitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemTitleDataLocalizedtitletokensItemNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemTitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemTitleDataLocalizedtitletokensItem]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItem(TypedDict):
	__typename: str
	content: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemContentData
	id: str
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemSubtitleData
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItemTitleData
	type: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemSubtitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	location: str
	text: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemSubtitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemSubtitleDataLocalizedtitletokensItemNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemSubtitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemSubtitleDataLocalizedtitletokensItem]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemTitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	location: str
	text: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemTitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemTitleDataLocalizedtitletokensItemNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemTitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemTitleDataLocalizedtitletokensItem]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItem(TypedDict):
	__typename: str
	id: str
	shelves: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemShelvesItem]
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemSubtitleData
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItemTitleData
	trackingID: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	location: str
	text: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensItemNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleDataLocalizedtitletokensItem]

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensItemNodeData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	location: str
	text: str

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensItem(TypedDict):
	__typename: str
	node: BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensItemNodeData

class BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str
	key: str
	localizedTitleTokens: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleDataLocalizedtitletokensItem]

class BrowseVerticalDirectoryResponseVerticaldirectoryData(TypedDict):
	__typename: str
	id: str
	shelfGroups: List[BrowseVerticalDirectoryResponseVerticaldirectoryDataShelfgroupsItem]
	subtitle: BrowseVerticalDirectoryResponseVerticaldirectoryDataSubtitleData
	title: BrowseVerticalDirectoryResponseVerticaldirectoryDataTitleData
	trackingID: Optional[str]

class BrowseVerticalDirectoryResponse(TypedDict):
	verticalDirectory: BrowseVerticalDirectoryResponseVerticaldirectoryData

class DirectoryCollection_BrowsableCollectionRequest1OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class DirectoryCollection_BrowsableCollectionRequest1OptionsData(TypedDict):
	recommendationsContext: DirectoryCollection_BrowsableCollectionRequest1OptionsDataRecommendationscontextData
	requestID: str

class DirectoryCollection_BrowsableCollectionRequest1(TypedDict):
	limit: int
	imageWidth: int
	slug: str
	options: DirectoryCollection_BrowsableCollectionRequest1OptionsData
	includeIsDJ: Optional[bool]

class DirectoryCollection_BrowsableCollectionRequest2OptionsDataRecommendationscontextData(TypedDict):
	platform: str

class DirectoryCollection_BrowsableCollectionRequest2OptionsData(TypedDict):
	recommendationsContext: DirectoryCollection_BrowsableCollectionRequest2OptionsDataRecommendationscontextData
	requestID: str

class DirectoryCollection_BrowsableCollectionRequest2(TypedDict):
	limit: int
	imageWidth: int
	slug: str
	options: DirectoryCollection_BrowsableCollectionRequest2OptionsData
	includeIsDJ: Optional[bool]
	cursor: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataDescriptionData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: Optional[NoneType]

class DirectoryCollection_BrowsableCollectionResponseCollectionDataNameData(TypedDict):
	__typename: str
	fallbackLocalizedTitle: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataBroadcasterDataRolesData

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataBroadcasterData
	freeformTags: List[DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataFreeformtagsItem]
	game: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataGameData
	id: str
	previewImageURL: str
	previewThumbnailProperties: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	title: str
	type: str
	viewersCount: int

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItemNodeData
	trackingID: str

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsData(TypedDict):
	__typename: str
	edges: List[DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataEdgesItem]
	pageInfo: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsDataPageinfoData

class DirectoryCollection_BrowsableCollectionResponseCollectionData(TypedDict):
	__typename: str
	description: DirectoryCollection_BrowsableCollectionResponseCollectionDataDescriptionData
	id: str
	name: DirectoryCollection_BrowsableCollectionResponseCollectionDataNameData
	slug: str
	streams: DirectoryCollection_BrowsableCollectionResponseCollectionDataStreamsData

class DirectoryCollection_BrowsableCollectionResponse(TypedDict):
	collection: DirectoryCollection_BrowsableCollectionResponseCollectionData

class HomeShelfEditorRequest(TypedDict):
	channelLogin: str

class HomeShelfEditorResponseUserDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class HomeShelfEditorResponseUserData(TypedDict):
	__typename: str
	id: str
	self: HomeShelfEditorResponseUserDataSelfData

class HomeShelfEditorResponse(TypedDict):
	user: HomeShelfEditorResponseUserData

class HomeShelfUsersRequest(TypedDict):
	channelLogin: str

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesItemNodeData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	stream: Optional[NoneType]

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesItem(TypedDict):
	__typename: str
	node: HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesItemNodeData
	trackingID: str

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfData(TypedDict):
	__typename: str
	edges: List[HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfDataEdgesItem]
	type: str

class HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesData(TypedDict):
	__typename: str
	streamerShelf: HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesDataStreamershelfData

class HomeShelfUsersResponseUserDataChannelDataHomeData(TypedDict):
	__typename: str
	shelves: HomeShelfUsersResponseUserDataChannelDataHomeDataShelvesData

class HomeShelfUsersResponseUserDataChannelData(TypedDict):
	__typename: str
	home: HomeShelfUsersResponseUserDataChannelDataHomeData
	id: str

class HomeShelfUsersResponseUserDataPrimaryteamData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str

class HomeShelfUsersResponseUserData(TypedDict):
	__typename: str
	channel: HomeShelfUsersResponseUserDataChannelData
	displayName: str
	id: str
	login: str
	primaryTeam: HomeShelfUsersResponseUserDataPrimaryteamData

class HomeShelfUsersResponse(TypedDict):
	user: HomeShelfUsersResponseUserData

class HomeShelfVideosRequest(TypedDict):
	channelLogin: str
	first: int

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterDataRolesData

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemClipgameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemCuratorData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemGueststarparticipantsDataHostData(TypedDict):
	__typename: str
	description: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemGueststarparticipantsData(TypedDict):
	__typename: str
	guests: List[Any]
	host: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemGueststarparticipantsDataHostData
	sessionIdentifier: Optional[str]

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItem(TypedDict):
	__typename: str
	broadcaster: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemBroadcasterData
	clipGame: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemClipgameData
	clipTitle: str
	clipViewCount: int
	createdAt: str
	curator: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemCuratorData
	durationSeconds: int
	guestStarParticipants: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItemGueststarparticipantsData
	id: str
	isFeatured: Optional[bool]
	slug: str
	thumbnailURL: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeData(TypedDict):
	__typename: str
	description: Optional[NoneType]
	id: str
	items: List[HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeDataItemsItem]
	title: str
	type: str

class HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItem(TypedDict):
	__typename: str
	node: HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItemNodeData

class HomeShelfVideosResponseUserDataVideoshelvesData(TypedDict):
	__typename: str
	edges: List[HomeShelfVideosResponseUserDataVideoshelvesDataEdgesItem]

class HomeShelfVideosResponseUserData(TypedDict):
	__typename: str
	id: str
	videoShelves: HomeShelfVideosResponseUserDataVideoshelvesData

class HomeShelfVideosResponse(TypedDict):
	user: HomeShelfVideosResponseUserData

class HomeShelfGamesRequest(TypedDict):
	channelLogin: str

class HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfData(TypedDict):
	__typename: str
	edges: List[Any]

class HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesData(TypedDict):
	__typename: str
	categoryShelf: HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesDataCategoryshelfData

class HomeShelfGamesResponseUserDataChannelDataHomeData(TypedDict):
	__typename: str
	shelves: HomeShelfGamesResponseUserDataChannelDataHomeDataShelvesData

class HomeShelfGamesResponseUserDataChannelData(TypedDict):
	__typename: str
	home: HomeShelfGamesResponseUserDataChannelDataHomeData
	id: str

class HomeShelfGamesResponseUserData(TypedDict):
	__typename: str
	channel: HomeShelfGamesResponseUserDataChannelData
	id: str
	primaryColorHex: str

class HomeShelfGamesResponse(TypedDict):
	user: HomeShelfGamesResponseUserData

class OfflineBannerOverlayRequest(TypedDict):
	login: str

class OfflineBannerOverlayResponseUserData(TypedDict):
	__typename: str
	id: str
	offlineImageURL: str

class OfflineBannerOverlayResponse(TypedDict):
	user: OfflineBannerOverlayResponseUserData

class VideoPlayerOfflineRecommendationsOverlayRequest(TypedDict):
	login: str

class VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosData(TypedDict):
	__typename: str
	edges: List[Any]

class VideoPlayerOfflineRecommendationsOverlayResponseUserData(TypedDict):
	__typename: str
	id: str
	videos: VideoPlayerOfflineRecommendationsOverlayResponseUserDataVideosData

class VideoPlayerOfflineRecommendationsOverlayResponse(TypedDict):
	user: VideoPlayerOfflineRecommendationsOverlayResponseUserData

class ChannelClipCoreRequest(TypedDict):
	clipSlug: str

class ChannelClipCoreResponseClipDataBroadcasterDataChannelDataSelfData(TypedDict):
	__typename: str
	isAuthorized: Optional[bool]
	restrictionType: Optional[NoneType]

class ChannelClipCoreResponseClipDataBroadcasterDataChannelDataTrailerData(TypedDict):
	__typename: str
	video: Optional[NoneType]

class ChannelClipCoreResponseClipDataBroadcasterDataChannelData(TypedDict):
	__typename: str
	id: str
	self: ChannelClipCoreResponseClipDataBroadcasterDataChannelDataSelfData
	trailer: ChannelClipCoreResponseClipDataBroadcasterDataChannelDataTrailerData

class ChannelClipCoreResponseClipDataBroadcasterData(TypedDict):
	__typename: str
	channel: ChannelClipCoreResponseClipDataBroadcasterDataChannelData
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	stream: Optional[NoneType]

class ChannelClipCoreResponseClipDataGueststarparticipantsData(TypedDict):
	__typename: str
	guests: List[Any]
	sessionIdentifier: Optional[str]

class ChannelClipCoreResponseClipData(TypedDict):
	__typename: str
	broadcaster: ChannelClipCoreResponseClipDataBroadcasterData
	guestStarParticipants: ChannelClipCoreResponseClipDataGueststarparticipantsData
	id: str
	isFeatured: Optional[bool]
	videoOffsetSeconds: Optional[NoneType]

class ChannelClipCoreResponse(TypedDict):
	clip: ChannelClipCoreResponseClipData

class VideoAccessToken_ClipRequest(TypedDict):
	platform: str
	slug: str

class VideoAccessToken_ClipResponseClipDataPlaybackaccesstokenData(TypedDict):
	__typename: str
	signature: str
	value: str

class VideoAccessToken_ClipResponseClipDataVideoqualitiesItem(TypedDict):
	__typename: str
	frameRate: int
	quality: str
	sourceURL: str

class VideoAccessToken_ClipResponseClipData(TypedDict):
	__typename: str
	id: str
	playbackAccessToken: VideoAccessToken_ClipResponseClipDataPlaybackaccesstokenData
	videoQualities: List[VideoAccessToken_ClipResponseClipDataVideoqualitiesItem]

class VideoAccessToken_ClipResponse(TypedDict):
	clip: VideoAccessToken_ClipResponseClipData

class ClipMetadataRequest(TypedDict):
	clipSlug: str

class ClipMetadataResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isSiteAdmin: Optional[NoneType]
	isStaff: Optional[NoneType]

class ClipMetadataResponseCurrentuserDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class ClipMetadataResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str
	roles: ClipMetadataResponseCurrentuserDataRolesData
	self: ClipMetadataResponseCurrentuserDataSelfData

class ClipMetadataResponseClipDataGueststarparticipantsData(TypedDict):
	__typename: str
	guests: List[Any]
	sessionIdentifier: Optional[str]

class ClipMetadataResponseClipData(TypedDict):
	__typename: str
	guestStarParticipants: ClipMetadataResponseClipDataGueststarparticipantsData
	id: str

class ClipMetadataResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class ClipMetadataResponse(TypedDict):
	currentUser: ClipMetadataResponseCurrentuserData
	clip: ClipMetadataResponseClipData
	requestInfo: ClipMetadataResponseRequestinfoData

class ShareClipRenderStatusRequest(TypedDict):
	slug: str

class ShareClipRenderStatusResponseClipDataAssetsItemCuratorData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str

class ShareClipRenderStatusResponseClipDataAssetsItemVideoqualitiesItem(TypedDict):
	__typename: str
	frameRate: int
	quality: str
	sourceURL: str

class ShareClipRenderStatusResponseClipDataAssetsItem(TypedDict):
	__typename: str
	aspectRatio: float
	createdAt: str
	creationState: str
	curator: ShareClipRenderStatusResponseClipDataAssetsItemCuratorData
	id: str
	portraitMetadata: Optional[NoneType]
	thumbnailURL: str
	type: str
	videoQualities: List[ShareClipRenderStatusResponseClipDataAssetsItemVideoqualitiesItem]

class ShareClipRenderStatusResponseClipDataBroadcastData(TypedDict):
	__typename: str
	id: str
	title: Optional[NoneType]

class ShareClipRenderStatusResponseClipDataBroadcasterDataFollowersData(TypedDict):
	__typename: str
	totalCount: int

class ShareClipRenderStatusResponseClipDataBroadcasterDataLastbroadcastData(TypedDict):
	__typename: str
	id: str
	startedAt: str

class ShareClipRenderStatusResponseClipDataBroadcasterDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class ShareClipRenderStatusResponseClipDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	followers: ShareClipRenderStatusResponseClipDataBroadcasterDataFollowersData
	id: str
	isPartner: Optional[bool]
	lastBroadcast: ShareClipRenderStatusResponseClipDataBroadcasterDataLastbroadcastData
	login: str
	primaryColorHex: str
	profileImageURL: str
	self: ShareClipRenderStatusResponseClipDataBroadcasterDataSelfData
	stream: Optional[NoneType]

class ShareClipRenderStatusResponseClipDataCuratorData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str

class ShareClipRenderStatusResponseClipDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class ShareClipRenderStatusResponseClipDataPlaybackaccesstokenData(TypedDict):
	__typename: str
	signature: str
	value: str

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData(TypedDict):
	__typename: str
	xPercentage: float
	yPercentage: int

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData(TypedDict):
	__typename: str
	xPercentage: float
	yPercentage: Optional[int]

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData(TypedDict):
	__typename: str
	bottomRight: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData
	topLeft: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData

class ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataData(TypedDict):
	__typename: str
	mainFrame: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData

class ShareClipRenderStatusResponseClipDataSuggestedcroppingData(TypedDict):
	__typename: str
	fullTemplateMetadata: ShareClipRenderStatusResponseClipDataSuggestedcroppingDataFulltemplatemetadataData
	portraitClipLayout: str
	stackedTemplateMetadata: Optional[NoneType]

class ShareClipRenderStatusResponseClipDataVideoqualitiesItem(TypedDict):
	__typename: str
	sourceURL: str

class ShareClipRenderStatusResponseClipData(TypedDict):
	__typename: str
	assets: List[ShareClipRenderStatusResponseClipDataAssetsItem]
	broadcast: ShareClipRenderStatusResponseClipDataBroadcastData
	broadcaster: ShareClipRenderStatusResponseClipDataBroadcasterData
	champBadge: Optional[NoneType]
	createdAt: str
	curator: ShareClipRenderStatusResponseClipDataCuratorData
	durationSeconds: int
	embedURL: str
	game: ShareClipRenderStatusResponseClipDataGameData
	id: str
	isFeatured: Optional[bool]
	isPublished: Optional[bool]
	isViewerEditRestricted: Optional[bool]
	language: str
	playbackAccessToken: ShareClipRenderStatusResponseClipDataPlaybackaccesstokenData
	slug: str
	suggestedCropping: ShareClipRenderStatusResponseClipDataSuggestedcroppingData
	thumbnailURL: str
	title: str
	url: str
	video: Optional[NoneType]
	videoOffsetSeconds: Optional[NoneType]
	videoQualities: List[ShareClipRenderStatusResponseClipDataVideoqualitiesItem]
	viewCount: int

class ShareClipRenderStatusResponse(TypedDict):
	clip: ShareClipRenderStatusResponseClipData

class ChatClipRequest(TypedDict):
	clipSlug: str

class ChatClipResponseClipData(TypedDict):
	__typename: str
	durationSeconds: int
	id: str
	video: Optional[NoneType]
	videoOffsetSeconds: Optional[NoneType]

class ChatClipResponse(TypedDict):
	clip: ChatClipResponseClipData

class CanViewersExportQueryRequest(TypedDict):
	channelLogin: str

class CanViewersExportQueryResponseUserDataChannelDataClipssettingsData(TypedDict):
	__typename: str
	isClipsCreationEnabled: Optional[bool]
	isViewerExportsEnabled: Optional[bool]

class CanViewersExportQueryResponseUserDataChannelData(TypedDict):
	__typename: str
	clipsSettings: CanViewersExportQueryResponseUserDataChannelDataClipssettingsData
	id: str

class CanViewersExportQueryResponseUserData(TypedDict):
	__typename: str
	channel: CanViewersExportQueryResponseUserDataChannelData
	id: str

class CanViewersExportQueryResponse(TypedDict):
	user: CanViewersExportQueryResponseUserData

class AccessGetFeatureClipRestrictionsQueryRequest(TypedDict):
	channelLogin: str

class AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsData(TypedDict):
	__typename: str
	featuringRestrictedTo: Optional[NoneType]

class AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelData(TypedDict):
	__typename: str
	clipsSettings: AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelDataClipssettingsData
	id: str

class AccessGetFeatureClipRestrictionsQueryResponseUserData(TypedDict):
	__typename: str
	channel: AccessGetFeatureClipRestrictionsQueryResponseUserDataChannelData
	id: str

class AccessGetFeatureClipRestrictionsQueryResponse(TypedDict):
	user: AccessGetFeatureClipRestrictionsQueryResponseUserData

class incrementClipViewCountRequestInputData(TypedDict):
	slug: str

class incrementClipViewCountRequest(TypedDict):
	input: incrementClipViewCountRequestInputData

class incrementClipViewCountResponseUpdateclipviewcountDataClipData(TypedDict):
	__typename: str
	id: str

class incrementClipViewCountResponseUpdateclipviewcountData(TypedDict):
	__typename: str
	clip: incrementClipViewCountResponseUpdateclipviewcountDataClipData

class incrementClipViewCountResponse(TypedDict):
	updateClipViewCount: incrementClipViewCountResponseUpdateclipviewcountData

class HappeningNowSettingsRequest(TypedDict):
	...

class HappeningNowSettingsResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	isChatHappeningNowEnabled: Optional[bool]

class HappeningNowSettingsResponse(TypedDict):
	currentUser: HappeningNowSettingsResponseCurrentuserData

class ClaimCommunityPointsRequestInputData(TypedDict):
	channelID: str
	claimID: str

class ClaimCommunityPointsRequest(TypedDict):
	input: ClaimCommunityPointsRequestInputData

class ClaimCommunityPointsResponseClaimcommunitypointsDataClaimData(TypedDict):
	__typename: str
	id: str
	multipliers: List[Any]
	pointsEarnedBaseline: int
	pointsEarnedTotal: int

class ClaimCommunityPointsResponseClaimcommunitypointsData(TypedDict):
	__typename: str
	claim: ClaimCommunityPointsResponseClaimcommunitypointsDataClaimData
	currentPoints: int
	error: Optional[NoneType]

class ClaimCommunityPointsResponse(TypedDict):
	claimCommunityPoints: ClaimCommunityPointsResponseClaimcommunitypointsData

class RewardCenter_BitsBalanceRequest(TypedDict):
	...

class RewardCenter_BitsBalanceResponseCurrentuserData(TypedDict):
	__typename: str
	bitsBalance: Optional[int]
	id: str

class RewardCenter_BitsBalanceResponse(TypedDict):
	currentUser: RewardCenter_BitsBalanceResponseCurrentuserData

class SupportPanelCheckoutServiceRequest(TypedDict):
	giftRecipientLogin: Optional[str]
	withStandardGifting: Optional[bool]
	login: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	setID: str
	token: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData
	previewPrice: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData(TypedDict):
	__typename: str
	internal: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData(TypedDict):
	__typename: str
	chargeModel: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData(TypedDict):
	__typename: str
	eligibility: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData
	giftType: str
	id: str
	listing: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataQuantityData
	tagBindings: List[SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataTagbindingsItem]
	tplr: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem(TypedDict):
	__typename: str
	offer: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingData(TypedDict):
	__typename: str
	community: List[SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem]

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemIntervalData(TypedDict):
	__typename: str
	unit: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPlanData
	previewPrice: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelData(TypedDict):
	__typename: str
	internal: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelDataInternalData

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingData(TypedDict):
	__typename: str
	chargeModel: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingDataChargemodelData

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItem(TypedDict):
	__typename: str
	eligibility: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemEligibilityData
	giftType: Optional[NoneType]
	id: str
	listing: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemQuantityData
	tagBindings: List[SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItemTagbindingsItem]
	tplr: str

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemSelfData(TypedDict):
	__typename: str
	canGiftInChannel: Optional[bool]

class SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	displayName: str
	emoteModifiers: List[Any]
	emoteSetID: str
	emotes: List[SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemEmotesItem]
	gifting: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemGiftingData
	hasAdFree: Optional[bool]
	id: str
	interval: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemIntervalData
	name: str
	offers: List[SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemOffersItem]
	price: str
	self: SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItemSelfData
	tier: str
	type: str
	url: str

class SupportPanelCheckoutServiceResponseUserData(TypedDict):
	__typename: str
	id: str
	subscriptionProducts: List[SupportPanelCheckoutServiceResponseUserDataSubscriptionproductsItem]

class SupportPanelCheckoutServiceResponse(TypedDict):
	user: SupportPanelCheckoutServiceResponseUserData

class SupportPanelTrackingServiceRequest(TypedDict):
	login: str
	CSBTrackingFlagEnabled: Optional[bool]

class SupportPanelTrackingServiceResponseUserDataChannelDataGoalsData(TypedDict):
	__typename: str
	edges: List[Any]

class SupportPanelTrackingServiceResponseUserDataChannelData(TypedDict):
	__typename: str
	customSubBenefits: List[Any]
	founderBadgeAvailability: Optional[int]
	goals: SupportPanelTrackingServiceResponseUserDataChannelDataGoalsData
	id: str

class SupportPanelTrackingServiceResponseUserDataSelfDataCumulativetenureData(TypedDict):
	__typename: str
	daysRemaining: Optional[int]
	months: Optional[int]

class SupportPanelTrackingServiceResponseUserDataSelfDataStreaktenureData(TypedDict):
	__typename: str
	daysRemaining: Optional[int]
	months: Optional[int]

class SupportPanelTrackingServiceResponseUserDataSelfData(TypedDict):
	__typename: str
	canPrimeSubscribe: Optional[bool]
	cumulativeTenure: SupportPanelTrackingServiceResponseUserDataSelfDataCumulativetenureData
	isFounder: Optional[bool]
	streakTenure: SupportPanelTrackingServiceResponseUserDataSelfDataStreaktenureData
	subscriptionBenefit: Optional[NoneType]

class SupportPanelTrackingServiceResponseUserData(TypedDict):
	__typename: str
	channel: SupportPanelTrackingServiceResponseUserDataChannelData
	id: str
	self: SupportPanelTrackingServiceResponseUserDataSelfData

class SupportPanelTrackingServiceResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class SupportPanelTrackingServiceResponse(TypedDict):
	user: SupportPanelTrackingServiceResponseUserData
	requestInfo: SupportPanelTrackingServiceResponseRequestinfoData

class GiftSubscriptionRewardPreviewsRequest(TypedDict):
	channelID: str
	quantity: int
	tier: int
	isAnonymous: Optional[bool]

class GiftSubscriptionRewardPreviewsResponse(TypedDict):
	rewardCampaignGiftPreviews: List[Any]

class SupportPanelCommunityGifting_GiftingOptionsRequest(TypedDict):
	giftRecipientLogin: Optional[str]
	withStandardGifting: Optional[bool]
	withCheckoutPrice: Optional[bool]
	login: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	setID: str
	token: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData
	previewPrice: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelData(TypedDict):
	__typename: str
	internal: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingData(TypedDict):
	__typename: str
	chargeModel: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelData

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferData(TypedDict):
	__typename: str
	eligibility: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataEligibilityData
	giftType: str
	id: str
	listing: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataQuantityData
	tagBindings: List[SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataTagbindingsItem]
	tplr: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItem(TypedDict):
	__typename: str
	offer: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferData

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingData(TypedDict):
	__typename: str
	community: List[SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItem]

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemIntervalData(TypedDict):
	__typename: str
	unit: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanData
	previewPrice: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelData(TypedDict):
	__typename: str
	internal: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalData

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingData(TypedDict):
	__typename: str
	chargeModel: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelData

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItem(TypedDict):
	__typename: str
	eligibility: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemEligibilityData
	giftType: Optional[NoneType]
	id: str
	listing: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemQuantityData
	tagBindings: List[SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemTagbindingsItem]
	tplr: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemSelfData(TypedDict):
	__typename: str
	canGiftInChannel: Optional[bool]

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItem(TypedDict):
	__typename: str
	displayName: str
	emoteModifiers: List[Any]
	emoteSetID: str
	emotes: List[SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemEmotesItem]
	gifting: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingData
	hasAdFree: Optional[bool]
	id: str
	interval: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemIntervalData
	name: str
	offers: List[SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItem]
	price: str
	self: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemSelfData
	tier: str
	type: str
	url: str

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultData(TypedDict):
	__typename: str
	nodes: List[SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItem]

class SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginData(TypedDict):
	__typename: str
	id: str
	subscriptionProductsResult: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginDataSubscriptionproductsresultData

class SupportPanelCommunityGifting_GiftingOptionsResponse(TypedDict):
	userResultByLogin: SupportPanelCommunityGifting_GiftingOptionsResponseUserresultbyloginData

class SupportPanelSubTokenBalanceRequest(TypedDict):
	...

class SupportPanelSubTokenBalanceResponseCurrentuserDataSubscriptiontokenData(TypedDict):
	__typename: str
	balance: Optional[int]

class SupportPanelSubTokenBalanceResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	subscriptionToken: SupportPanelSubTokenBalanceResponseCurrentuserDataSubscriptiontokenData

class SupportPanelSubTokenBalanceResponse(TypedDict):
	currentUser: SupportPanelSubTokenBalanceResponseCurrentuserData

class OneClickEligibilityRequest(TypedDict):
	walletType: str

class OneClickEligibilityResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class OneClickEligibilityResponseCurrentuserDataPaymentmethodsItem(TypedDict):
	__typename: str
	billingCountry: Optional[NoneType]
	billingEmail: Optional[NoneType]
	billingUsername: Optional[NoneType]
	cardType: Optional[NoneType]
	chargeInstrumentID: Optional[str]
	expirationMonth: Optional[NoneType]
	expirationYear: Optional[NoneType]
	lastFour: Optional[NoneType]
	paymentScheme: Optional[NoneType]
	paymentType: str
	provider: str

class OneClickEligibilityResponseCurrentuserDataWalletbalancesDataAllbalancesItem(TypedDict):
	__typename: str
	amount: Optional[int]
	currency: str
	expiresAt: Optional[NoneType]
	exponent: int

class OneClickEligibilityResponseCurrentuserDataWalletbalancesData(TypedDict):
	__typename: str
	allBalances: List[OneClickEligibilityResponseCurrentuserDataWalletbalancesDataAllbalancesItem]

class OneClickEligibilityResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	paymentMethods: List[OneClickEligibilityResponseCurrentuserDataPaymentmethodsItem]
	residence: Optional[NoneType]
	walletBalances: OneClickEligibilityResponseCurrentuserDataWalletbalancesData

class OneClickEligibilityResponseRecurlyconfigsDataPaywithamazonconfigsData(TypedDict):
	__typename: str
	clientID: str
	isProduction: Optional[bool]
	sellerID: str

class OneClickEligibilityResponseRecurlyconfigsData(TypedDict):
	__typename: str
	braintreeClientAuthorization: str
	payWithAmazonConfigs: OneClickEligibilityResponseRecurlyconfigsDataPaywithamazonconfigsData
	publicKey: str

class OneClickEligibilityResponse(TypedDict):
	requestInfo: OneClickEligibilityResponseRequestinfoData
	currentUser: OneClickEligibilityResponseCurrentuserData
	recurlyConfigs: OneClickEligibilityResponseRecurlyconfigsData

class SupportPanelSubTokenOffersRequest(TypedDict):
	id: str
	withSingleGifting: Optional[bool]
	withCommunityGifting: Optional[bool]
	withRecurringSubscriptions: Optional[bool]

class SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData(TypedDict):
	__typename: str
	isEligible: Optional[bool]

class SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData(TypedDict):
	__typename: str
	credit: Optional[NoneType]

class SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData(TypedDict):
	__typename: str
	chargeModel: SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingDataChargemodelData

class SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData(TypedDict):
	__typename: str
	eligibility: SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataEligibilityData
	id: str
	listing: SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferDataListingData

class SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem(TypedDict):
	__typename: str
	offer: SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItemOfferData

class SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingData(TypedDict):
	__typename: str
	community: List[SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingDataCommunityItem]

class SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	gifting: SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItemGiftingData
	id: str
	tier: str

class SupportPanelSubTokenOffersResponseUserData(TypedDict):
	__typename: str
	id: str
	subscriptionProducts: List[SupportPanelSubTokenOffersResponseUserDataSubscriptionproductsItem]

class SupportPanelSubTokenOffersResponse(TypedDict):
	user: SupportPanelSubTokenOffersResponseUserData

class SupportPanelCommunityGifting_GifterBadgeProgressRequest(TypedDict):
	login: str

class SupportPanelCommunityGifting_GifterBadgeProgressResponseUserDataSelfData(TypedDict):
	__typename: str
	subscriptionGiftCount: Optional[int]

class SupportPanelCommunityGifting_GifterBadgeProgressResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	self: SupportPanelCommunityGifting_GifterBadgeProgressResponseUserDataSelfData

class SupportPanelCommunityGifting_GifterBadgeProgressResponseBadgesItem(TypedDict):
	__typename: str
	clickAction: str
	clickURL: str
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class SupportPanelCommunityGifting_GifterBadgeProgressResponseCurrentuserDataSubscriptionsettingsData(TypedDict):
	__typename: str
	isGiftCountHidden: Optional[bool]

class SupportPanelCommunityGifting_GifterBadgeProgressResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	subscriptionSettings: SupportPanelCommunityGifting_GifterBadgeProgressResponseCurrentuserDataSubscriptionsettingsData

class SupportPanelCommunityGifting_GifterBadgeProgressResponse(TypedDict):
	user: SupportPanelCommunityGifting_GifterBadgeProgressResponseUserData
	badges: List[SupportPanelCommunityGifting_GifterBadgeProgressResponseBadgesItem]
	currentUser: SupportPanelCommunityGifting_GifterBadgeProgressResponseCurrentuserData

class FollowButton_UnfollowUserRequestInputData(TypedDict):
	targetID: str

class FollowButton_UnfollowUserRequest(TypedDict):
	input: FollowButton_UnfollowUserRequestInputData

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: Optional[NoneType]

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	self: FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserDataSelfData

class FollowButton_UnfollowUserResponseUnfollowuserDataFollowData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]
	user: FollowButton_UnfollowUserResponseUnfollowuserDataFollowDataUserData

class FollowButton_UnfollowUserResponseUnfollowuserData(TypedDict):
	__typename: str
	follow: FollowButton_UnfollowUserResponseUnfollowuserDataFollowData

class FollowButton_UnfollowUserResponse(TypedDict):
	unfollowUser: FollowButton_UnfollowUserResponseUnfollowuserData

class FollowButton_FollowUserRequestInputData(TypedDict):
	disableNotifications: Optional[bool]
	targetID: str

class FollowButton_FollowUserRequest(TypedDict):
	input: FollowButton_FollowUserRequestInputData

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfDataFollowerData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]
	followedAt: str

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfDataFollowerData

class FollowButton_FollowUserResponseFollowuserDataFollowDataUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	self: FollowButton_FollowUserResponseFollowuserDataFollowDataUserDataSelfData

class FollowButton_FollowUserResponseFollowuserDataFollowData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]
	user: FollowButton_FollowUserResponseFollowuserDataFollowDataUserData

class FollowButton_FollowUserResponseFollowuserData(TypedDict):
	__typename: str
	error: Optional[NoneType]
	follow: FollowButton_FollowUserResponseFollowuserDataFollowData

class FollowButton_FollowUserResponse(TypedDict):
	followUser: FollowButton_FollowUserResponseFollowuserData

class SupportPanelTitleSectionAvatarRequest(TypedDict):
	avatarSize: int
	login: str

class SupportPanelTitleSectionAvatarResponseUserData(TypedDict):
	__typename: str
	id: str
	primaryColorHex: str
	profileImageURL: str
	stream: Optional[NoneType]

class SupportPanelTitleSectionAvatarResponse(TypedDict):
	user: SupportPanelTitleSectionAvatarResponseUserData

class SubscriptionRewardPreviewsRequest(TypedDict):
	channelID: str
	months: int
	tier: int

class SubscriptionRewardPreviewsResponse(TypedDict):
	rewardCampaignSubPreviews: List[Any]

class SupportPanelSubscribeViewFooterPrimeRequest(TypedDict):
	giftRecipientLogin: Optional[str]
	withStandardGifting: Optional[bool]
	withCheckoutPrice: Optional[bool]
	login: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemEmotesItem(TypedDict):
	__typename: str
	assetType: str
	id: str
	setID: str
	token: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPlanData
	previewPrice: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalDataPreviewpriceData

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelData(TypedDict):
	__typename: str
	internal: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelDataInternalData

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingData(TypedDict):
	__typename: str
	chargeModel: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingDataChargemodelData

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferData(TypedDict):
	__typename: str
	eligibility: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataEligibilityData
	giftType: str
	id: str
	listing: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataQuantityData
	tagBindings: List[SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferDataTagbindingsItem]
	tplr: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItem(TypedDict):
	__typename: str
	offer: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItemOfferData

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingData(TypedDict):
	__typename: str
	community: List[SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingDataCommunityItem]

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemIntervalData(TypedDict):
	__typename: str
	unit: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData(TypedDict):
	__typename: str
	duration: int
	unit: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanData(TypedDict):
	__typename: str
	interval: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanDataIntervalData
	renewalPolicy: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	price: int
	total: int

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	plan: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPlanData
	previewPrice: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalDataPreviewpriceData

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelData(TypedDict):
	__typename: str
	credit: Optional[NoneType]
	internal: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelDataInternalData

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingData(TypedDict):
	__typename: str
	chargeModel: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingDataChargemodelData

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemQuantityData(TypedDict):
	__typename: str
	max: int
	min: int

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItem(TypedDict):
	__typename: str
	eligibility: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemEligibilityData
	giftType: Optional[NoneType]
	id: str
	listing: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemListingData
	platform: str
	promotion: Optional[NoneType]
	quantity: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemQuantityData
	tagBindings: List[SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItemTagbindingsItem]
	tplr: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemSelfData(TypedDict):
	__typename: str
	canGiftInChannel: Optional[bool]

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItem(TypedDict):
	__typename: str
	displayName: str
	emoteModifiers: List[Any]
	emoteSetID: str
	emotes: List[SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemEmotesItem]
	gifting: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemGiftingData
	hasAdFree: Optional[bool]
	id: str
	interval: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemIntervalData
	name: str
	offers: List[SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemOffersItem]
	price: str
	self: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItemSelfData
	tier: str
	type: str
	url: str

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultData(TypedDict):
	__typename: str
	nodes: List[SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultDataNodesItem]

class SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginData(TypedDict):
	__typename: str
	id: str
	self: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSelfData
	subscriptionProductsResult: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginDataSubscriptionproductsresultData

class SupportPanelSubscribeViewFooterPrimeResponse(TypedDict):
	userResultByLogin: SupportPanelSubscribeViewFooterPrimeResponseUserresultbyloginData

class SupportPanelFooterPrimeStatusRequest(TypedDict):
	login: str

class SupportPanelFooterPrimeStatusResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class SupportPanelFooterPrimeStatusResponseCurrentuserData(TypedDict):
	__typename: str
	hasPrime: Optional[bool]
	id: str

class SupportPanelFooterPrimeStatusResponseUserDataSelfDataPrimesubcreditbenefitData(TypedDict):
	__typename: str
	renewalDate: Optional[NoneType]
	willRenew: Optional[bool]

class SupportPanelFooterPrimeStatusResponseUserDataSelfData(TypedDict):
	__typename: str
	canPrimeSubscribe: Optional[bool]
	primeSubCreditBenefit: SupportPanelFooterPrimeStatusResponseUserDataSelfDataPrimesubcreditbenefitData

class SupportPanelFooterPrimeStatusResponseUserData(TypedDict):
	__typename: str
	id: str
	self: SupportPanelFooterPrimeStatusResponseUserDataSelfData

class SupportPanelFooterPrimeStatusResponse(TypedDict):
	requestInfo: SupportPanelFooterPrimeStatusResponseRequestinfoData
	currentUser: SupportPanelFooterPrimeStatusResponseCurrentuserData
	user: SupportPanelFooterPrimeStatusResponseUserData

class PersonalSectionsHypeTrainsRequest(TypedDict):
	channelIDs: List[str]

class PersonalSectionsHypeTrainsResponseActivehypetrainstatusesItemChannelData(TypedDict):
	__typename: str
	id: str

class PersonalSectionsHypeTrainsResponseActivehypetrainstatusesItem(TypedDict):
	__typename: str
	channel: PersonalSectionsHypeTrainsResponseActivehypetrainstatusesItemChannelData
	id: str
	isAllTimeHighTrain: Optional[bool]
	isGoldenKappaTrain: Optional[bool]
	level: int

class PersonalSectionsHypeTrainsResponse(TypedDict):
	activeHypeTrainStatuses: List[PersonalSectionsHypeTrainsResponseActivehypetrainstatusesItem]

class MinimalTopNav_MinimalUserRequest(TypedDict):
	...

class MinimalTopNav_MinimalUserResponseCurrentuserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str

class MinimalTopNav_MinimalUserResponse(TypedDict):
	currentUser: MinimalTopNav_MinimalUserResponseCurrentuserData

class TurboProductInformationRequest(TypedDict):
	name: str

class TurboProductInformationResponseSubscriptionproductDataOffersItemEligibilityData(TypedDict):
	__typename: str
	benefitsStartAt: str
	isEligible: Optional[bool]

class TurboProductInformationResponseSubscriptionproductDataOffersItemListingDataChargemodelDataInternalDataPreviewpriceData(TypedDict):
	__typename: str
	currency: str
	discount: Optional[NoneType]
	exponent: int
	id: str
	total: int

class TurboProductInformationResponseSubscriptionproductDataOffersItemListingDataChargemodelDataInternalData(TypedDict):
	__typename: str
	previewPrice: TurboProductInformationResponseSubscriptionproductDataOffersItemListingDataChargemodelDataInternalDataPreviewpriceData

class TurboProductInformationResponseSubscriptionproductDataOffersItemListingDataChargemodelData(TypedDict):
	__typename: str
	internal: TurboProductInformationResponseSubscriptionproductDataOffersItemListingDataChargemodelDataInternalData

class TurboProductInformationResponseSubscriptionproductDataOffersItemListingData(TypedDict):
	__typename: str
	chargeModel: TurboProductInformationResponseSubscriptionproductDataOffersItemListingDataChargemodelData

class TurboProductInformationResponseSubscriptionproductDataOffersItemTagbindingsItem(TypedDict):
	__typename: str
	key: str
	value: str

class TurboProductInformationResponseSubscriptionproductDataOffersItem(TypedDict):
	__typename: str
	eligibility: TurboProductInformationResponseSubscriptionproductDataOffersItemEligibilityData
	id: str
	listing: TurboProductInformationResponseSubscriptionproductDataOffersItemListingData
	tagBindings: List[TurboProductInformationResponseSubscriptionproductDataOffersItemTagbindingsItem]
	tplr: str

class TurboProductInformationResponseSubscriptionproductDataSelfData(TypedDict):
	__typename: str
	benefit: Optional[NoneType]

class TurboProductInformationResponseSubscriptionproductData(TypedDict):
	__typename: str
	id: str
	offers: List[TurboProductInformationResponseSubscriptionproductDataOffersItem]
	self: TurboProductInformationResponseSubscriptionproductDataSelfData

class TurboProductInformationResponse(TypedDict):
	subscriptionProduct: TurboProductInformationResponseSubscriptionproductData

class Sub_AnalyticsRequest(TypedDict):
	channelID: str

class Sub_AnalyticsResponseUserDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class Sub_AnalyticsResponseUserData(TypedDict):
	__typename: str
	id: str
	self: Sub_AnalyticsResponseUserDataSelfData

class Sub_AnalyticsResponse(TypedDict):
	user: Sub_AnalyticsResponseUserData

class ChannelSocialButtonsRequest(TypedDict):
	channelID: str

class ChannelSocialButtonsResponseChannelDataLocalemotesetsItemEmotesItem(TypedDict):
	__typename: str
	id: str
	token: str
	type: str

class ChannelSocialButtonsResponseChannelDataLocalemotesetsItem(TypedDict):
	__typename: str
	emotes: List[ChannelSocialButtonsResponseChannelDataLocalemotesetsItemEmotesItem]
	id: str
	productType: str

class ChannelSocialButtonsResponseChannelData(TypedDict):
	__typename: str
	id: str
	localEmoteSets: List[ChannelSocialButtonsResponseChannelDataLocalemotesetsItem]

class ChannelSocialButtonsResponse(TypedDict):
	channel: ChannelSocialButtonsResponseChannelData

class RewardListRequest(TypedDict):
	channelID: str

class RewardListResponseChannelDataSelfData(TypedDict):
	__typename: str
	watchStreakMilestone: Optional[NoneType]

class RewardListResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: RewardListResponseChannelDataSelfData

class RewardListResponse(TypedDict):
	channel: RewardListResponseChannelData

class SearchTray_SearchSuggestionsRequest(TypedDict):
	requestID: str
	queryFragment: str
	withOfflineChannelContent: Optional[bool]
	includeIsDJ: Optional[bool]

class SearchTray_SearchSuggestionsResponseSearchsuggestionsDataEdgesItemNodeDataMatchingcharactersData(TypedDict):
	__typename: str
	end: int
	start: Optional[int]

class SearchTray_SearchSuggestionsResponseSearchsuggestionsDataEdgesItemNodeData(TypedDict):
	__typename: str
	content: Optional[NoneType]
	id: str
	matchingCharacters: SearchTray_SearchSuggestionsResponseSearchsuggestionsDataEdgesItemNodeDataMatchingcharactersData
	text: str

class SearchTray_SearchSuggestionsResponseSearchsuggestionsDataEdgesItem(TypedDict):
	__typename: str
	node: SearchTray_SearchSuggestionsResponseSearchsuggestionsDataEdgesItemNodeData

class SearchTray_SearchSuggestionsResponseSearchsuggestionsDataTrackingData(TypedDict):
	__typename: str
	modelTrackingID: str
	responseID: str

class SearchTray_SearchSuggestionsResponseSearchsuggestionsData(TypedDict):
	__typename: str
	edges: List[SearchTray_SearchSuggestionsResponseSearchsuggestionsDataEdgesItem]
	tracking: SearchTray_SearchSuggestionsResponseSearchsuggestionsDataTrackingData

class SearchTray_SearchSuggestionsResponse(TypedDict):
	searchSuggestions: SearchTray_SearchSuggestionsResponseSearchsuggestionsData

class SearchResultsPage_SearchResultsRequestOptionsData(TypedDict):
	shouldSkipDiscoveryControl: Optional[bool]
	targets: Optional[NoneType]

class SearchResultsPage_SearchResultsRequest(TypedDict):
	platform: str
	query: str
	options: SearchResultsPage_SearchResultsRequestOptionsData
	requestID: str
	includeIsDJ: Optional[bool]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataChannelDataScheduleDataNextsegmentData(TypedDict):
	__typename: str
	categories: List[Any]
	endAt: Optional[NoneType]
	hasReminder: Optional[bool]
	id: str
	startAt: str
	title: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataChannelDataScheduleData(TypedDict):
	__typename: str
	id: str
	nextSegment: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataChannelDataScheduleDataNextsegmentData

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataChannelData(TypedDict):
	__typename: str
	id: str
	schedule: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataChannelDataScheduleData

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataFollowersData(TypedDict):
	__typename: str
	totalCount: int

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLastbroadcastData(TypedDict):
	__typename: str
	id: str
	startedAt: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoDataEdgesItemNodeData(TypedDict):
	__typename: str
	id: str
	lengthSeconds: int
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	previewThumbnailURL: str
	templatePreviewThumbnailURL: str
	title: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoDataEdgesItem(TypedDict):
	__typename: str
	node: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoDataEdgesItemNodeData

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoData(TypedDict):
	__typename: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoDataEdgesItem]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataSelfDataFollowerData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataSelfDataFollowerData

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipDataEdgesItemNodeData(TypedDict):
	__typename: str
	durationSeconds: int
	id: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	slug: str
	thumbnailURL: str
	title: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipDataEdgesItem(TypedDict):
	__typename: str
	node: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipDataEdgesItemNodeData

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipData(TypedDict):
	__typename: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipDataEdgesItem]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemData(TypedDict):
	__typename: str
	broadcastSettings: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataBroadcastsettingsData
	channel: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataChannelData
	description: str
	displayName: str
	followers: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataFollowersData
	id: str
	lastBroadcast: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLastbroadcastData
	latestVideo: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataLatestvideoData
	login: str
	profileImageURL: str
	roles: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataRolesData
	self: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataSelfData
	stream: Optional[NoneType]
	topClip: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemDataTopclipData
	watchParty: Optional[NoneType]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItem(TypedDict):
	__typename: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItemItemData
	trackingID: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelsData(TypedDict):
	__typename: str
	cursor: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelsDataEdgesItem]
	score: int
	totalMatches: int

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataChannelData(TypedDict):
	__typename: str
	id: str
	schedule: Optional[NoneType]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataFollowersData(TypedDict):
	__typename: str
	totalCount: int

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataLastbroadcastData(TypedDict):
	__typename: str
	id: str
	startedAt: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataLatestvideoData(TypedDict):
	__typename: str
	edges: List[Any]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: Optional[NoneType]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	slug: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamData(TypedDict):
	__typename: str
	freeformTags: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamDataFreeformtagsItem]
	game: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamDataGameData
	id: str
	previewImageURL: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamDataPreviewthumbnailpropertiesData
	templatePreviewImageURL: str
	type: str
	viewersCount: int

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipDataEdgesItemNodeData(TypedDict):
	__typename: str
	durationSeconds: int
	id: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	slug: str
	thumbnailURL: str
	title: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipDataEdgesItem(TypedDict):
	__typename: str
	node: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipDataEdgesItemNodeData

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipData(TypedDict):
	__typename: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipDataEdgesItem]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemData(TypedDict):
	__typename: str
	broadcastSettings: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataBroadcastsettingsData
	channel: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataChannelData
	description: str
	displayName: str
	followers: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataFollowersData
	id: str
	lastBroadcast: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataLastbroadcastData
	latestVideo: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataLatestvideoData
	login: str
	profileImageURL: str
	roles: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataRolesData
	self: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataSelfData
	stream: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataStreamData
	topClip: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemDataTopclipData
	watchParty: Optional[NoneType]

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItem(TypedDict):
	__typename: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItemItemData
	trackingID: str

class SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagData(TypedDict):
	__typename: str
	cursor: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagDataEdgesItem]
	score: int
	totalMatches: int

class SearchResultsPage_SearchResultsResponseSearchforDataGamesData(TypedDict):
	__typename: str
	cursor: Optional[str]
	edges: List[Any]
	score: int
	totalMatches: Optional[int]

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataBroadcasterDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	title: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataBroadcasterData(TypedDict):
	__typename: str
	broadcastSettings: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataBroadcasterDataBroadcastsettingsData
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	roles: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataBroadcasterDataRolesData

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataGameData(TypedDict):
	__typename: str
	id: str
	name: str
	slug: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamData(TypedDict):
	__typename: str
	broadcaster: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataBroadcasterData
	game: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataGameData
	id: str
	previewImageURL: str
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamDataPreviewthumbnailpropertiesData
	templatePreviewImageURL: str
	viewersCount: int

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemData(TypedDict):
	__typename: str
	id: str
	stream: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemDataStreamData
	watchParty: Optional[NoneType]

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItem(TypedDict):
	__typename: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItemItemData
	trackingID: str

class SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsData(TypedDict):
	__typename: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsDataEdgesItem]
	score: int

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	slug: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataOwnerDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	roles: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataOwnerDataRolesData

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemData(TypedDict):
	__typename: str
	createdAt: str
	game: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataGameData
	id: str
	lengthSeconds: int
	owner: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataOwnerData
	previewThumbnailProperties: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemDataPreviewthumbnailpropertiesData
	previewThumbnailURL: str
	templatePreviewThumbnailURL: str
	title: str
	viewCount: int

class SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItem(TypedDict):
	__typename: str
	item: SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItemItemData
	trackingID: str

class SearchResultsPage_SearchResultsResponseSearchforDataVideosData(TypedDict):
	__typename: str
	cursor: str
	edges: List[SearchResultsPage_SearchResultsResponseSearchforDataVideosDataEdgesItem]
	score: int
	totalMatches: int

class SearchResultsPage_SearchResultsResponseSearchforData(TypedDict):
	__typename: str
	banners: Optional[NoneType]
	channels: SearchResultsPage_SearchResultsResponseSearchforDataChannelsData
	channelsWithTag: SearchResultsPage_SearchResultsResponseSearchforDataChannelswithtagData
	games: SearchResultsPage_SearchResultsResponseSearchforDataGamesData
	relatedLiveChannels: SearchResultsPage_SearchResultsResponseSearchforDataRelatedlivechannelsData
	videos: SearchResultsPage_SearchResultsResponseSearchforDataVideosData

class SearchResultsPage_SearchResultsResponse(TypedDict):
	searchFor: SearchResultsPage_SearchResultsResponseSearchforData

class LiveNotificationsToggle_UserRequest(TypedDict):
	login: str

class LiveNotificationsToggle_UserResponseUserDataSelfDataFollowerData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]
	followedAt: str

class LiveNotificationsToggle_UserResponseUserDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: LiveNotificationsToggle_UserResponseUserDataSelfDataFollowerData

class LiveNotificationsToggle_UserResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	self: LiveNotificationsToggle_UserResponseUserDataSelfData

class LiveNotificationsToggle_UserResponse(TypedDict):
	user: LiveNotificationsToggle_UserResponseUserData

class Directory_DirectoryBannerRequest(TypedDict):
	slug: str

class Directory_DirectoryBannerResponseGameDataStreamsData(TypedDict):
	__typename: str
	edges: List[Any]

class Directory_DirectoryBannerResponseGameDataTagsItem(TypedDict):
	__typename: str
	id: str
	isLanguageTag: Optional[bool]
	localizedName: str
	tagName: str

class Directory_DirectoryBannerResponseGameData(TypedDict):
	__typename: str
	avatarURL: str
	coverURL: Optional[NoneType]
	description: str
	displayName: str
	followersCount: int
	id: str
	igdbURL: str
	name: str
	prestoID: Optional[NoneType]
	slug: str
	streams: Directory_DirectoryBannerResponseGameDataStreamsData
	tags: List[Directory_DirectoryBannerResponseGameDataTagsItem]
	viewersCount: Optional[NoneType]

class Directory_DirectoryBannerResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isSiteAdmin: Optional[NoneType]
	isStaff: Optional[NoneType]

class Directory_DirectoryBannerResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	roles: Directory_DirectoryBannerResponseCurrentuserDataRolesData

class Directory_DirectoryBannerResponse(TypedDict):
	game: Directory_DirectoryBannerResponseGameData
	currentUser: Directory_DirectoryBannerResponseCurrentuserData

class DirectoryPage_GameRequestOptionsDataRecommendationscontextData(TypedDict):
	platform: str

class DirectoryPage_GameRequestOptionsData(TypedDict):
	broadcasterLanguages: List[Any]
	freeformTags: Optional[NoneType]
	includeRestricted: List[str]
	recommendationsContext: DirectoryPage_GameRequestOptionsDataRecommendationscontextData
	requestID: str
	sort: str
	systemFilters: List[Any]
	tags: List[Any]

class DirectoryPage_GameRequest(TypedDict):
	imageWidth: int
	slug: str
	options: DirectoryPage_GameRequestOptionsData
	sortTypeIsRecency: Optional[bool]
	limit: int
	includeIsDJ: Optional[bool]

class DirectoryPage_GameResponseGameDataStreamsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class DirectoryPage_GameResponseGameDataStreamsData(TypedDict):
	__typename: str
	banners: Optional[NoneType]
	edges: List[Any]
	pageInfo: DirectoryPage_GameResponseGameDataStreamsDataPageinfoData

class DirectoryPage_GameResponseGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	streams: DirectoryPage_GameResponseGameDataStreamsData

class DirectoryPage_GameResponse(TypedDict):
	game: DirectoryPage_GameResponseGameData

class DirectoryRoot_DirectoryRequest(TypedDict):
	slug: str

class DirectoryRoot_DirectoryResponseGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	slug: str

class DirectoryRoot_DirectoryResponse(TypedDict):
	game: DirectoryRoot_DirectoryResponseGameData

class FollowGameButton_GameRequest(TypedDict):
	slug: str

class FollowGameButton_GameResponseGameDataSelfData(TypedDict):
	__typename: str
	follow: Optional[NoneType]

class FollowGameButton_GameResponseGameData(TypedDict):
	__typename: str
	id: str
	name: str
	self: FollowGameButton_GameResponseGameDataSelfData

class FollowGameButton_GameResponseCurrentuserData(TypedDict):
	__typename: str
	id: str

class FollowGameButton_GameResponse(TypedDict):
	game: FollowGameButton_GameResponseGameData
	currentUser: FollowGameButton_GameResponseCurrentuserData

class DirectoryVideos_GameRequest1(TypedDict):
	includePreviewBlur: Optional[bool]
	slug: str
	videoLimit: int
	languages: List[Any]
	videoSort: str

class DirectoryVideos_GameRequest2(TypedDict):
	includePreviewBlur: Optional[bool]
	slug: str
	videoLimit: int
	languages: List[Any]
	videoSort: str
	followedCursor: str

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataOwnerDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataOwnerDataRolesData

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataSelfDataViewinghistoryData(TypedDict):
	__typename: str
	position: Optional[NoneType]
	updatedAt: Optional[NoneType]

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataSelfData(TypedDict):
	__typename: str
	isRestricted: Optional[bool]
	viewingHistory: DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataSelfDataViewinghistoryData

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeData(TypedDict):
	__typename: str
	animatedPreviewURL: str
	contentTags: List[Any]
	game: DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataGameData
	id: str
	lengthSeconds: int
	owner: DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataOwnerData
	previewThumbnailProperties: DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	previewThumbnailURL: str
	publishedAt: str
	resourceRestriction: Optional[NoneType]
	self: DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeDataSelfData
	title: str
	viewCount: int

class DirectoryVideos_GameResponseGameDataVideosDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[NoneType]
	node: DirectoryVideos_GameResponseGameDataVideosDataEdgesItemNodeData

class DirectoryVideos_GameResponseGameDataVideosDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class DirectoryVideos_GameResponseGameDataVideosData(TypedDict):
	__typename: str
	banners: Optional[NoneType]
	edges: List[DirectoryVideos_GameResponseGameDataVideosDataEdgesItem]
	pageInfo: DirectoryVideos_GameResponseGameDataVideosDataPageinfoData

class DirectoryVideos_GameResponseGameData(TypedDict):
	__typename: str
	id: str
	name: str
	videos: DirectoryVideos_GameResponseGameDataVideosData

class DirectoryVideos_GameResponse(TypedDict):
	game: DirectoryVideos_GameResponseGameData

class Prime_PrimeOfferList_PrimeOffers_EligibilityRequest(TypedDict):
	...

class Prime_PrimeOfferList_PrimeOffers_EligibilityResponsePrimeofferswitheligibilityItemContentData(TypedDict):
	__typename: str
	categories: List[str]
	ctaText: Optional[str]
	ctaType: Optional[str]
	externalURL: str
	publisher: str
	shortDescription: str
	subtitleSubtext: Optional[str]

class Prime_PrimeOfferList_PrimeOffers_EligibilityResponsePrimeofferswitheligibilityItemOffereligibilityData(TypedDict):
	__typename: str
	canClaim: Optional[bool]
	isClaimed: Optional[bool]
	offerState: str

class Prime_PrimeOfferList_PrimeOffers_EligibilityResponsePrimeofferswitheligibilityItem(TypedDict):
	__typename: str
	catalogOfferID: str
	claimInstructions: str
	content: Prime_PrimeOfferList_PrimeOffers_EligibilityResponsePrimeofferswitheligibilityItemContentData
	deliveryMethod: str
	description: Optional[str]
	endTime: str
	gameTitle: str
	id: str
	imageURL: str
	offerEligibility: Prime_PrimeOfferList_PrimeOffers_EligibilityResponsePrimeofferswitheligibilityItemOffereligibilityData
	priority: int
	tags: List[str]
	title: str

class Prime_PrimeOfferList_PrimeOffers_EligibilityResponse(TypedDict):
	primeOffersWithEligibility: List[Prime_PrimeOfferList_PrimeOffers_EligibilityResponsePrimeofferswitheligibilityItem]

class OnsiteNotifications_ViewRequest(TypedDict):
	...

class OnsiteNotifications_ViewResponseViewednotificationsDataUserDataNotificationsDataSummaryData(TypedDict):
	__typename: str
	lastSeenAt: str
	unseenCount: Optional[int]

class OnsiteNotifications_ViewResponseViewednotificationsDataUserDataNotificationsData(TypedDict):
	__typename: str
	summary: OnsiteNotifications_ViewResponseViewednotificationsDataUserDataNotificationsDataSummaryData

class OnsiteNotifications_ViewResponseViewednotificationsDataUserData(TypedDict):
	__typename: str
	id: str
	notifications: OnsiteNotifications_ViewResponseViewednotificationsDataUserDataNotificationsData

class OnsiteNotifications_ViewResponseViewednotificationsData(TypedDict):
	__typename: str
	user: OnsiteNotifications_ViewResponseViewednotificationsDataUserData

class OnsiteNotifications_ViewResponse(TypedDict):
	viewedNotifications: OnsiteNotifications_ViewResponseViewednotificationsData

class OnsiteNotifications_ListNotificationsRequest(TypedDict):
	shouldLoadLastBroadcast: Optional[bool]
	limit: int
	cursor: Optional[str]
	language: str
	displayType: str

class OnsiteNotifications_ListNotificationsResponseCurrentuserDataNotificationsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class OnsiteNotifications_ListNotificationsResponseCurrentuserDataNotificationsData(TypedDict):
	__typename: str
	edges: List[Any]
	pageInfo: OnsiteNotifications_ListNotificationsResponseCurrentuserDataNotificationsDataPageinfoData

class OnsiteNotifications_ListNotificationsResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	notifications: OnsiteNotifications_ListNotificationsResponseCurrentuserDataNotificationsData

class OnsiteNotifications_ListNotificationsResponse(TypedDict):
	currentUser: OnsiteNotifications_ListNotificationsResponseCurrentuserData

class SettingsNotificationsPage_UserRequest(TypedDict):
	...

class SettingsNotificationsPage_UserResponseCurrentuserDataFollowsDataEdgesItemNotificationsettingsData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]

class SettingsNotificationsPage_UserResponseCurrentuserDataFollowsDataEdgesItem(TypedDict):
	__typename: str
	notificationSettings: SettingsNotificationsPage_UserResponseCurrentuserDataFollowsDataEdgesItemNotificationsettingsData

class SettingsNotificationsPage_UserResponseCurrentuserDataFollowsData(TypedDict):
	__typename: str
	edges: List[SettingsNotificationsPage_UserResponseCurrentuserDataFollowsDataEdgesItem]
	totalCount: int

class SettingsNotificationsPage_UserResponseCurrentuserDataNotificationsettingsItemPlatformsItem(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	platformName: str
	settingState: str

class SettingsNotificationsPage_UserResponseCurrentuserDataNotificationsettingsItem(TypedDict):
	__typename: str
	category: str
	platforms: List[SettingsNotificationsPage_UserResponseCurrentuserDataNotificationsettingsItemPlatformsItem]

class SettingsNotificationsPage_UserResponseCurrentuserData(TypedDict):
	__typename: str
	follows: SettingsNotificationsPage_UserResponseCurrentuserDataFollowsData
	id: str
	notificationSettings: List[SettingsNotificationsPage_UserResponseCurrentuserDataNotificationsettingsItem]

class SettingsNotificationsPage_UserResponse(TypedDict):
	currentUser: SettingsNotificationsPage_UserResponseCurrentuserData

class SmartNotificationSettings_UserRequest(TypedDict):
	...

class SmartNotificationSettings_UserResponseCurrentuserDataNotificationsettingsItemPlatformsItem(TypedDict):
	__typename: str
	isEnabled: Optional[bool]
	platformName: str
	settingState: str

class SmartNotificationSettings_UserResponseCurrentuserDataNotificationsettingsItem(TypedDict):
	__typename: str
	category: str
	platforms: List[SmartNotificationSettings_UserResponseCurrentuserDataNotificationsettingsItemPlatformsItem]

class SmartNotificationSettings_UserResponseCurrentuserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	notificationSettings: List[SmartNotificationSettings_UserResponseCurrentuserDataNotificationsettingsItem]

class SmartNotificationSettings_UserResponse(TypedDict):
	currentUser: SmartNotificationSettings_UserResponseCurrentuserData

class PlatformNotificationSettings_UserRequest(TypedDict):
	...

class PlatformNotificationSettings_UserResponseCurrentuserData(TypedDict):
	__typename: str
	displayName: str
	id: str

class PlatformNotificationSettings_UserResponse(TypedDict):
	currentUser: PlatformNotificationSettings_UserResponseCurrentuserData

class AdvancedNotificationSettings_UserRequest(TypedDict):
	limit: int

class AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItemNodeDataFollowersData(TypedDict):
	__typename: str
	totalCount: int

class AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItemNodeData(TypedDict):
	__typename: str
	displayName: str
	followers: AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItemNodeDataFollowersData
	id: str
	login: str
	profileImageURL: str

class AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItemNotificationsettingsData(TypedDict):
	__typename: str
	isEnabled: Optional[bool]

class AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItemNodeData
	notificationSettings: AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItemNotificationsettingsData

class AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsData(TypedDict):
	__typename: str
	edges: List[AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataEdgesItem]
	pageInfo: AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsDataPageinfoData
	totalCount: int

class AdvancedNotificationSettings_UserResponseCurrentuserData(TypedDict):
	__typename: str
	follows: AdvancedNotificationSettings_UserResponseCurrentuserDataFollowsData
	id: str

class AdvancedNotificationSettings_UserResponse(TypedDict):
	currentUser: AdvancedNotificationSettings_UserResponseCurrentuserData

class UserDJStatusQueryRequest(TypedDict):
	login: str

class UserDJStatusQueryResponseUserDataDjstatusData(TypedDict):
	__typename: str
	isOptOutBlocked: Optional[bool]
	lastProgramUpdate: str
	programState: str

class UserDJStatusQueryResponseUserData(TypedDict):
	__typename: str
	djStatus: UserDJStatusQueryResponseUserDataDjstatusData
	id: str

class UserDJStatusQueryResponse(TypedDict):
	user: UserDJStatusQueryResponseUserData

class SunlightLoggedInUserMenuQueryRequest(TypedDict):
	userLogin: str

class SunlightLoggedInUserMenuQueryResponseUserData(TypedDict):
	__typename: str
	hasUnreadChangelogItems: Optional[bool]
	id: str
	profileImageURL: str

class SunlightLoggedInUserMenuQueryResponse(TypedDict):
	user: SunlightLoggedInUserMenuQueryResponseUserData

class HasNewBountiesContextQueryRequest(TypedDict):
	channelLogin: str

class HasNewBountiesContextQueryResponseUserDataBountyboardsettingsData(TypedDict):
	__typename: str
	hasNotification: Optional[bool]
	status: str

class HasNewBountiesContextQueryResponseUserData(TypedDict):
	__typename: str
	bountyBoardSettings: HasNewBountiesContextQueryResponseUserDataBountyboardsettingsData
	id: str

class HasNewBountiesContextQueryResponse(TypedDict):
	user: HasNewBountiesContextQueryResponseUserData

class AccessIsBountiesEnabledQueryRequest(TypedDict):
	channelLogin: str

class AccessIsBountiesEnabledQueryResponseUserDataBountyboardsettingsData(TypedDict):
	__typename: str
	status: str

class AccessIsBountiesEnabledQueryResponseUserData(TypedDict):
	__typename: str
	bountyBoardSettings: AccessIsBountiesEnabledQueryResponseUserDataBountyboardsettingsData
	id: str

class AccessIsBountiesEnabledQueryResponse(TypedDict):
	user: AccessIsBountiesEnabledQueryResponseUserData

class CharityNavItemRequest(TypedDict):
	channelLogin: str

class CharityNavItemResponseChannelDataCharitycampaignsData(TypedDict):
	__typename: str
	edges: List[Any]

class CharityNavItemResponseChannelData(TypedDict):
	__typename: str
	activeCharityCampaign: Optional[NoneType]
	charityCampaigns: CharityNavItemResponseChannelDataCharitycampaignsData
	id: str

class CharityNavItemResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class CharityNavItemResponse(TypedDict):
	channel: CharityNavItemResponseChannelData
	requestInfo: CharityNavItemResponseRequestinfoData

class AccessIsExtensionsDeveloperQueryRequest(TypedDict):
	channelLogin: str
	isChannelLoginSameAsUserLogin: Optional[bool]

class AccessIsExtensionsDeveloperQueryResponseUserDataRolesData(TypedDict):
	__typename: str
	isExtensionsDeveloper: Optional[bool]

class AccessIsExtensionsDeveloperQueryResponseUserData(TypedDict):
	__typename: str
	id: str
	payoutInvite: Optional[NoneType]
	roles: AccessIsExtensionsDeveloperQueryResponseUserDataRolesData

class AccessIsExtensionsDeveloperQueryResponse(TypedDict):
	user: AccessIsExtensionsDeveloperQueryResponseUserData

class AccessIsSiteAdminQueryRequest(TypedDict):
	channelLogin: str

class AccessIsSiteAdminQueryResponseUserDataRolesData(TypedDict):
	__typename: str
	isSiteAdmin: Optional[NoneType]

class AccessIsSiteAdminQueryResponseUserData(TypedDict):
	__typename: str
	id: str
	roles: AccessIsSiteAdminQueryResponseUserDataRolesData

class AccessIsSiteAdminQueryResponse(TypedDict):
	user: AccessIsSiteAdminQueryResponseUserData

class AccessGetUserQueryRequest(TypedDict):
	channelLogin: str

class AccessGetUserQueryResponseUserData(TypedDict):
	__typename: str
	id: str

class AccessGetUserQueryResponse(TypedDict):
	user: AccessGetUserQueryResponseUserData

class Dashboard_CensusGetBirthdateRequest(TypedDict):
	...

class Dashboard_CensusGetBirthdateResponseCurrentuserDataOnboardinginvitationsData(TypedDict):
	__typename: str
	payout: Optional[NoneType]

class Dashboard_CensusGetBirthdateResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str
	onboardingInvitations: Dashboard_CensusGetBirthdateResponseCurrentuserDataOnboardinginvitationsData

class Dashboard_CensusGetBirthdateResponse(TypedDict):
	currentUser: Dashboard_CensusGetBirthdateResponseCurrentuserData

class AccessIsChannelPointsAvailableQueryRequest(TypedDict):
	channelLogin: str

class AccessIsChannelPointsAvailableQueryResponseUserDataChannelDataCommunitypointssettingsData(TypedDict):
	__typename: str
	isAvailable: Optional[bool]

class AccessIsChannelPointsAvailableQueryResponseUserDataChannelData(TypedDict):
	__typename: str
	communityPointsSettings: AccessIsChannelPointsAvailableQueryResponseUserDataChannelDataCommunitypointssettingsData
	id: str

class AccessIsChannelPointsAvailableQueryResponseUserData(TypedDict):
	__typename: str
	channel: AccessIsChannelPointsAvailableQueryResponseUserDataChannelData
	id: str

class AccessIsChannelPointsAvailableQueryResponse(TypedDict):
	user: AccessIsChannelPointsAvailableQueryResponseUserData

class broadcastLanguageQueryRequest(TypedDict):
	channelLogin: str

class broadcastLanguageQueryResponseUserDataBroadcastsettingsData(TypedDict):
	__typename: str
	id: str
	language: str

class broadcastLanguageQueryResponseUserData(TypedDict):
	__typename: str
	broadcastSettings: broadcastLanguageQueryResponseUserDataBroadcastsettingsData
	id: str

class broadcastLanguageQueryResponse(TypedDict):
	user: broadcastLanguageQueryResponseUserData

class DashboardChannelSettingsRequest(TypedDict):
	channelLogin: str

class DashboardChannelSettingsResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str

class DashboardChannelSettingsResponseUserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]
	isStaff: Optional[NoneType]

class DashboardChannelSettingsResponseUserDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class DashboardChannelSettingsResponseUserData(TypedDict):
	__typename: str
	id: str
	roles: DashboardChannelSettingsResponseUserDataRolesData
	self: DashboardChannelSettingsResponseUserDataSelfData

class DashboardChannelSettingsResponse(TypedDict):
	currentUser: DashboardChannelSettingsResponseCurrentuserData
	user: DashboardChannelSettingsResponseUserData

class AnnouncementsIconRequest(TypedDict):
	...

class AnnouncementsIconResponseUserData(TypedDict):
	__typename: str
	hasUnreadChangelogItems: Optional[bool]
	id: str

class AnnouncementsIconResponse(TypedDict):
	user: AnnouncementsIconResponseUserData

class AccessIsCommunityMomentsEnabledQueryRequest(TypedDict):
	channelID: str

class AccessIsCommunityMomentsEnabledQueryResponseExperimentData(TypedDict):
	__typename: str
	isInCommunityMomentsExperiment: Optional[bool]

class AccessIsCommunityMomentsEnabledQueryResponse(TypedDict):
	experiment: AccessIsCommunityMomentsEnabledQueryResponseExperimentData

class SponsorshipChannelSettingsRequest(TypedDict):
	channelLogin: str

class SponsorshipChannelSettingsResponseUsersponsorshipsettingsData(TypedDict):
	__typename: str
	activationSettings: Optional[NoneType]
	isProfileEligible: Optional[bool]

class SponsorshipChannelSettingsResponse(TypedDict):
	userSponsorshipSettings: SponsorshipChannelSettingsResponseUsersponsorshipsettingsData

class UserEmoticonPrefix_QueryRequest(TypedDict):
	...

class UserEmoticonPrefix_QueryResponseCurrentuserDataEmoticonprefixData(TypedDict):
	__typename: str
	isEditable: Optional[bool]
	name: Optional[str]
	state: str

class UserEmoticonPrefix_QueryResponseCurrentuserDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isPartner: Optional[bool]

class UserEmoticonPrefix_QueryResponseCurrentuserData(TypedDict):
	__typename: str
	emoticonPrefix: UserEmoticonPrefix_QueryResponseCurrentuserDataEmoticonprefixData
	id: str
	login: str
	roles: UserEmoticonPrefix_QueryResponseCurrentuserDataRolesData

class UserEmoticonPrefix_QueryResponse(TypedDict):
	currentUser: UserEmoticonPrefix_QueryResponseCurrentuserData

class Settings_ProfilePage_AccountInfoSettingsRequest(TypedDict):
	...

class Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserDataSettingsData(TypedDict):
	__typename: str
	preferredLanguageTag: str

class Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserData(TypedDict):
	__typename: str
	description: Optional[NoneType]
	displayName: str
	id: str
	isEmailVerified: Optional[bool]
	login: str
	settings: Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserDataSettingsData

class Settings_ProfilePage_AccountInfoSettingsResponse(TypedDict):
	currentUser: Settings_ProfilePage_AccountInfoSettingsResponseCurrentuserData

class SocialMediaRequest(TypedDict):
	channelID: str

class SocialMediaResponseUserDataChannelData(TypedDict):
	__typename: str
	id: str
	socialMedias: List[Any]

class SocialMediaResponseUserData(TypedDict):
	__typename: str
	channel: SocialMediaResponseUserDataChannelData
	id: str

class SocialMediaResponse(TypedDict):
	user: SocialMediaResponseUserData

class UpgradeTermsBannerQueryRequest(TypedDict):
	...

class UpgradeTermsBannerQueryResponseCurrentuserDataOnboardinginvitationsData(TypedDict):
	__typename: str
	upgrade: Optional[NoneType]

class UpgradeTermsBannerQueryResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	login: str
	onboardingInvitations: UpgradeTermsBannerQueryResponseCurrentuserDataOnboardinginvitationsData

class UpgradeTermsBannerQueryResponse(TypedDict):
	currentUser: UpgradeTermsBannerQueryResponseCurrentuserData

class CopyrightSchoolInvitationRequest(TypedDict):
	...

class CopyrightSchoolInvitationResponseCopyrightschoolinvitationData(TypedDict):
	__typename: str
	invitation: Optional[NoneType]

class CopyrightSchoolInvitationResponse(TypedDict):
	copyrightSchoolInvitation: CopyrightSchoolInvitationResponseCopyrightschoolinvitationData

class Settings_ChannelClipsSettingsRequest(TypedDict):
	channelLogin: str

class Settings_ChannelClipsSettingsResponseUserDataChannelDataClipssettingsData(TypedDict):
	__typename: str
	categoryBlocklist: List[Any]
	creationRestrictedTo: Optional[NoneType]
	creationRestrictionOptions: Optional[NoneType]
	discoverySetting: str
	featuringRestrictedTo: Optional[NoneType]
	hasAcknowledgedViewerExportsLegalDisclosure: Optional[bool]
	isClipsCreationEnabled: Optional[bool]
	isClipsFeatureToggleDefaultEnabled: Optional[bool]
	isViewerExportingEnabled: Optional[NoneType]

class Settings_ChannelClipsSettingsResponseUserDataChannelData(TypedDict):
	__typename: str
	clipsSettings: Settings_ChannelClipsSettingsResponseUserDataChannelDataClipssettingsData
	id: str

class Settings_ChannelClipsSettingsResponseUserDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]

class Settings_ChannelClipsSettingsResponseUserData(TypedDict):
	__typename: str
	channel: Settings_ChannelClipsSettingsResponseUserDataChannelData
	id: str
	roles: Settings_ChannelClipsSettingsResponseUserDataRolesData
	stream: Optional[NoneType]

class Settings_ChannelClipsSettingsResponse(TypedDict):
	user: Settings_ChannelClipsSettingsResponseUserData

class ProductConsentRequest(TypedDict):
	...

class ProductConsentResponseCurrentuserDataProductconsentDataProductconsentItem(TypedDict):
	__typename: str
	consentType: str
	id: str
	shouldShowNotification: Optional[bool]
	url: str
	version: str

class ProductConsentResponseCurrentuserDataProductconsentData(TypedDict):
	__typename: str
	productConsent: List[ProductConsentResponseCurrentuserDataProductconsentDataProductconsentItem]

class ProductConsentResponseCurrentuserData(TypedDict):
	__typename: str
	createdAt: str
	id: str
	productConsent: ProductConsentResponseCurrentuserDataProductconsentData

class ProductConsentResponse(TypedDict):
	currentUser: ProductConsentResponseCurrentuserData

class UsernameRenameStatusRequest(TypedDict):
	...

class UsernameRenameStatusResponseCurrentuserDataLoginrenamestatusData(TypedDict):
	__typename: str
	eligibleAt: str
	isEligible: Optional[bool]

class UsernameRenameStatusResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	loginRenameStatus: UsernameRenameStatusResponseCurrentuserDataLoginrenamestatusData

class UsernameRenameStatusResponse(TypedDict):
	currentUser: UsernameRenameStatusResponseCurrentuserData

class TaxExpiryQueryRequest(TypedDict):
	...

class TaxExpiryQueryResponseCurrentuserDataPayoutData(TypedDict):
	__typename: str
	taxIntents: Optional[NoneType]

class TaxExpiryQueryResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	payout: TaxExpiryQueryResponseCurrentuserDataPayoutData

class TaxExpiryQueryResponse(TypedDict):
	currentUser: TaxExpiryQueryResponseCurrentuserData

class GetBitsButton_BitsRequest(TypedDict):
	login: Optional[str]
	withChannel: Optional[bool]
	isLoggedIn: Optional[bool]

class GetBitsButton_BitsResponseCurrentuserDataBitsoffersItem(TypedDict):
	__typename: str
	bits: int
	id: str
	type: str

class GetBitsButton_BitsResponseCurrentuserDataBitsusersettingsDataFirstcheertutorialData(TypedDict):
	__typename: str
	hasAbandoned: Optional[bool]
	hasSkipped: Optional[bool]

class GetBitsButton_BitsResponseCurrentuserDataBitsusersettingsData(TypedDict):
	__typename: str
	firstCheerTutorial: GetBitsButton_BitsResponseCurrentuserDataBitsusersettingsDataFirstcheertutorialData

class GetBitsButton_BitsResponseCurrentuserData(TypedDict):
	__typename: str
	bitsBalance: Optional[int]
	bitsOffers: List[GetBitsButton_BitsResponseCurrentuserDataBitsoffersItem]
	bitsUserSettings: GetBitsButton_BitsResponseCurrentuserDataBitsusersettingsData
	bitsUserState: str
	id: str
	idSHA1: str

class GetBitsButton_BitsResponse(TypedDict):
	currentUser: GetBitsButton_BitsResponseCurrentuserData

class ChatHighlightSettingsRequest(TypedDict):
	...

class ChatHighlightSettingsResponseChathighlightsettingsDataFirsttimechattersDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: Optional[NoneType]
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataFirsttimechattersData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataFirsttimechattersDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsDataMentionsDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: Optional[NoneType]
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataMentionsData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataMentionsDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsDataModsDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: Optional[NoneType]
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataModsData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataModsDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsDataRaidersDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: int
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataRaidersData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataRaidersDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsDataReturningchattersDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: Optional[NoneType]
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataReturningchattersData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataReturningchattersDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsDataSubscribersDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: Optional[NoneType]
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataSubscribersData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataSubscribersDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsDataSuspicioususersDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: Optional[NoneType]
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataSuspicioususersData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataSuspicioususersDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsDataVipsDataDisplaysettingData(TypedDict):
	__typename: str
	chatHighlightDisplayMode: str
	durationMinutes: Optional[NoneType]
	isEnabled: Optional[bool]

class ChatHighlightSettingsResponseChathighlightsettingsDataVipsData(TypedDict):
	__typename: str
	displaySetting: ChatHighlightSettingsResponseChathighlightsettingsDataVipsDataDisplaysettingData
	releaseDate: str

class ChatHighlightSettingsResponseChathighlightsettingsData(TypedDict):
	__typename: str
	firstTimeChatters: ChatHighlightSettingsResponseChathighlightsettingsDataFirsttimechattersData
	lastSeen: Optional[NoneType]
	mentions: ChatHighlightSettingsResponseChathighlightsettingsDataMentionsData
	mods: ChatHighlightSettingsResponseChathighlightsettingsDataModsData
	raiders: ChatHighlightSettingsResponseChathighlightsettingsDataRaidersData
	returningChatters: ChatHighlightSettingsResponseChathighlightsettingsDataReturningchattersData
	shouldHideIcon: Optional[bool]
	subscribers: ChatHighlightSettingsResponseChathighlightsettingsDataSubscribersData
	suspiciousUsers: ChatHighlightSettingsResponseChathighlightsettingsDataSuspicioususersData
	vips: ChatHighlightSettingsResponseChathighlightsettingsDataVipsData

class ChatHighlightSettingsResponse(TypedDict):
	chatHighlightSettings: ChatHighlightSettingsResponseChathighlightsettingsData

class FollowPanelOverlayRequest(TypedDict):
	channelLogin: str

class FollowPanelOverlayResponseUserDataSelfData(TypedDict):
	__typename: str
	follower: Optional[NoneType]

class FollowPanelOverlayResponseUserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	self: FollowPanelOverlayResponseUserDataSelfData

class FollowPanelOverlayResponse(TypedDict):
	user: FollowPanelOverlayResponseUserData

class DashboardInsights_ChannelRequest(TypedDict):
	channelLogin: str

class DashboardInsights_ChannelResponseChannelDataLastbroadcastData(TypedDict):
	__typename: str
	id: Optional[NoneType]

class DashboardInsights_ChannelResponseChannelDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isExtensionsDeveloper: Optional[bool]
	isPartner: Optional[bool]

class DashboardInsights_ChannelResponseChannelData(TypedDict):
	__typename: str
	displayName: str
	id: str
	lastBroadcast: DashboardInsights_ChannelResponseChannelDataLastbroadcastData
	login: str
	roles: DashboardInsights_ChannelResponseChannelDataRolesData

class DashboardInsights_ChannelResponse(TypedDict):
	channel: DashboardInsights_ChannelResponseChannelData

class SunlightHomePageRequest(TypedDict):
	login: str

class SunlightHomePageResponseChannelDataLastbroadcastData(TypedDict):
	__typename: str
	id: Optional[NoneType]

class SunlightHomePageResponseChannelDataRolesData(TypedDict):
	__typename: str
	isAffiliate: Optional[bool]
	isExtensionsDeveloper: Optional[bool]
	isPartner: Optional[bool]

class SunlightHomePageResponseChannelDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class SunlightHomePageResponseChannelData(TypedDict):
	__typename: str
	displayName: str
	id: str
	lastBroadcast: SunlightHomePageResponseChannelDataLastbroadcastData
	login: str
	roles: SunlightHomePageResponseChannelDataRolesData
	self: SunlightHomePageResponseChannelDataSelfData

class SunlightHomePageResponse(TypedDict):
	channel: SunlightHomePageResponseChannelData

class GuestStarFavoriteGuestsRequest(TypedDict):
	channelID: str
	channelLogin: str
	after: Optional[str]
	first: int

class GuestStarFavoriteGuestsResponseGueststarfavoriteguestsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class GuestStarFavoriteGuestsResponseGueststarfavoriteguestsData(TypedDict):
	__typename: str
	edges: List[Any]
	pageInfo: GuestStarFavoriteGuestsResponseGueststarfavoriteguestsDataPageinfoData
	status: str

class GuestStarFavoriteGuestsResponse(TypedDict):
	guestStarFavoriteGuests: GuestStarFavoriteGuestsResponseGueststarfavoriteguestsData

class CreatorHomeGetEmoteDataRequest(TypedDict):
	channelID: str

class CreatorHomeGetEmoteDataResponseUserDataEmoticonprefixData(TypedDict):
	__typename: str
	name: Optional[str]

class CreatorHomeGetEmoteDataResponseUserData(TypedDict):
	__typename: str
	emoticonPrefix: CreatorHomeGetEmoteDataResponseUserDataEmoticonprefixData
	id: str
	isInEmoteGoodStanding: Optional[bool]
	subscriptionProducts: List[Any]

class CreatorHomeGetEmoteDataResponse(TypedDict):
	user: CreatorHomeGetEmoteDataResponseUserData

class SunlightHomePageCardsRequest(TypedDict):
	channelID: str
	browserTime: str
	platform: str

class SunlightHomePageCardsResponseCreatorhomeDataClustersItem(TypedDict):
	__typename: str
	id: str

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemActionsItemEventData(TypedDict):
	__typename: str
	modalName: str

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemActionsItemTriggerData(TypedDict):
	__typename: str
	fieldType: str

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemActionsItem(TypedDict):
	__typename: str
	event: SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemActionsItemEventData
	trigger: SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemActionsItemTriggerData

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemDecoratorsData(TypedDict):
	__typename: str
	backgroundImageURL: Optional[str]
	externalVideoURL: Optional[str]
	icon: Optional[NoneType]
	imageURL: str
	vod: Optional[NoneType]

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentDataNodesItemDecoratorData(TypedDict):
	__typename: str
	hasEmphasis: Optional[bool]
	hasHighlight: Optional[bool]
	highlightColor: Optional[str]

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentDataNodesItemValueData(TypedDict):
	__typename: str
	text: str

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentDataNodesItem(TypedDict):
	__typename: str
	decorator: SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentDataNodesItemDecoratorData
	value: SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentDataNodesItemValueData

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentData(TypedDict):
	__typename: str
	nodes: List[SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentDataNodesItem]

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItem(TypedDict):
	__typename: str
	content: SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItemContentData
	fieldType: str
	style: Optional[NoneType]

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTrackingmetadataData(TypedDict):
	__typename: str
	itemRole: str

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItem(TypedDict):
	__typename: str
	actions: List[SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemActionsItem]
	colorTheme: str
	customContent: Optional[NoneType]
	decorators: SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemDecoratorsData
	dismissalOptions: Optional[NoneType]
	display: Optional[NoneType]
	error: Optional[NoneType]
	identifier: str
	pollingOptions: Optional[NoneType]
	template: str
	testPageMetadata: Optional[NoneType]
	tokenizedTextSections: List[SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTokenizedtextsectionsItem]
	trackingMetadata: SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItemTrackingmetadataData

class SunlightHomePageCardsResponseCreatorhomeDataPanelsItem(TypedDict):
	__typename: str
	cards: List[SunlightHomePageCardsResponseCreatorhomeDataPanelsItemCardsItem]
	type: str

class SunlightHomePageCardsResponseCreatorhomeData(TypedDict):
	__typename: str
	clusters: List[SunlightHomePageCardsResponseCreatorhomeDataClustersItem]
	id: str
	panels: List[SunlightHomePageCardsResponseCreatorhomeDataPanelsItem]

class SunlightHomePageCardsResponse(TypedDict):
	creatorHome: SunlightHomePageCardsResponseCreatorhomeData

class ShieldModeStateRequest(TypedDict):
	channelID: str

class ShieldModeStateResponseChannelshieldmodeData(TypedDict):
	__typename: str
	id: str
	isActive: Optional[bool]
	isShortcutEnabled: Optional[bool]
	lastDisabledAt: Optional[NoneType]
	lastDisabledBy: Optional[NoneType]
	lastEnabledAt: Optional[NoneType]
	lastEnabledBy: Optional[NoneType]

class ShieldModeStateResponse(TypedDict):
	channelShieldMode: ShieldModeStateResponseChannelshieldmodeData

class AchievementsPageRequest(TypedDict):
	channelID: str

class AchievementsPageResponseAchievementspageData(TypedDict):
	__typename: str
	achievements: List[Any]

class AchievementsPageResponse(TypedDict):
	achievementsPage: AchievementsPageResponseAchievementspageData

class StreamSummaryPage_GetRecentStreamSessionsRequest(TypedDict):
	channelID: str

class StreamSummaryPage_GetRecentStreamSessionsResponseUserData(TypedDict):
	__typename: str
	id: str
	streamSessions: List[Any]

class StreamSummaryPage_GetRecentStreamSessionsResponse(TypedDict):
	user: StreamSummaryPage_GetRecentStreamSessionsResponseUserData

class ArtistAttributionChannelsRequest(TypedDict):
	limit: int

class ArtistAttributionChannelsResponseEmoteattributionchannelsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]
	hasPreviousPage: Optional[bool]

class ArtistAttributionChannelsResponseEmoteattributionchannelsData(TypedDict):
	__typename: str
	edges: Optional[NoneType]
	hasEmoteAttributionEnabled: Optional[bool]
	pageInfo: ArtistAttributionChannelsResponseEmoteattributionchannelsDataPageinfoData

class ArtistAttributionChannelsResponse(TypedDict):
	emoteAttributionChannels: ArtistAttributionChannelsResponseEmoteattributionchannelsData

class UseCreatorHomeActionDataQueryRequest(TypedDict):
	userID: str

class UseCreatorHomeActionDataQueryResponseUserDataChannelDataHomeDataPreferencesData(TypedDict):
	__typename: str
	heroPreset: str

class UseCreatorHomeActionDataQueryResponseUserDataChannelDataHomeData(TypedDict):
	__typename: str
	preferences: UseCreatorHomeActionDataQueryResponseUserDataChannelDataHomeDataPreferencesData

class UseCreatorHomeActionDataQueryResponseUserDataChannelData(TypedDict):
	__typename: str
	home: UseCreatorHomeActionDataQueryResponseUserDataChannelDataHomeData
	id: str
	socialMedias: List[Any]

class UseCreatorHomeActionDataQueryResponseUserData(TypedDict):
	__typename: str
	channel: UseCreatorHomeActionDataQueryResponseUserDataChannelData
	description: Optional[NoneType]
	displayName: str
	id: str
	installedExtensions: List[Any]
	primaryColorHex: Optional[NoneType]
	profileImageURL: str

class UseCreatorHomeActionDataQueryResponse(TypedDict):
	user: UseCreatorHomeActionDataQueryResponseUserData

class CreatorHomeSuggestedExtensionsRequest(TypedDict):
	categoryID: str

class CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsDataEdgesItemNodeDataIconurlsData(TypedDict):
	__typename: str
	square100: str

class CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsDataEdgesItemNodeData(TypedDict):
	__typename: str
	clientID: str
	iconURLs: CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsDataEdgesItemNodeDataIconurlsData
	id: str
	name: str
	summary: str
	version: str

class CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsDataEdgesItem(TypedDict):
	__typename: str
	node: CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsDataEdgesItemNodeData

class CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsData(TypedDict):
	__typename: str
	edges: List[CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsDataEdgesItem]

class CreatorHomeSuggestedExtensionsResponseExtensioncategoryData(TypedDict):
	__typename: str
	extensions: CreatorHomeSuggestedExtensionsResponseExtensioncategoryDataExtensionsData
	id: str

class CreatorHomeSuggestedExtensionsResponse(TypedDict):
	extensionCategory: CreatorHomeSuggestedExtensionsResponseExtensioncategoryData

class SubscriptionsManagement_SubscriptionBenefitsRequest(TypedDict):
	limit: int
	cursor: Optional[str]
	filter: str
	platform: str

class SubscriptionsManagement_SubscriptionBenefitsResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserDataAvailablebadgesItem(TypedDict):
	__typename: str
	clickAction: Optional[NoneType]
	clickURL: Optional[NoneType]
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserDataSubscriptionsettingsData(TypedDict):
	__typename: str
	isFounderBadgesHidden: Optional[bool]

class SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserDataSubscriptiontokenData(TypedDict):
	__typename: str
	balance: Optional[int]

class SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserData(TypedDict):
	__typename: str
	availableBadges: List[SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserDataAvailablebadgesItem]
	hasPrime: Optional[bool]
	id: str
	subscriptionBenefits: Optional[NoneType]
	subscriptionSettings: SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserDataSubscriptionsettingsData
	subscriptionToken: SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserDataSubscriptiontokenData

class SubscriptionsManagement_SubscriptionBenefitsResponseMoneybannernotificationsItem(TypedDict):
	__typename: str
	id: str
	location: str
	metadata: Optional[NoneType]
	position: str
	priority: int

class SubscriptionsManagement_SubscriptionBenefitsResponse(TypedDict):
	requestInfo: SubscriptionsManagement_SubscriptionBenefitsResponseRequestinfoData
	currentUser: SubscriptionsManagement_SubscriptionBenefitsResponseCurrentuserData
	moneyBannerNotifications: List[SubscriptionsManagement_SubscriptionBenefitsResponseMoneybannernotificationsItem]

class UnbanRequestsListCtxRequest(TypedDict):
	limit: int
	order: str
	status: str
	channelLogin: str

class UnbanRequestsListCtxResponseChannelDataUnbanrequestsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class UnbanRequestsListCtxResponseChannelDataUnbanrequestsData(TypedDict):
	__typename: str
	edges: Optional[NoneType]
	pageInfo: UnbanRequestsListCtxResponseChannelDataUnbanrequestsDataPageinfoData
	totalCount: Optional[NoneType]

class UnbanRequestsListCtxResponseChannelDataUnbanrequestssettingsData(TypedDict):
	__typename: str
	cooldownMinutes: int
	isEnabled: Optional[bool]

class UnbanRequestsListCtxResponseChannelData(TypedDict):
	__typename: str
	id: str
	unbanRequests: UnbanRequestsListCtxResponseChannelDataUnbanrequestsData
	unbanRequestsSettings: UnbanRequestsListCtxResponseChannelDataUnbanrequestssettingsData

class UnbanRequestsListCtxResponse(TypedDict):
	channel: UnbanRequestsListCtxResponseChannelData

class InventoryRequest(TypedDict):
	fetchRewardCampaigns: Optional[bool]

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemAllowData(TypedDict):
	__typename: str
	channels: Optional[NoneType]

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemGameData(TypedDict):
	__typename: str
	boxArtURL: str
	id: str
	name: str
	slug: str

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemSelfData(TypedDict):
	__typename: str
	isAccountConnected: Optional[bool]

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemBenefitedgesItemBenefitData(TypedDict):
	__typename: str
	distributionType: str
	id: str
	imageAssetURL: str
	name: str

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemBenefitedgesItem(TypedDict):
	__typename: str
	benefit: InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemBenefitedgesItemBenefitData
	claimCount: Optional[int]
	entitlementLimit: int

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemCampaignDataSelfData(TypedDict):
	__typename: str
	isAccountConnected: Optional[bool]

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemCampaignData(TypedDict):
	__typename: str
	accountLinkURL: str
	detailsURL: str
	id: str
	self: InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemCampaignDataSelfData

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemSelfData(TypedDict):
	__typename: str
	currentMinutesWatched: int
	currentSubs: Optional[int]
	dropInstanceID: Optional[NoneType]
	hasPreconditionsMet: Optional[bool]
	isClaimed: Optional[bool]

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItem(TypedDict):
	__typename: str
	benefitEdges: List[InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemBenefitedgesItem]
	campaign: InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemCampaignData
	endAt: str
	id: str
	name: str
	preconditionDrops: Optional[NoneType]
	requiredMinutesWatched: int
	requiredSubs: Optional[int]
	self: InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItemSelfData
	startAt: str

class InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItem(TypedDict):
	__typename: str
	accountLinkURL: str
	allow: InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemAllowData
	detailsURL: str
	endAt: str
	eventBasedDrops: List[Any]
	game: InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemGameData
	id: str
	imageURL: str
	name: str
	self: InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemSelfData
	startAt: str
	status: str
	timeBasedDrops: List[InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItemTimebaseddropsItem]

class InventoryResponseCurrentuserDataInventoryData(TypedDict):
	__typename: str
	completedRewardCampaigns: List[Any]
	dropCampaignsInProgress: List[InventoryResponseCurrentuserDataInventoryDataDropcampaignsinprogressItem]
	gameEventDrops: List[Any]

class InventoryResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	inventory: InventoryResponseCurrentuserDataInventoryData

class InventoryResponse(TypedDict):
	currentUser: InventoryResponseCurrentuserData

class ChannelSharedBansRequest(TypedDict):
	channelID: str

class ChannelSharedBansResponseChannelDataBanssharingrelationshipsData(TypedDict):
	__typename: str
	acceptedRequests: List[Any]

class ChannelSharedBansResponseChannelData(TypedDict):
	__typename: str
	bansSharingRelationships: ChannelSharedBansResponseChannelDataBanssharingrelationshipsData
	id: str

class ChannelSharedBansResponse(TypedDict):
	channel: ChannelSharedBansResponseChannelData

class GetGuestStarSessionQueryRequestSessionoptionsData(TypedDict):
	channelLogin: str

class GetGuestStarSessionQueryRequest(TypedDict):
	channelLogin: str
	sessionOptions: GetGuestStarSessionQueryRequestSessionoptionsData
	isAuthenticatedRequest: Optional[bool]

class GetGuestStarSessionQueryResponseHostData(TypedDict):
	__typename: str
	description: Optional[NoneType]
	displayName: str
	id: str
	login: str
	primaryColorHex: Optional[NoneType]
	profileImageURL: str

class GetGuestStarSessionQueryResponseGueststarsettingsData(TypedDict):
	__typename: str
	id: str
	slotCount: int
	viewOnlyToken: str

class GetGuestStarSessionQueryResponse(TypedDict):
	host: GetGuestStarSessionQueryResponseHostData
	guestStarSettings: GetGuestStarSessionQueryResponseGueststarsettingsData
	guestStarSession: Optional[NoneType]

class SettingsTabs_UserRequest(TypedDict):
	...

class SettingsTabs_UserResponseCurrentuserData(TypedDict):
	__typename: str
	hasPrime: Optional[bool]
	hasTurbo: Optional[bool]
	id: str

class SettingsTabs_UserResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class SettingsTabs_UserResponse(TypedDict):
	currentUser: SettingsTabs_UserResponseCurrentuserData
	requestInfo: SettingsTabs_UserResponseRequestinfoData

class ProfileImageSettingRequest(TypedDict):
	...

class ProfileImageSettingResponseCurrentuserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	profileImageURL: str

class ProfileImageSettingResponse(TypedDict):
	currentUser: ProfileImageSettingResponseCurrentuserData

class ProfileBannerSettingRequest(TypedDict):
	...

class ProfileBannerSettingResponseCurrentuserData(TypedDict):
	__typename: str
	bannerImageURL: Optional[NoneType]
	displayName: str
	id: str
	login: str

class ProfileBannerSettingResponse(TypedDict):
	currentUser: ProfileBannerSettingResponseCurrentuserData

class PaymentMethodsTab_UserPaymentMethodsRequest(TypedDict):
	...

class PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsDataRecurlyDataPaywithamazonconfigsData(TypedDict):
	__typename: str
	clientID: Optional[str]
	isProduction: Optional[bool]
	sellerID: Optional[str]

class PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsDataRecurlyData(TypedDict):
	__typename: str
	braintreeClientAuthorization: Optional[str]
	payWithAmazonConfigs: PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsDataRecurlyDataPaywithamazonconfigsData
	publicKey: Optional[str]

class PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsDataXsollaData(TypedDict):
	__typename: str
	isSandbox: Optional[bool]
	token: Optional[str]

class PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsData(TypedDict):
	__typename: str
	recurly: PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsDataRecurlyData
	xsolla: PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsDataXsollaData

class PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodsItem(TypedDict):
	__typename: str
	billingEmail: Optional[NoneType]
	billingUsername: Optional[NoneType]
	cardType: Optional[NoneType]
	chargeInstrumentID: Optional[str]
	expirationMonth: Optional[NoneType]
	expirationYear: Optional[NoneType]
	extMethodID: Optional[str]
	lastFour: Optional[NoneType]
	paymentScheme: Optional[NoneType]
	paymentType: str
	provider: str
	purchaseProfiles: List[Any]
	recurringPaymentDetails: List[Any]

class PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserData(TypedDict):
	__typename: str
	displayName: str
	email: str
	id: str
	login: str
	paymentMethodConfigs: PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodconfigsData
	paymentMethods: List[PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserDataPaymentmethodsItem]
	profileImageURL: str
	residence: Optional[NoneType]

class PaymentMethodsTab_UserPaymentMethodsResponsePaymentpastduestatusesItem(TypedDict):
	__typename: str
	isInDunning: Optional[bool]
	vendor: str

class PaymentMethodsTab_UserPaymentMethodsResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class PaymentMethodsTab_UserPaymentMethodsResponse(TypedDict):
	currentUser: PaymentMethodsTab_UserPaymentMethodsResponseCurrentuserData
	paymentPastDueStatuses: List[PaymentMethodsTab_UserPaymentMethodsResponsePaymentpastduestatusesItem]
	requestInfo: PaymentMethodsTab_UserPaymentMethodsResponseRequestinfoData

class SubscriptionsManagement_ExpiredSubscriptionsRequest(TypedDict):
	limit: int
	cursor: Optional[str]

class SubscriptionsManagement_ExpiredSubscriptionsResponseCurrentuserDataExpiredsubscriptionsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]
	hasPreviousPage: Optional[bool]

class SubscriptionsManagement_ExpiredSubscriptionsResponseCurrentuserDataExpiredsubscriptionsData(TypedDict):
	__typename: str
	edges: List[Any]
	pageInfo: SubscriptionsManagement_ExpiredSubscriptionsResponseCurrentuserDataExpiredsubscriptionsDataPageinfoData

class SubscriptionsManagement_ExpiredSubscriptionsResponseCurrentuserData(TypedDict):
	__typename: str
	expiredSubscriptions: SubscriptionsManagement_ExpiredSubscriptionsResponseCurrentuserDataExpiredsubscriptionsData
	id: str

class SubscriptionsManagement_ExpiredSubscriptionsResponseMoneybannernotificationsItem(TypedDict):
	__typename: str
	id: str
	location: str
	metadata: Optional[NoneType]
	position: str
	priority: int

class SubscriptionsManagement_ExpiredSubscriptionsResponse(TypedDict):
	currentUser: SubscriptionsManagement_ExpiredSubscriptionsResponseCurrentuserData
	moneyBannerNotifications: List[SubscriptionsManagement_ExpiredSubscriptionsResponseMoneybannernotificationsItem]

class WalletBalancesRequest(TypedDict):
	bestGuessCountryCode: str

class WalletBalancesResponseCurrentuserDataSubscriptiontokenData(TypedDict):
	__typename: str
	balance: Optional[int]

class WalletBalancesResponseCurrentuserDataWalletbalancesDataAllbalancesItem(TypedDict):
	__typename: str
	amount: Optional[int]
	currency: str
	expiresAt: Optional[NoneType]
	exponent: int

class WalletBalancesResponseCurrentuserDataWalletbalancesData(TypedDict):
	__typename: str
	allBalances: List[WalletBalancesResponseCurrentuserDataWalletbalancesDataAllbalancesItem]
	eligibleCurrencies: List[str]

class WalletBalancesResponseCurrentuserData(TypedDict):
	__typename: str
	id: str
	subscriptionToken: WalletBalancesResponseCurrentuserDataSubscriptiontokenData
	walletBalances: WalletBalancesResponseCurrentuserDataWalletbalancesData

class WalletBalancesResponse(TypedDict):
	currentUser: WalletBalancesResponseCurrentuserData

class ChannelFollowsRequest(TypedDict):
	limit: int
	order: str

class ChannelFollowsResponseUserDataFollowsDataEdgesItemNodeDataSelfDataFollowerData(TypedDict):
	__typename: str
	disableNotifications: Optional[bool]
	followedAt: str

class ChannelFollowsResponseUserDataFollowsDataEdgesItemNodeDataSelfData(TypedDict):
	__typename: str
	canFollow: Optional[bool]
	follower: ChannelFollowsResponseUserDataFollowsDataEdgesItemNodeDataSelfDataFollowerData

class ChannelFollowsResponseUserDataFollowsDataEdgesItemNodeData(TypedDict):
	__typename: str
	bannerImageURL: str
	displayName: str
	id: str
	login: str
	profileImageURL: str
	self: ChannelFollowsResponseUserDataFollowsDataEdgesItemNodeDataSelfData

class ChannelFollowsResponseUserDataFollowsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: ChannelFollowsResponseUserDataFollowsDataEdgesItemNodeData

class ChannelFollowsResponseUserDataFollowsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class ChannelFollowsResponseUserDataFollowsData(TypedDict):
	__typename: str
	edges: List[ChannelFollowsResponseUserDataFollowsDataEdgesItem]
	pageInfo: ChannelFollowsResponseUserDataFollowsDataPageinfoData

class ChannelFollowsResponseUserData(TypedDict):
	__typename: str
	follows: ChannelFollowsResponseUserDataFollowsData
	id: str

class ChannelFollowsResponse(TypedDict):
	user: ChannelFollowsResponseUserData

class UserEmotesRequest(TypedDict):
	withOwner: Optional[bool]

class UserEmotesResponseCurrentuserDataEmotesetsItemEmotesItem(TypedDict):
	__typename: str
	id: str
	modifiers: Optional[NoneType]
	setID: str
	token: str
	type: str

class UserEmotesResponseCurrentuserDataEmotesetsItem(TypedDict):
	__typename: str
	emotes: List[UserEmotesResponseCurrentuserDataEmotesetsItemEmotesItem]
	id: str
	owner: Optional[NoneType]

class UserEmotesResponseCurrentuserData(TypedDict):
	__typename: str
	emoteSets: List[UserEmotesResponseCurrentuserDataEmotesetsItem]
	id: str

class UserEmotesResponse(TypedDict):
	currentUser: UserEmotesResponseCurrentuserData

class Whispers_Thread_WhisperThreadRequest1(TypedDict):
	id: str

class Whispers_Thread_WhisperThreadRequest2(TypedDict):
	id: str
	cursor: Optional[str]

class Whispers_Thread_WhisperThreadResponseWhisperthreadDataMessagesData(TypedDict):
	__typename: str
	edges: List[Any]

class Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItemDisplaybadgesItem(TypedDict):
	__typename: str
	id: str
	imageURL: str
	title: str

class Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItemSelfDataWhisperpermissionsData(TypedDict):
	__typename: str
	isStrangerBlocked: Optional[bool]
	receive: str

class Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItemSelfData(TypedDict):
	__typename: str
	whisperPermissions: Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItemSelfDataWhisperpermissionsData

class Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItem(TypedDict):
	__typename: str
	chatColor: Optional[NoneType]
	displayBadges: List[Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItemDisplaybadgesItem]
	displayName: str
	id: str
	login: str
	profileImageURL: str
	self: Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItemSelfData

class Whispers_Thread_WhisperThreadResponseWhisperthreadDataSpaminfoData(TypedDict):
	__typename: str
	lastMarkedNotSpamAt: Optional[NoneType]
	likelihood: str

class Whispers_Thread_WhisperThreadResponseWhisperthreadData(TypedDict):
	__typename: str
	id: str
	isArchived: Optional[bool]
	isMuted: Optional[bool]
	messages: Whispers_Thread_WhisperThreadResponseWhisperthreadDataMessagesData
	participants: List[Whispers_Thread_WhisperThreadResponseWhisperthreadDataParticipantsItem]
	spamInfo: Whispers_Thread_WhisperThreadResponseWhisperthreadDataSpaminfoData
	unreadMessagesCount: Optional[int]
	userLastMessageRead: Optional[NoneType]

class Whispers_Thread_WhisperThreadResponseCurrentuserData(TypedDict):
	__typename: str
	blockedUsers: List[Any]
	chatColor: Optional[NoneType]
	displayBadges: List[Any]
	displayName: str
	id: str
	isEmailVerified: Optional[bool]
	login: str
	profileImageURL: str

class Whispers_Thread_WhisperThreadResponse(TypedDict):
	whisperThread: Whispers_Thread_WhisperThreadResponseWhisperthreadData
	currentUser: Whispers_Thread_WhisperThreadResponseCurrentuserData

class Whispers_Thread_User_ActivityRequest(TypedDict):
	targetUserID: str

class Whispers_Thread_User_ActivityResponseUserDataDisplaybadgesItem(TypedDict):
	__typename: str
	id: str
	imageURL: str
	title: str

class Whispers_Thread_User_ActivityResponseUserData(TypedDict):
	__typename: str
	chatColor: Optional[NoneType]
	displayBadges: List[Whispers_Thread_User_ActivityResponseUserDataDisplaybadgesItem]
	displayName: str
	id: str
	login: str
	profileImageURL: str

class Whispers_Thread_User_ActivityResponse(TypedDict):
	user: Whispers_Thread_User_ActivityResponseUserData

class VideoPlayer_MutedSegmentsAlertOverlayRequest(TypedDict):
	includePrivate: Optional[bool]
	vodID: str

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesItem(TypedDict):
	__typename: str
	duration: int
	offset: int

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionData(TypedDict):
	__typename: str
	nodes: List[VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionDataNodesItem]

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoData(TypedDict):
	__typename: str
	mutedSegmentConnection: VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoDataMutedsegmentconnectionData

class VideoPlayer_MutedSegmentsAlertOverlayResponseVideoData(TypedDict):
	__typename: str
	id: str
	muteInfo: VideoPlayer_MutedSegmentsAlertOverlayResponseVideoDataMuteinfoData

class VideoPlayer_MutedSegmentsAlertOverlayResponse(TypedDict):
	video: VideoPlayer_MutedSegmentsAlertOverlayResponseVideoData

class CollectionCarouselQueryRequest(TypedDict):
	includePreviewBlur: Optional[bool]
	collectionID: str
	first: int

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataOwnerDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataOwnerDataRolesData

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataSelfDataViewinghistoryData(TypedDict):
	__typename: str
	position: Optional[NoneType]
	updatedAt: Optional[NoneType]

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataSelfData(TypedDict):
	__typename: str
	isRestricted: Optional[bool]
	viewingHistory: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataSelfDataViewinghistoryData

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeData(TypedDict):
	__typename: str
	animatedPreviewURL: str
	contentTags: List[Any]
	game: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataGameData
	id: str
	lengthSeconds: int
	owner: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataOwnerData
	previewThumbnailURL: str
	publishedAt: str
	resourceRestriction: Optional[NoneType]
	self: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeDataSelfData
	title: str
	viewCount: int

class CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItemNodeData

class CollectionCarouselQueryResponseCollectionDataItemsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class CollectionCarouselQueryResponseCollectionDataItemsData(TypedDict):
	__typename: str
	edges: List[CollectionCarouselQueryResponseCollectionDataItemsDataEdgesItem]
	pageInfo: CollectionCarouselQueryResponseCollectionDataItemsDataPageinfoData
	totalCount: int

class CollectionCarouselQueryResponseCollectionDataOwnerData(TypedDict):
	__typename: str
	id: str
	login: str

class CollectionCarouselQueryResponseCollectionData(TypedDict):
	__typename: str
	description: Optional[str]
	id: str
	items: CollectionCarouselQueryResponseCollectionDataItemsData
	lengthSeconds: int
	owner: CollectionCarouselQueryResponseCollectionDataOwnerData
	thumbnailURL: str
	title: str
	type: str
	updatedAt: str

class CollectionCarouselQueryResponse(TypedDict):
	collection: CollectionCarouselQueryResponseCollectionData

class ClipMetadataBroadcastInfoQueryRequest(TypedDict):
	channelLogin: str

class ClipMetadataBroadcastInfoQueryResponseUserDataBroadcastsettingsDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str

class ClipMetadataBroadcastInfoQueryResponseUserDataBroadcastsettingsData(TypedDict):
	__typename: str
	game: ClipMetadataBroadcastInfoQueryResponseUserDataBroadcastsettingsDataGameData
	id: str

class ClipMetadataBroadcastInfoQueryResponseUserData(TypedDict):
	__typename: str
	broadcastSettings: ClipMetadataBroadcastInfoQueryResponseUserDataBroadcastsettingsData
	displayName: str
	id: str
	profileImageURL: str

class ClipMetadataBroadcastInfoQueryResponse(TypedDict):
	user: ClipMetadataBroadcastInfoQueryResponseUserData

class CreateRawMediaRequestInputData(TypedDict):
	broadcastID: str
	offsetSeconds: int
	vodID: Optional[NoneType]

class CreateRawMediaRequest(TypedDict):
	input: CreateRawMediaRequestInputData

class CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData(TypedDict):
	__typename: str
	xPercentage: float
	yPercentage: int

class CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData(TypedDict):
	__typename: str
	xPercentage: float
	yPercentage: Optional[int]

class CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData(TypedDict):
	__typename: str
	bottomRight: CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData
	topLeft: CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData

class CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataData(TypedDict):
	__typename: str
	mainFrame: CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData

class CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingData(TypedDict):
	__typename: str
	fullTemplateMetadata: CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingDataFulltemplatemetadataData
	portraitClipLayout: str
	stackedTemplateMetadata: Optional[NoneType]

class CreateRawMediaResponseCreaterawmediaDataRawmediaData(TypedDict):
	__typename: str
	aspectRatio: Optional[NoneType]
	id: str
	renditions: Optional[NoneType]
	status: str
	suggestedCropping: CreateRawMediaResponseCreaterawmediaDataRawmediaDataSuggestedcroppingData

class CreateRawMediaResponseCreaterawmediaData(TypedDict):
	__typename: str
	error: Optional[NoneType]
	rawMedia: CreateRawMediaResponseCreaterawmediaDataRawmediaData

class CreateRawMediaResponse(TypedDict):
	createRawMedia: CreateRawMediaResponseCreaterawmediaData

class GetRawMediaRequest(TypedDict):
	id: str

class GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData(TypedDict):
	__typename: str
	xPercentage: float
	yPercentage: int

class GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData(TypedDict):
	__typename: str
	xPercentage: float
	yPercentage: Optional[int]

class GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData(TypedDict):
	__typename: str
	bottomRight: GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataBottomrightData
	topLeft: GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeDataTopleftData

class GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataData(TypedDict):
	__typename: str
	mainFrame: GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataDataMainframeData

class GetRawMediaResponseRawmediaDataSuggestedcroppingData(TypedDict):
	__typename: str
	fullTemplateMetadata: GetRawMediaResponseRawmediaDataSuggestedcroppingDataFulltemplatemetadataData
	portraitClipLayout: str
	stackedTemplateMetadata: Optional[NoneType]

class GetRawMediaResponseRawmediaData(TypedDict):
	__typename: str
	aspectRatio: Optional[NoneType]
	id: str
	renditions: Optional[NoneType]
	status: str
	suggestedCropping: GetRawMediaResponseRawmediaDataSuggestedcroppingData

class GetRawMediaResponse(TypedDict):
	rawMedia: GetRawMediaResponseRawmediaData

class AccessIsChannelEditorQueryRequest(TypedDict):
	channelLogin: str

class AccessIsChannelEditorQueryResponseChannelDataSelfData(TypedDict):
	__typename: str
	isEditor: Optional[bool]

class AccessIsChannelEditorQueryResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: AccessIsChannelEditorQueryResponseChannelDataSelfData

class AccessIsChannelEditorQueryResponse(TypedDict):
	channel: AccessIsChannelEditorQueryResponseChannelData

class AccessIsChannelModeratorQueryRequest(TypedDict):
	channelLogin: str

class AccessIsChannelModeratorQueryResponseChannelDataSelfData(TypedDict):
	__typename: str
	isModerator: Optional[bool]

class AccessIsChannelModeratorQueryResponseChannelData(TypedDict):
	__typename: str
	id: str
	self: AccessIsChannelModeratorQueryResponseChannelDataSelfData

class AccessIsChannelModeratorQueryResponse(TypedDict):
	channel: AccessIsChannelModeratorQueryResponseChannelData

class ReportMenuItemRequest(TypedDict):
	channelID: str

class ReportMenuItemResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class ReportMenuItemResponseUserDataStreamData(TypedDict):
	__typename: str
	createdAt: str
	id: str

class ReportMenuItemResponseUserData(TypedDict):
	__typename: str
	id: str
	stream: ReportMenuItemResponseUserDataStreamData

class ReportMenuItemResponse(TypedDict):
	requestInfo: ReportMenuItemResponseRequestinfoData
	user: ReportMenuItemResponseUserData

class ReportUserModal_ReportWizardDataRequest(TypedDict):
	targetUserID: str
	content: str
	reportSessionID: str
	reportWizardVersion: str

class ReportUserModal_ReportWizardDataResponseTargetuserData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ReportUserModal_ReportWizardDataResponseCurrentuserData(TypedDict):
	__typename: str
	blockedUsers: List[Any]
	email: str
	id: str
	login: str

class ReportUserModal_ReportWizardDataResponseRequestinfoData(TypedDict):
	__typename: str
	countryCode: str

class ReportUserModal_ReportWizardDataResponseReportwizardDataReasonsDataTosandcountryreasonsItem(TypedDict):
	__typename: str
	deadEndType: str
	description: str
	detailedReasons: Optional[NoneType]
	id: str
	isApplicableToCountryRegulations: Optional[bool]
	text: str

class ReportUserModal_ReportWizardDataResponseReportwizardDataReasonsData(TypedDict):
	__typename: str
	countryCode: str
	disclosureText: Optional[NoneType]
	id: str
	toSAndCountryReasons: List[ReportUserModal_ReportWizardDataResponseReportwizardDataReasonsDataTosandcountryreasonsItem]

class ReportUserModal_ReportWizardDataResponseReportwizardDataReportablecontentItemApplicablereasonsItemReportreasonData(TypedDict):
	__typename: str
	id: str

class ReportUserModal_ReportWizardDataResponseReportwizardDataReportablecontentItemApplicablereasonsItem(TypedDict):
	__typename: str
	id: str
	reportReason: ReportUserModal_ReportWizardDataResponseReportwizardDataReportablecontentItemApplicablereasonsItemReportreasonData
	visibility: str

class ReportUserModal_ReportWizardDataResponseReportwizardDataReportablecontentItem(TypedDict):
	__typename: str
	applicableReasons: List[ReportUserModal_ReportWizardDataResponseReportwizardDataReportablecontentItemApplicablereasonsItem]
	deadEndType: str
	id: str
	type: str

class ReportUserModal_ReportWizardDataResponseReportwizardData(TypedDict):
	__typename: str
	reasons: ReportUserModal_ReportWizardDataResponseReportwizardDataReasonsData
	reportableContent: List[ReportUserModal_ReportWizardDataResponseReportwizardDataReportablecontentItem]

class ReportUserModal_ReportWizardDataResponse(TypedDict):
	targetUser: ReportUserModal_ReportWizardDataResponseTargetuserData
	currentUser: ReportUserModal_ReportWizardDataResponseCurrentuserData
	requestInfo: ReportUserModal_ReportWizardDataResponseRequestinfoData
	reportWizard: ReportUserModal_ReportWizardDataResponseReportwizardData

class CategoryChannels_InternationalSectionRequestOptionsDataRecommendationscontextData(TypedDict):
	platform: str

class CategoryChannels_InternationalSectionRequestOptionsData(TypedDict):
	broadcasterLanguages: List[str]
	recommendationsContext: CategoryChannels_InternationalSectionRequestOptionsDataRecommendationscontextData
	sort: str

class CategoryChannels_InternationalSectionRequest(TypedDict):
	imageWidth: int
	limit: int
	slug: str
	options: CategoryChannels_InternationalSectionRequestOptionsData
	sortTypeIsRecency: Optional[bool]
	includeIsDJ: Optional[bool]

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: Optional[NoneType]
	profileImageURL: str
	roles: CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataBroadcasterDataRolesData

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataBroadcasterData
	freeformTags: List[CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataFreeformtagsItem]
	game: CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataGameData
	id: str
	previewImageURL: str
	previewThumbnailProperties: CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	title: str
	type: str
	viewersCount: int

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItemNodeData
	trackingID: Optional[NoneType]

class CategoryChannels_InternationalSectionResponseGameDataStreamsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class CategoryChannels_InternationalSectionResponseGameDataStreamsData(TypedDict):
	__typename: str
	edges: List[CategoryChannels_InternationalSectionResponseGameDataStreamsDataEdgesItem]
	pageInfo: CategoryChannels_InternationalSectionResponseGameDataStreamsDataPageinfoData

class CategoryChannels_InternationalSectionResponseGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	streams: CategoryChannels_InternationalSectionResponseGameDataStreamsData

class CategoryChannels_InternationalSectionResponse(TypedDict):
	game: CategoryChannels_InternationalSectionResponseGameData

class UpcomingScheduleRequestOptionsData(TypedDict):
	scheduleType: str
	utcOffsetMinutes: int

class UpcomingScheduleRequest(TypedDict):
	options: UpcomingScheduleRequestOptionsData
	categoryID: str

class UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelDataOwnerData(TypedDict):
	__typename: str
	bannerImageURL: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	tags: List[Any]

class UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelData(TypedDict):
	__typename: str
	id: str
	name: str
	owner: UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelDataOwnerData
	stream: Optional[NoneType]

class UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItemSegmentData(TypedDict):
	__typename: str
	baseSegmentID: str
	channel: UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelData
	endAt: Optional[NoneType]
	hasReminder: Optional[bool]
	id: str
	isCancelled: Optional[bool]
	repeatEndsAfterCount: int
	startAt: str
	title: str

class UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItem(TypedDict):
	__typename: str
	id: str
	reminderCount: int
	segment: UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItemSegmentData

class UpcomingScheduleResponseFeaturedupcomingstreamsData(TypedDict):
	__typename: str
	nodes: List[UpcomingScheduleResponseFeaturedupcomingstreamsDataNodesItem]

class UpcomingScheduleResponse(TypedDict):
	featuredUpcomingStreams: UpcomingScheduleResponseFeaturedupcomingstreamsData

class FeaturedUpcomingStreamsRequestOptionsData(TypedDict):
	scheduleType: str
	utcOffsetMinutes: int

class FeaturedUpcomingStreamsRequest(TypedDict):
	options: FeaturedUpcomingStreamsRequestOptionsData
	categoryID: str

class FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelDataOwnerData(TypedDict):
	__typename: str
	bannerImageURL: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	tags: List[Any]

class FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelData(TypedDict):
	__typename: str
	id: str
	name: str
	owner: FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelDataOwnerData
	stream: Optional[NoneType]

class FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItemSegmentData(TypedDict):
	__typename: str
	baseSegmentID: str
	channel: FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItemSegmentDataChannelData
	endAt: Optional[NoneType]
	hasReminder: Optional[bool]
	id: str
	isCancelled: Optional[bool]
	repeatEndsAfterCount: int
	startAt: str
	title: str

class FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItem(TypedDict):
	__typename: str
	id: str
	reminderCount: int
	segment: FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItemSegmentData

class FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsData(TypedDict):
	__typename: str
	nodes: List[FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsDataNodesItem]

class FeaturedUpcomingStreamsResponse(TypedDict):
	featuredUpcomingStreams: FeaturedUpcomingStreamsResponseFeaturedupcomingstreamsData

class ChannelVideoCoreRequest(TypedDict):
	videoID: str

class ChannelVideoCoreResponseVideoDataOwnerDataChannelDataSelfData(TypedDict):
	__typename: str
	isAuthorized: Optional[bool]
	restrictionType: Optional[NoneType]

class ChannelVideoCoreResponseVideoDataOwnerDataChannelDataTrailerData(TypedDict):
	__typename: str
	video: Optional[NoneType]

class ChannelVideoCoreResponseVideoDataOwnerDataChannelData(TypedDict):
	__typename: str
	id: str
	self: ChannelVideoCoreResponseVideoDataOwnerDataChannelDataSelfData
	trailer: ChannelVideoCoreResponseVideoDataOwnerDataChannelDataTrailerData

class ChannelVideoCoreResponseVideoDataOwnerData(TypedDict):
	__typename: str
	channel: ChannelVideoCoreResponseVideoDataOwnerDataChannelData
	displayName: str
	id: str
	login: str
	primaryColorHex: Optional[NoneType]
	profileImageURL: str
	stream: Optional[NoneType]

class ChannelVideoCoreResponseVideoData(TypedDict):
	__typename: str
	id: str
	owner: ChannelVideoCoreResponseVideoDataOwnerData

class ChannelVideoCoreResponse(TypedDict):
	video: ChannelVideoCoreResponseVideoData

class ChatSettings_BadgesRequest(TypedDict):
	channelLogin: str

class ChatSettings_BadgesResponseCurrentuserDataAvailablebadgesItem(TypedDict):
	__typename: str
	clickAction: Optional[NoneType]
	clickURL: Optional[NoneType]
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class ChatSettings_BadgesResponseCurrentuserDataSubscriptionsettingsData(TypedDict):
	__typename: str
	isBadgeModifierHidden: Optional[bool]

class ChatSettings_BadgesResponseCurrentuserData(TypedDict):
	__typename: str
	availableBadges: List[ChatSettings_BadgesResponseCurrentuserDataAvailablebadgesItem]
	hasPrime: Optional[bool]
	hasTurbo: Optional[bool]
	id: str
	selectedBadge: Optional[NoneType]
	subscriptionSettings: ChatSettings_BadgesResponseCurrentuserDataSubscriptionsettingsData

class ChatSettings_BadgesResponseUserDataSelfDataAvailablebadgesItem(TypedDict):
	__typename: str
	clickAction: Optional[NoneType]
	clickURL: Optional[NoneType]
	id: str
	image1x: str
	image2x: str
	image4x: str
	setID: str
	title: str
	version: str

class ChatSettings_BadgesResponseUserDataSelfDataSubscriptiontenureData(TypedDict):
	__typename: str
	months: Optional[int]

class ChatSettings_BadgesResponseUserDataSelfData(TypedDict):
	__typename: str
	availableBadges: List[ChatSettings_BadgesResponseUserDataSelfDataAvailablebadgesItem]
	selectedBadge: Optional[NoneType]
	subscriptionBenefit: Optional[NoneType]
	subscriptionTenure: ChatSettings_BadgesResponseUserDataSelfDataSubscriptiontenureData

class ChatSettings_BadgesResponseUserDataSubscriptionproductsItem(TypedDict):
	__typename: str
	displayName: str
	id: str

class ChatSettings_BadgesResponseUserData(TypedDict):
	__typename: str
	id: str
	self: ChatSettings_BadgesResponseUserDataSelfData
	subscriptionProducts: List[ChatSettings_BadgesResponseUserDataSubscriptionproductsItem]

class ChatSettings_BadgesResponse(TypedDict):
	currentUser: ChatSettings_BadgesResponseCurrentuserData
	user: ChatSettings_BadgesResponseUserData

class BrowsePage_PopularRequestOptionsDataRecommendationscontextData(TypedDict):
	platform: str

class BrowsePage_PopularRequestOptionsData(TypedDict):
	broadcasterLanguages: List[Any]
	freeformTags: List[str]
	includeRestricted: List[str]
	recommendationsContext: BrowsePage_PopularRequestOptionsDataRecommendationscontextData
	requestID: str
	sort: str
	tags: List[Any]

class BrowsePage_PopularRequest(TypedDict):
	imageWidth: int
	limit: int
	platformType: str
	options: BrowsePage_PopularRequestOptionsData
	sortTypeIsRecency: Optional[bool]
	includeIsDJ: Optional[bool]

class BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isParticipatingDJ: Optional[bool]
	isPartner: Optional[bool]

class BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataBroadcasterDataRolesData

class BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataFreeformtagsItem(TypedDict):
	__typename: str
	id: str
	name: str

class BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	displayName: str
	id: str
	name: str
	slug: str

class BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class BrowsePage_PopularResponseStreamsDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataBroadcasterData
	freeformTags: List[BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataFreeformtagsItem]
	game: BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataGameData
	id: str
	previewImageURL: str
	previewThumbnailProperties: BrowsePage_PopularResponseStreamsDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	title: str
	type: str
	viewersCount: int

class BrowsePage_PopularResponseStreamsDataEdgesItem(TypedDict):
	__typename: str
	cursor: str
	node: BrowsePage_PopularResponseStreamsDataEdgesItemNodeData
	trackingID: Optional[NoneType]

class BrowsePage_PopularResponseStreamsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class BrowsePage_PopularResponseStreamsData(TypedDict):
	__typename: str
	edges: List[BrowsePage_PopularResponseStreamsDataEdgesItem]
	pageInfo: BrowsePage_PopularResponseStreamsDataPageinfoData

class BrowsePage_PopularResponse(TypedDict):
	streams: BrowsePage_PopularResponseStreamsData

class ClipsCards__GameRequestCriteriaData(TypedDict):
	filter: str
	languages: List[Any]
	shouldFilterByDiscoverySetting: Optional[bool]

class ClipsCards__GameRequest(TypedDict):
	categorySlug: str
	limit: int
	criteria: ClipsCards__GameRequestCriteriaData
	cursor: Optional[NoneType]

class ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataBroadcasterDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataBroadcasterData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str
	primaryColorHex: str
	profileImageURL: str
	roles: ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataBroadcasterDataRolesData

class ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataCuratorData(TypedDict):
	__typename: str
	displayName: str
	id: str
	login: str

class ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataGameData(TypedDict):
	__typename: str
	boxArtURL: str
	id: str
	name: str
	slug: str

class ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataGueststarparticipantsData(TypedDict):
	__typename: str
	guests: List[Any]
	sessionIdentifier: str

class ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataPreviewthumbnailpropertiesData(TypedDict):
	__typename: str
	blurReason: str

class ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeData(TypedDict):
	__typename: str
	broadcaster: ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataBroadcasterData
	createdAt: str
	curator: ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataCuratorData
	durationSeconds: int
	game: ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataGameData
	guestStarParticipants: ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataGueststarparticipantsData
	id: str
	isFeatured: Optional[bool]
	previewThumbnailProperties: ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeDataPreviewthumbnailpropertiesData
	slug: str
	thumbnailURL: str
	title: str
	viewCount: int

class ClipsCards__GameResponseGameDataClipsDataEdgesItem(TypedDict):
	__typename: str
	cursor: Optional[NoneType]
	node: ClipsCards__GameResponseGameDataClipsDataEdgesItemNodeData

class ClipsCards__GameResponseGameDataClipsDataPageinfoData(TypedDict):
	__typename: str
	hasNextPage: Optional[bool]

class ClipsCards__GameResponseGameDataClipsData(TypedDict):
	__typename: str
	banners: Optional[NoneType]
	edges: List[ClipsCards__GameResponseGameDataClipsDataEdgesItem]
	pageInfo: ClipsCards__GameResponseGameDataClipsDataPageinfoData

class ClipsCards__GameResponseGameData(TypedDict):
	__typename: str
	clips: ClipsCards__GameResponseGameDataClipsData
	displayName: str
	id: str
	name: str

class ClipsCards__GameResponse(TypedDict):
	game: ClipsCards__GameResponseGameData

class VideoPlayerStreamInfoOverlayChannelRequest(TypedDict):
	channel: str

class VideoPlayerStreamInfoOverlayChannelResponseUserDataBroadcastsettingsDataGameData(TypedDict):
	__typename: str
	displayName: str
	id: str
	name: str
	slug: str

class VideoPlayerStreamInfoOverlayChannelResponseUserDataBroadcastsettingsData(TypedDict):
	__typename: str
	game: VideoPlayerStreamInfoOverlayChannelResponseUserDataBroadcastsettingsDataGameData
	id: str
	title: str

class VideoPlayerStreamInfoOverlayChannelResponseUserDataRolesData(TypedDict):
	__typename: str
	isPartner: Optional[bool]

class VideoPlayerStreamInfoOverlayChannelResponseUserDataStreamData(TypedDict):
	__typename: str
	id: str
	tags: List[Any]
	viewersCount: int

class VideoPlayerStreamInfoOverlayChannelResponseUserData(TypedDict):
	__typename: str
	broadcastSettings: VideoPlayerStreamInfoOverlayChannelResponseUserDataBroadcastsettingsData
	displayName: str
	id: str
	login: str
	profileImageURL: str
	profileURL: str
	roles: VideoPlayerStreamInfoOverlayChannelResponseUserDataRolesData
	stream: VideoPlayerStreamInfoOverlayChannelResponseUserDataStreamData

class VideoPlayerStreamInfoOverlayChannelResponse(TypedDict):
	user: VideoPlayerStreamInfoOverlayChannelResponseUserData

class ExtensionsNotificationBitsBalanceRequest(TypedDict):
	...

class ExtensionsNotificationBitsBalanceResponseCurrentuserData(TypedDict):
	__typename: str
	bitsBalance: Optional[int]
	id: str

class ExtensionsNotificationBitsBalanceResponse(TypedDict):
	currentUser: ExtensionsNotificationBitsBalanceResponseCurrentuserData

class SubscribedContextRequest(TypedDict):
	login: str

class SubscribedContextResponseUserDataSelfData(TypedDict):
	__typename: str
	subscriptionBenefit: Optional[NoneType]

class SubscribedContextResponseUserData(TypedDict):
	__typename: str
	id: str
	self: SubscribedContextResponseUserDataSelfData

class SubscribedContextResponse(TypedDict):
	user: SubscribedContextResponseUserData

class ClientSideAdEventHandling_RecordAdEventRequestInputData(TypedDict):
	eventName: str
	eventPayload: str
	radToken: str

class ClientSideAdEventHandling_RecordAdEventRequest(TypedDict):
	input: ClientSideAdEventHandling_RecordAdEventRequestInputData

class ClientSideAdEventHandling_RecordAdEventResponseRecordadeventData(TypedDict):
	__typename: str
	error: Optional[NoneType]

class ClientSideAdEventHandling_RecordAdEventResponse(TypedDict):
	recordAdEvent: ClientSideAdEventHandling_RecordAdEventResponseRecordadeventData

class VideoPlayerVODPostplayRecommendationsRequest(TypedDict):
	videoID: str

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosData(TypedDict):
	__typename: str
	edges: List[Any]

class VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerData(TypedDict):
	__typename: str
	displayName: str
	id: str
	videos: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerDataVideosData

class VideoPlayerVODPostplayRecommendationsResponseVideoData(TypedDict):
	__typename: str
	id: str
	owner: VideoPlayerVODPostplayRecommendationsResponseVideoDataOwnerData

class VideoPlayerVODPostplayRecommendationsResponse(TypedDict):
	video: VideoPlayerVODPostplayRecommendationsResponseVideoData

class Consent(Endpoint):
	sha256Hash = '012157dd34a0fb2f401124cd5a66b3f333a6ea572f75ba0db91a69bae0c3bd13'
	operation_name = 'Consent'
	def build_query(self, variables: ConsentRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Ads_Components_AdManager_User(Endpoint):
	sha256Hash = '1fd9eeac7ab98004ee00dc6554e88759f1fa66ea94b97487f69b1ddf3a9d215b'
	operation_name = 'Ads_Components_AdManager_User'
	def build_query(self, variables: Ads_Components_AdManager_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Prime_PrimeOffers_CurrentUser(Endpoint):
	sha256Hash = 'a773b7efefe390d49753520f7db73d03794b008af6acc22c06a2c630d46d5518'
	operation_name = 'Prime_PrimeOffers_CurrentUser'
	def build_query(self, variables: Prime_PrimeOffers_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UserMenuCurrentUser(Endpoint):
	sha256Hash = '3cff634f43c5c78830907a662b315b1847cfc0dce32e6a9752e7f5d70b37f8c0'
	operation_name = 'UserMenuCurrentUser'
	def build_query(self, variables: UserMenuCurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class TopNav_CurrentUser(Endpoint):
	sha256Hash = 'a31dd0def64bc249bfa6d1c614b5977771de7d15b88bceae382cd14424bed4af'
	operation_name = 'TopNav_CurrentUser'
	def build_query(self, variables: TopNav_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StoryPreviewsWithOrder(Endpoint):
	sha256Hash = '122290ddd34892464b89fd76f2bdd75d9aa3408342bdd7b3439b3e7295d92299'
	operation_name = 'StoryPreviewsWithOrder'
	def build_query(self, variables: StoryPreviewsWithOrderRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SideNav(Endpoint):
	sha256Hash = 'b235e7c084bc768d827343cda0b95310535a0956d449e574885b00e176fe5f27'
	operation_name = 'SideNav'
	def build_query(self, variables: SideNavRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FrontPageNew_User(Endpoint):
	sha256Hash = '64bd07a2cbaca80699d62636d966cf6395a5d14a1f0a14282067dcb28b13eb11'
	operation_name = 'FrontPageNew_User'
	def build_query(self, variables: FrontPageNew_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Shelves(Endpoint):
	sha256Hash = 'c04cbfe9d604367b6ea4ea3fe4c9695046561ef44c9af2af3e0e3c0c20f563b1'
	operation_name = 'Shelves'
	def build_query(self, variables: Union[ShelvesRequest1, ShelvesRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PrefetchPlaybackAccessToken(Endpoint):
	sha256Hash = 'c101f277c6ab7de34f64e63c90d698edae0d83ed5fad8efe198596b472ef3337'
	operation_name = 'PrefetchPlaybackAccessToken'
	def build_query(self, variables: PrefetchPlaybackAccessTokenRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestStarBatchCollaborationQuery(Endpoint):
	sha256Hash = '096d50357df5e938f4fa83fe2acf25cb0f4886149aa81ddb9754eae98c05f2dd'
	operation_name = 'GuestStarBatchCollaborationQuery'
	def build_query(self, variables: GuestStarBatchCollaborationQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CoreActionsCurrentUser(Endpoint):
	sha256Hash = '6b5b63a013cf66a995d61f71a508ab5c8e4473350c5d4136f846ba65e8101e95'
	operation_name = 'CoreActionsCurrentUser'
	def build_query(self, variables: CoreActionsCurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FeaturedContentCarouselStreams(Endpoint):
	sha256Hash = '663a12a5bcf38aa3f6f566e328e9e7de44986746101c0ad10b50186f768b41b7'
	operation_name = 'FeaturedContentCarouselStreams'
	def build_query(self, variables: FeaturedContentCarouselStreamsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class TrackingManager_RequestInfo(Endpoint):
	sha256Hash = 'aacdbed250e409105d124ea697ad291a06864c9343067714559fa01230c4cf1b'
	operation_name = 'TrackingManager_RequestInfo'
	def build_query(self, variables: TrackingManager_RequestInfoRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Prime_PrimeOffers_PrimeOfferIds_Eligibility(Endpoint):
	sha256Hash = '04a2d0ee1efa76171275ce8a1f7a23509e2d696bd15c0b1238c5811239d98488'
	operation_name = 'Prime_PrimeOffers_PrimeOfferIds_Eligibility'
	def build_query(self, variables: Prime_PrimeOffers_PrimeOfferIds_EligibilityRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPage_SetSessionStatus(Endpoint):
	sha256Hash = '8521e08af74c8cb5128e4bb99fa53b591391cb19492e65fb0489aeee2f96947f'
	operation_name = 'ChannelPage_SetSessionStatus'
	def build_query(self, variables: ChannelPage_SetSessionStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Core_Services_Spade_CurrentUser(Endpoint):
	sha256Hash = '482be6fdcd0ff8e6a55192210e2ec6db8a67392f206021e81abe0347fc727ebe'
	operation_name = 'Core_Services_Spade_CurrentUser'
	def build_query(self, variables: Core_Services_Spade_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DMCAViolationCountBanner(Endpoint):
	sha256Hash = '64616ab82f723fb8677314c2e70c10a5317a37830005e595c10e0a5d5cbd7f56'
	operation_name = 'DMCAViolationCountBanner'
	def build_query(self, variables: DMCAViolationCountBannerRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VerifyEmail_CurrentUser(Endpoint):
	sha256Hash = 'f9e7dcdf7e99c314c82d8f7f725fab5f99d1df3d7359b53c9ae122deec590198'
	operation_name = 'VerifyEmail_CurrentUser'
	def build_query(self, variables: VerifyEmail_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OnsiteNotifications_Summary(Endpoint):
	sha256Hash = '4d07584aeb25d8fec753ea232935ab2c18ec2b85e80a6e4a5ef89d46cf9193b1'
	operation_name = 'OnsiteNotifications_Summary'
	def build_query(self, variables: OnsiteNotifications_SummaryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Whispers_Whispers_UserWhisperThreads(Endpoint):
	sha256Hash = '9d4bf15288a0b4d96492c97dafa17222aa000528adcad4f8d1652441d9132d62'
	operation_name = 'Whispers_Whispers_UserWhisperThreads'
	def build_query(self, variables: Union[Whispers_Whispers_UserWhisperThreadsRequest1, Whispers_Whispers_UserWhisperThreadsRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ConnectAdIdentityMutation(Endpoint):
	sha256Hash = 'aeb02ffde95392868a9da662631090526b891a2972620e6b6393873a39111564'
	operation_name = 'ConnectAdIdentityMutation'
	def build_query(self, variables: ConnectAdIdentityMutationRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPreviewOverlay(Endpoint):
	sha256Hash = '9515480dee68a77e667cb19de634739d33f243572b007e98e67184b1a5d8369f'
	operation_name = 'VideoPreviewOverlay'
	def build_query(self, variables: VideoPreviewOverlayRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoAdBanner(Endpoint):
	sha256Hash = '4d9da3e74d52b668ad9f163a641236f2c804e1129f717f2861b362310e6c64c7'
	operation_name = 'VideoAdBanner'
	def build_query(self, variables: VideoAdBannerRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ContentPolicyPropertiesQuery(Endpoint):
	sha256Hash = 'e2c1cb362a9b601440d764b2db98eaf4fc21b9091973b158c8b702716419545a'
	operation_name = 'ContentPolicyPropertiesQuery'
	def build_query(self, variables: ContentPolicyPropertiesQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetUserID(Endpoint):
	sha256Hash = 'bf6c594605caa0c63522f690156aa04bd434870bf963deb76668c381d16fcaa5'
	operation_name = 'GetUserID'
	def build_query(self, variables: GetUserIDRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_AgeGateOverlayBroadcaster(Endpoint):
	sha256Hash = 'ab175a77fb908cd5dfe25d6d23da0765b3fc187e3d3461d1c7b157c354e917ee'
	operation_name = 'VideoPlayer_AgeGateOverlayBroadcaster'
	def build_query(self, variables: VideoPlayer_AgeGateOverlayBroadcasterRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_VideoSourceManager(Endpoint):
	sha256Hash = 'f5e1b35d6f5a40348c6476fea36945d0931ba50621e1701b6c31252ee498cc3e'
	operation_name = 'VideoPlayer_VideoSourceManager'
	def build_query(self, variables: VideoPlayer_VideoSourceManagerRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerPixelAnalyticsUrls(Endpoint):
	sha256Hash = 'f3af1d5b492d70dc932de61226d764f61859ecebeaabc5ca6baf6125ded56021'
	operation_name = 'VideoPlayerPixelAnalyticsUrls'
	def build_query(self, variables: VideoPlayerPixelAnalyticsUrlsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamRefetchManager(Endpoint):
	sha256Hash = 'ecdcb724b0559d49689e6a32795e6a43bba4b2071b5e762a4d1edf2bb42a6789'
	operation_name = 'StreamRefetchManager'
	def build_query(self, variables: StreamRefetchManagerRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AdRequestHandling(Endpoint):
	sha256Hash = '61a5ecca6da3d924efa9dbde811e051b8a10cb6bd0fe22c372c2f4401f3e88d1'
	operation_name = 'AdRequestHandling'
	def build_query(self, variables: AdRequestHandlingRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class NielsenContentMetadata(Endpoint):
	sha256Hash = '2dbf505ee929438369e68e72319d1106bb3c142e295332fac157c90638968586'
	operation_name = 'NielsenContentMetadata'
	def build_query(self, variables: NielsenContentMetadataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelSkins(Endpoint):
	sha256Hash = 'b035de8611dc0bfbea6d0ce43af3f95319220fb5d23fc7a1448c16e1d83fed1c'
	operation_name = 'ChannelSkins'
	def build_query(self, variables: ChannelSkinsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ExtensionsUIContext_ChannelID(Endpoint):
	sha256Hash = 'aaa9870965b55ecb88e01a4d73b5427e8ff9397eea16b9adbd08cad86d3b9d25'
	operation_name = 'ExtensionsUIContext_ChannelID'
	def build_query(self, variables: ExtensionsUIContext_ChannelIDRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PlayerTrackingContextQuery(Endpoint):
	sha256Hash = '9d0ffcd1b007bbf4995f6be211ab78658e2fd6ce5978a335b78cbbb4d565a581'
	operation_name = 'PlayerTrackingContextQuery'
	def build_query(self, variables: Union[PlayerTrackingContextQueryRequest1, PlayerTrackingContextQueryRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ContentClassificationContext(Endpoint):
	sha256Hash = '57bb6c1aca3631b2b3e74b1c3c8adbecbbcc3becb70ec52d7c5ef0f90d7c3b02'
	operation_name = 'ContentClassificationContext'
	def build_query(self, variables: Union[ContentClassificationContextRequest1, ContentClassificationContextRequest2, ContentClassificationContextRequest3] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerStreamMetadata(Endpoint):
	sha256Hash = '248fee6868e983c4e7b69074e888960f77735bd21a1d4a1d882b55f45d30a420'
	operation_name = 'VideoPlayerStreamMetadata'
	def build_query(self, variables: VideoPlayerStreamMetadataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ActiveWatchParty(Endpoint):
	sha256Hash = '4a8156c97b19e3a36e081cf6d6ddb5dbf9f9b02ae60e4d2ff26ed70aebc80a30'
	operation_name = 'ActiveWatchParty'
	def build_query(self, variables: ActiveWatchPartyRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerClipsButtonBroadcaster(Endpoint):
	sha256Hash = '784065d408671ee105d64241cc6f461b1c32684d837734fa2f4c761229a7efcd'
	operation_name = 'VideoPlayerClipsButtonBroadcaster'
	def build_query(self, variables: VideoPlayerClipsButtonBroadcasterRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsCelebrations(Endpoint):
	sha256Hash = '8c5da4184cd8d48a962f93f4767abb648c0a3e64637b95d728e635e6f20a28fd'
	operation_name = 'SyncedSettingsCelebrations'
	def build_query(self, variables: SyncedSettingsCelebrationsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CelebrationContextChannelID(Endpoint):
	sha256Hash = '60b6fc5d798253b09d4a09a66acc8f569830573b5ae7319242e1c7bea87b485f'
	operation_name = 'CelebrationContextChannelID'
	def build_query(self, variables: CelebrationContextChannelIDRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetDisplayName(Endpoint):
	sha256Hash = 'ba351b3d3018c3779fcaa398507e41579ae6cf12ad123a04f090943c21dedb8a'
	operation_name = 'GetDisplayName'
	def build_query(self, variables: GetDisplayNameRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PlaybackAccessToken(Endpoint):
	sha256Hash = 'ed230aa1e33e07eebb8928504583da78a5173989fadfb1ac94be06a04f3cdbe9'
	operation_name = 'PlaybackAccessToken'
	def build_query(self, variables: PlaybackAccessTokenRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ExtensionsForChannel(Endpoint):
	sha256Hash = 'd52085e5b03d1fc3534aa49de8f5128b2ee0f4e700f79bf3875dcb1c90947ac3'
	operation_name = 'ExtensionsForChannel'
	def build_query(self, variables: ExtensionsForChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CelebrationEmotes(Endpoint):
	sha256Hash = '2add4bd682371bfb75aa347ad39ae3ba8a168a1cfff03e0867b62582e3ab6786'
	operation_name = 'CelebrationEmotes'
	def build_query(self, variables: CelebrationEmotesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelProductsWithCommunityGiftOffers(Endpoint):
	sha256Hash = '403955b53340517f2a7f219b6bca2b559ad1995bfc98976ed5edc7b19203d774'
	operation_name = 'ChannelProductsWithCommunityGiftOffers'
	def build_query(self, variables: ChannelProductsWithCommunityGiftOffersRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RecapEligibilityQuery(Endpoint):
	sha256Hash = 'caf047b3d39c4ab74d0ae590e4a24530f531e1a33945058a4526d75cd86eb3fc'
	operation_name = 'RecapEligibilityQuery'
	def build_query(self, variables: RecapEligibilityQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BitsConfigContext_Global(Endpoint):
	sha256Hash = '6a265b86f3be1c8d11bdcf32c183e106028c6171e985cc2584d15f7840f5fee6'
	operation_name = 'BitsConfigContext_Global'
	def build_query(self, variables: BitsConfigContext_GlobalRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BitsConfigContext_Channel(Endpoint):
	sha256Hash = 'd897953c76165a0d2a12b57c9c013a77b3cf02b5c153645e1e1631f763bf1eb5'
	operation_name = 'BitsConfigContext_Channel'
	def build_query(self, variables: BitsConfigContext_ChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelShell(Endpoint):
	sha256Hash = '580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe'
	operation_name = 'ChannelShell'
	def build_query(self, variables: ChannelShellRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UseLive(Endpoint):
	sha256Hash = '639d5f11bfb8bf3053b424d9ef650d04c4ebb7d94711d644afb08fe9a0fad5d9'
	operation_name = 'UseLive'
	def build_query(self, variables: UseLiveRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UseViewCount(Endpoint):
	sha256Hash = '95e6bd7acfbb2f220c17e387805141b77b43b18e5b27b4f702713e9ddbe6b907'
	operation_name = 'UseViewCount'
	def build_query(self, variables: UseViewCountRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ExtensionsOverlay(Endpoint):
	sha256Hash = '0ac7d363a6f57917933f99a1066075cc38fcdb87c10643fbb2aeacf21399f7b9'
	operation_name = 'ExtensionsOverlay'
	def build_query(self, variables: ExtensionsOverlayRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamTagsTrackingChannel(Endpoint):
	sha256Hash = '6aa3851aaaf88c320d514eb173563d430b28ed70fdaaf7eeef6ed4b812f48608'
	operation_name = 'StreamTagsTrackingChannel'
	def build_query(self, variables: StreamTagsTrackingChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerStatusOverlayChannel(Endpoint):
	sha256Hash = '938d155c890df88b5da53592e327d36ae9b851d2ee38bdb13342a1402fc24ad2'
	operation_name = 'VideoPlayerStatusOverlayChannel'
	def build_query(self, variables: VideoPlayerStatusOverlayChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DropCurrentSessionContext(Endpoint):
	sha256Hash = '4d06b702d25d652afb9ef835d2a550031f1cf762b193523a92166f40ea3d142b'
	operation_name = 'DropCurrentSessionContext'
	def build_query(self, variables: DropCurrentSessionContextRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetIDFromLogin(Endpoint):
	sha256Hash = '94e82a7b1e3c21e186daa73ee2afc4b8f23bade1fbbff6fe8ac133f50a2f58ca'
	operation_name = 'GetIDFromLogin'
	def build_query(self, variables: GetIDFromLoginRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SubsidizedSubscriptions(Endpoint):
	sha256Hash = 'f3c4ecffe5132de7ab8b694659a990b3533e37b68ffb3026911bc283ed91f14a'
	operation_name = 'SubsidizedSubscriptions'
	def build_query(self, variables: Union[SubsidizedSubscriptionsRequest1, SubsidizedSubscriptionsRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatScreenReaderAutoAnnounce(Endpoint):
	sha256Hash = '3ddf79c5dd411106eae1d44801f1a123ecf82cad7e973575b18367b2c5d63a0c'
	operation_name = 'ChatScreenReaderAutoAnnounce'
	def build_query(self, variables: ChatScreenReaderAutoAnnounceRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SharedChatModeratorStrikes(Endpoint):
	sha256Hash = '846b72652391105f0cd30ff586c807dfb4d4815f768ec13462d7b4d2e0d75d52'
	operation_name = 'SharedChatModeratorStrikes'
	def build_query(self, variables: SharedChatModeratorStrikesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatInput(Endpoint):
	sha256Hash = 'd8ab574eb44e3e82aabc96fc9c59af6eafead3e96262910a6396c007e7a11e05'
	operation_name = 'ChatInput'
	def build_query(self, variables: ChatInputRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CurrentUserBannedStatus(Endpoint):
	sha256Hash = 'dede147839ea4a357639f1dc3d3eb978556e82eefb7abdefce8911d0e23a63ad'
	operation_name = 'CurrentUserBannedStatus'
	def build_query(self, variables: CurrentUserBannedStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatList_ActiveCharityCampaign(Endpoint):
	sha256Hash = '6b2925285953ed45adf0d2769a34dee6e8fc60c7882e8e05d1165d59a829e427'
	operation_name = 'ChatList_ActiveCharityCampaign'
	def build_query(self, variables: ChatList_ActiveCharityCampaignRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GlobalBadges(Endpoint):
	sha256Hash = '9db27e18d61ee393ccfdec8c7d90f14f9a11266298c2e5eb808550b77d7bcdf6'
	operation_name = 'GlobalBadges'
	def build_query(self, variables: GlobalBadgesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatList_Badges(Endpoint):
	sha256Hash = '838a7e0b47c09cac05f93ff081a9ff4f876b68f7624f0fc465fe30031e372fc2'
	operation_name = 'ChatList_Badges'
	def build_query(self, variables: ChatList_BadgesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatRestrictions(Endpoint):
	sha256Hash = '7514aeb3d2c203087b83e920f8d36eb18a5ca1bfa96a554ed431255ecbbbc089'
	operation_name = 'ChatRestrictions'
	def build_query(self, variables: ChatRestrictionsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BlockedUsers(Endpoint):
	sha256Hash = '8044e3fd61f8158a39e07b38f5d1a279d1fdb748faa9889fde046feae640f76b'
	operation_name = 'BlockedUsers'
	def build_query(self, variables: BlockedUsersRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class MessageBufferChatHistory(Endpoint):
	sha256Hash = '33dba0e0c249135052e930cbd6c4a66daa32249ba00d1c8def75857fa3f3431d'
	operation_name = 'MessageBufferChatHistory'
	def build_query(self, variables: Union[MessageBufferChatHistoryRequest1, MessageBufferChatHistoryRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class MessageBuffer_Channel(Endpoint):
	sha256Hash = 'bfc959904f55b5003ae4674d4bea83ebdcd8867ad76e12f38957d433902d2fcc'
	operation_name = 'MessageBuffer_Channel'
	def build_query(self, variables: MessageBuffer_ChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PollChannelSettings(Endpoint):
	sha256Hash = 'e31355d5fd19bf9b3c0907c8302ce9ff5466d06230bec209f78cf04724b7380c'
	operation_name = 'PollChannelSettings'
	def build_query(self, variables: PollChannelSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunityPointsRewardRedemptionContext(Endpoint):
	sha256Hash = 'f585e0d07bee16fa1355238b1762c095cc10470edc263d38c4e3a1b8a7e53f65'
	operation_name = 'CommunityPointsRewardRedemptionContext'
	def build_query(self, variables: CommunityPointsRewardRedemptionContextRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPointsPredictionContext(Endpoint):
	sha256Hash = 'beb846598256b75bd7c1fe54a80431335996153e358ca9c7837ce7bb83d7d383'
	operation_name = 'ChannelPointsPredictionContext'
	def build_query(self, variables: ChannelPointsPredictionContextRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPointsContext(Endpoint):
	sha256Hash = '374314de591e69925fce3ddc2bcf085796f56ebb8cad67a0daa3165c03adc345'
	operation_name = 'ChannelPointsContext'
	def build_query(self, variables: ChannelPointsContextRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPointsGlobalContext(Endpoint):
	sha256Hash = 'd3fa3a96e78a3e62bdd3ef3c4effafeda52442906cec41a9440e609a388679e2'
	operation_name = 'ChannelPointsGlobalContext'
	def build_query(self, variables: ChannelPointsGlobalContextRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsChatPauseSetting(Endpoint):
	sha256Hash = '922f2a23e49da4ce2660f7fbfeefeefab19f7651196f9b54f03555590f173627'
	operation_name = 'SyncedSettingsChatPauseSetting'
	def build_query(self, variables: SyncedSettingsChatPauseSettingRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsDeletedMessageDisplaySetting(Endpoint):
	sha256Hash = '79fbdf86e8ee5fa4ca27cad96c292702eed8a8cc14faedc874a577f6e8fe4004'
	operation_name = 'SyncedSettingsDeletedMessageDisplaySetting'
	def build_query(self, variables: SyncedSettingsDeletedMessageDisplaySettingRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsEmoteAnimations(Endpoint):
	sha256Hash = '64ac5d385b316fd889f8c46942a7c7463a1429452ef20ffc5d0cd23fcc4ecf30'
	operation_name = 'SyncedSettingsEmoteAnimations'
	def build_query(self, variables: SyncedSettingsEmoteAnimationsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SyncedSettingsReadableChatColors(Endpoint):
	sha256Hash = 'cd9c43ab3cb4c04515a879bbd618055aab18c6ac4081ed9de333945ca91247ba'
	operation_name = 'SyncedSettingsReadableChatColors'
	def build_query(self, variables: SyncedSettingsReadableChatColorsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatRoomState(Endpoint):
	sha256Hash = '9e0f79669e31950c658459564bc4cff236ac9c03e534cc32769ac58bc0cdd708'
	operation_name = 'ChatRoomState'
	def build_query(self, variables: ChatRoomStateRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_UserData(Endpoint):
	sha256Hash = '39985d1ff9324442a3a5df1be212e1bc4f358a31100e5025c4e61a07d7e70743'
	operation_name = 'Chat_UserData'
	def build_query(self, variables: Chat_UserDataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_ChannelData(Endpoint):
	sha256Hash = '3c445f9a8315fa164f2d3fb12c2f932754c2f2c129f952605b9ec6cf026dd362'
	operation_name = 'Chat_ChannelData'
	def build_query(self, variables: Chat_ChannelDataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommonHooks_BlockedUsers(Endpoint):
	sha256Hash = '7c87171d7497df41f9938d2bc18a26f7a97f32f11b7f28c4826950c4ebe000b2'
	operation_name = 'CommonHooks_BlockedUsers'
	def build_query(self, variables: CommonHooks_BlockedUsersRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PinnedCheersSettings(Endpoint):
	sha256Hash = 'ca73cb0396fe5bcbe05c906fd472622e4b873eeb07699c2664026a079aeec631'
	operation_name = 'PinnedCheersSettings'
	def build_query(self, variables: PinnedCheersSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CurrentUserStrikeStatus(Endpoint):
	sha256Hash = '954bb138c800c581b291b7068a9225f7e139eb2b5066bc5840a9b251f5eaf11b'
	operation_name = 'CurrentUserStrikeStatus'
	def build_query(self, variables: CurrentUserStrikeStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamChat(Endpoint):
	sha256Hash = 'fed5f3ae0f569dc9d6faf768475456715b853ef737873ed5cb2bb45b3e28e67f'
	operation_name = 'StreamChat'
	def build_query(self, variables: StreamChatRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OneTapFeed(Endpoint):
	sha256Hash = '287ce6226da1b78e05e5024b99a3e3190a3e57e1bd1a95ae16d0eef33edc1547'
	operation_name = 'OneTapFeed'
	def build_query(self, variables: OneTapFeedRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SharedChatSession(Endpoint):
	sha256Hash = '0ff9562b30cfa2b41ab1738485ced6f8f1e725a93abe732c396be5f4f1d13694'
	operation_name = 'SharedChatSession'
	def build_query(self, variables: SharedChatSessionRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelCollaborationEligibilityQuery(Endpoint):
	sha256Hash = 'f32cb49f6bc54a4dc182b54c6e247d8344f8a16cc255acbc2e18fbd145df4cb2'
	operation_name = 'ChannelCollaborationEligibilityQuery'
	def build_query(self, variables: ChannelCollaborationEligibilityQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetHypeTrainExecutionV2(Endpoint):
	sha256Hash = '9248d0eed139a2127b61e5c57e4c7bc4252cd521cb70af6bd5036a7c789598b8'
	operation_name = 'GetHypeTrainExecutionV2'
	def build_query(self, variables: GetHypeTrainExecutionV2Request = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StoryPreviewChannel(Endpoint):
	sha256Hash = '2d5d66edb6b3ea7af518074fcbb9a4b04b17b5ee4dc87fe0e9001cbb31216709'
	operation_name = 'StoryPreviewChannel'
	def build_query(self, variables: StoryPreviewChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamEventCelebrationsChannelPageBadge(Endpoint):
	sha256Hash = '93d2d5760c148819e718d301141e62c91ddf0ef09b3f8b8102afbab6ba833174'
	operation_name = 'StreamEventCelebrationsChannelPageBadge'
	def build_query(self, variables: StreamEventCelebrationsChannelPageBadgeRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestStarActiveJoinRequest(Endpoint):
	sha256Hash = 'ee299efe4c857e2ab673e57c0c29ff3171671dc4980ca3834f63d6e66ed16a8b'
	operation_name = 'GuestStarActiveJoinRequest'
	def build_query(self, variables: GuestStarActiveJoinRequestRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestStarChannelPageCollaborationQuery(Endpoint):
	sha256Hash = 'adb54eefd172fc9d310040afe5c158e2e41ec93dfe030067afa365178243ffa3'
	operation_name = 'GuestStarChannelPageCollaborationQuery'
	def build_query(self, variables: GuestStarChannelPageCollaborationQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatRoomBanStatus(Endpoint):
	sha256Hash = '319f2a9a3ac7ddecd7925944416c14b818b65676ab69da604460b68938d22bea'
	operation_name = 'ChatRoomBanStatus'
	def build_query(self, variables: ChatRoomBanStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestListQuery(Endpoint):
	sha256Hash = '7a2267973bdd74b9ddd5d07ceabd73b5b5d13eae83b54d4436fb5a3fa26c3bc8'
	operation_name = 'GuestListQuery'
	def build_query(self, variables: GuestListQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPage_SubscribeButton_User(Endpoint):
	sha256Hash = '53b7d2bfc430935ea80f813edba87f2447d5401acae5b6d8c885534997c3ca15'
	operation_name = 'ChannelPage_SubscribeButton_User'
	def build_query(self, variables: Union[ChannelPage_SubscribeButton_UserRequest1, ChannelPage_SubscribeButton_UserRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelActiveCharityCampaign(Endpoint):
	sha256Hash = '743d0e962377c1350a9b37987d715844f9782bef9cc207adb5a20240673795eb'
	operation_name = 'ChannelActiveCharityCampaign'
	def build_query(self, variables: ChannelActiveCharityCampaignRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RealtimeStreamTagList(Endpoint):
	sha256Hash = 'a4747cac9d8e8bf6cf80969f6da6363ca1bdbd80fe136797e71504eb404313fd'
	operation_name = 'RealtimeStreamTagList'
	def build_query(self, variables: RealtimeStreamTagListRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamMetadata(Endpoint):
	sha256Hash = 'b57f9b910f8cd1a4659d894fe7550ccc81ec9052c01e438b290fd66a040b9b93'
	operation_name = 'StreamMetadata'
	def build_query(self, variables: StreamMetadataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UseLiveBroadcast(Endpoint):
	sha256Hash = '0b47cc6d8c182acd2e78b81c8ba5414a5a38057f2089b1bbcfa6046aae248bd2'
	operation_name = 'UseLiveBroadcast'
	def build_query(self, variables: UseLiveBroadcastRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class WatchTrackQuery(Endpoint):
	sha256Hash = 'd8e507b720dd231780d57d325fb3a9bb8ee1ee60d424ae106e6dab328ea9b4c6'
	operation_name = 'WatchTrackQuery'
	def build_query(self, variables: WatchTrackQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class TurboAndSubUpsell(Endpoint):
	sha256Hash = '5dbca380e47e37808c89479f51f789990ec653428a01b76c649ebe01afb3aa7e'
	operation_name = 'TurboAndSubUpsell'
	def build_query(self, variables: TurboAndSubUpsellRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UserModStatus(Endpoint):
	sha256Hash = '511b58faf547070bc95b7d32e7b5cdedf8c289a3aeabfc3c5d3ece2de01ae06f'
	operation_name = 'UserModStatus'
	def build_query(self, variables: UserModStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunityOnboardingAllowlist(Endpoint):
	sha256Hash = 'b9119d11f5d434ed5482a7598000066f49dccbcb2395ae11105e28469370d110'
	operation_name = 'CommunityOnboardingAllowlist'
	def build_query(self, variables: CommunityOnboardingAllowlistRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetPinnedChat(Endpoint):
	sha256Hash = '2d099d4c9b6af80a07d8440140c4f3dbb04d516b35c401aab7ce8f60765308d5'
	operation_name = 'GetPinnedChat'
	def build_query(self, variables: GetPinnedChatRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PinnedChatSettings(Endpoint):
	sha256Hash = 'ff555546ff83a3034dee18a6d764123717b6f68553e082dea6b77a66b7b2672e'
	operation_name = 'PinnedChatSettings'
	def build_query(self, variables: PinnedChatSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AvailableEmotesForChannelPaginated(Endpoint):
	sha256Hash = '6c45e0ecaa823cc7db3ecdd1502af2223c775bdcfb0f18a3a0ce9a0b7db8ef6c'
	operation_name = 'AvailableEmotesForChannelPaginated'
	def build_query(self, variables: AvailableEmotesForChannelPaginatedRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class EmotesForChannelFollowStatus(Endpoint):
	sha256Hash = '40cf0bf434717c70fa192e8a7805ae8651fae53a410d609f02ad853e3af94e78'
	operation_name = 'EmotesForChannelFollowStatus'
	def build_query(self, variables: EmotesForChannelFollowStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CurrentUserModeratorStatus(Endpoint):
	sha256Hash = '1684c97f8b9f49bbeff32bfd6fcc08bd4e631f16b4fca43bdcc7e14e20eff110'
	operation_name = 'CurrentUserModeratorStatus'
	def build_query(self, variables: Union[CurrentUserModeratorStatusRequest1, CurrentUserModeratorStatusRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class WithIsStreamLiveQuery(Endpoint):
	sha256Hash = '04e46329a6786ff3a81c01c50bfa5d725902507a0deb83b0edbf7abe7a3716ea'
	operation_name = 'WithIsStreamLiveQuery'
	def build_query(self, variables: WithIsStreamLiveQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPollContext_GetViewablePoll(Endpoint):
	sha256Hash = 'e83188a3836c636393df3191665e543a03733d7c51d3ade3d85e42aa46c2bf55'
	operation_name = 'ChannelPollContext_GetViewablePoll'
	def build_query(self, variables: ChannelPollContext_GetViewablePollRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class LastUnbanRequest(Endpoint):
	sha256Hash = 'ff196f08b09d9f9f977610f676cfc56bc5e2f679ad773c1acc4f889defb9aebd'
	operation_name = 'LastUnbanRequest'
	def build_query(self, variables: LastUnbanRequestRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class EmotePicker_EmotePicker_UserSubscriptionProducts(Endpoint):
	sha256Hash = '71b5f829a4576d53b714c01d3176f192cbd0b14973eb1c3d0ee23d5d1b78fd7e'
	operation_name = 'EmotePicker_EmotePicker_UserSubscriptionProducts'
	def build_query(self, variables: EmotePicker_EmotePicker_UserSubscriptionProductsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BitsCard_Bits(Endpoint):
	sha256Hash = 'fe1052e19ce99f10b5bd9ab63c5de15405ce87a1644527498f0fc1aadeff89f2'
	operation_name = 'BitsCard_Bits'
	def build_query(self, variables: BitsCard_BitsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatModeratorStrikeStatus(Endpoint):
	sha256Hash = '7f50f7190a840cd9fe9a91398f34ebb690eeba7cb28bce70e4cbf7ed1d06f268'
	operation_name = 'ChatModeratorStrikeStatus'
	def build_query(self, variables: ChatModeratorStrikeStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_OrbisPresetText(Endpoint):
	sha256Hash = '960bf1fac4adb3f4e99b0c67627180d5f5ebb6e46139b1149fbdeab68f7f62e1'
	operation_name = 'Chat_OrbisPresetText'
	def build_query(self, variables: Chat_OrbisPresetTextRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunitySupportSettings(Endpoint):
	sha256Hash = '11b3e9eeff8190e1fa7b97cafbcb2427e3a54289676b030fc16a7ae125702da0'
	operation_name = 'CommunitySupportSettings'
	def build_query(self, variables: CommunitySupportSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipsExperimentEnrollmentStatus(Endpoint):
	sha256Hash = '0575e09a580d3a30bffe06b09ebda047ebebf57ab86a4d7329527d312e8dea22'
	operation_name = 'ClipsExperimentEnrollmentStatus'
	def build_query(self, variables: ClipsExperimentEnrollmentStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PaidPinnedChat(Endpoint):
	sha256Hash = '888056ddc92e62a7d2fd7a8e0afae5d61fab767ba621ed1006ba8628f6de8e41'
	operation_name = 'PaidPinnedChat'
	def build_query(self, variables: PaidPinnedChatRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelRoot_AboutPanel(Endpoint):
	sha256Hash = '0df42c4d26990ec1216d0b815c92cc4a4a806e25b352b66ac1dd91d5a1d59b80'
	operation_name = 'ChannelRoot_AboutPanel'
	def build_query(self, variables: ChannelRoot_AboutPanelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ActiveGoals(Endpoint):
	sha256Hash = 'c855218eb019092b69369658150473e440e1c09cb8515396897b96cfe350e647'
	operation_name = 'ActiveGoals'
	def build_query(self, variables: ActiveGoalsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DropsHighlightService_AvailableDrops(Endpoint):
	sha256Hash = '19e0b383db0be3dc917379fddcbf9dfa7c49f1fcc543d920f39f4efd054bc636'
	operation_name = 'DropsHighlightService_AvailableDrops'
	def build_query(self, variables: DropsHighlightService_AvailableDropsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ShoutoutHighlightServiceQuery(Endpoint):
	sha256Hash = 'da377690d61c9f2923af148efb8b79b29674e4195c0230a4037a567ce8d40825'
	operation_name = 'ShoutoutHighlightServiceQuery'
	def build_query(self, variables: ShoutoutHighlightServiceQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatInput_Badges(Endpoint):
	sha256Hash = '8cb0eae66555ad6dc76aaa111d191ea6174c743f996d506f530e479f28e6b37c'
	operation_name = 'ChatInput_Badges'
	def build_query(self, variables: ChatInput_BadgesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class TitleMentions(Endpoint):
	sha256Hash = '79439ae721a6f24f9d761ceae3a5c91097929fc59f5072a3b505e675bb3d432f'
	operation_name = 'TitleMentions'
	def build_query(self, variables: TitleMentionsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowButton_User(Endpoint):
	sha256Hash = '870906a2de25d7488239dbeb947dafe3e5697f1fef2e8bce6601555a17e4d86d'
	operation_name = 'FollowButton_User'
	def build_query(self, variables: FollowButton_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PartnerPlusPublicQuery(Endpoint):
	sha256Hash = 'b9b3c7607a381300d6ce63451689f85723cd864b28e74e932c1eb5b31cd070bf'
	operation_name = 'PartnerPlusPublicQuery'
	def build_query(self, variables: PartnerPlusPublicQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CanCreateClip(Endpoint):
	sha256Hash = 'ea1796b7893cd9ab447c989967e8441ea230ea54091f63e71d4b189b72d17215'
	operation_name = 'CanCreateClip'
	def build_query(self, variables: CanCreateClipRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PersistentGoalFollowButton_User(Endpoint):
	sha256Hash = '88f5b0d6e9d13d6751b07b5e9cc175e3f7f6f7cedb07b033e1b548ba2323f015'
	operation_name = 'PersistentGoalFollowButton_User'
	def build_query(self, variables: PersistentGoalFollowButton_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class WatchStreakExperiment(Endpoint):
	sha256Hash = 'ec1ad3e0e7a2c3c3c762652f7a42b12da8b4db074fe99f0d29b2febd330465db'
	operation_name = 'WatchStreakExperiment'
	def build_query(self, variables: WatchStreakExperimentRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_ShareBitsBadgeTier_ChannelData(Endpoint):
	sha256Hash = '95383deae2b82f718b9d713ca433807ff60dffa8c834e2ae92abdfeb55586fc4'
	operation_name = 'Chat_ShareBitsBadgeTier_ChannelData'
	def build_query(self, variables: Chat_ShareBitsBadgeTier_ChannelDataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_ShareResub_ChannelData(Endpoint):
	sha256Hash = '1cef2e84b602f767839e5ffd489e81536e9d11e0be250bb85a17974cedad8f54'
	operation_name = 'Chat_ShareResub_ChannelData'
	def build_query(self, variables: Chat_ShareResub_ChannelDataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetGuestSessionBlocksAndBans(Endpoint):
	sha256Hash = '4a96b8e893624487d7eaf212f61e756e00354e969a19b0e01d2e863021d75974'
	operation_name = 'GetGuestSessionBlocksAndBans'
	def build_query(self, variables: GetGuestSessionBlocksAndBansRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPointsAutomaticRewards(Endpoint):
	sha256Hash = '9147a41525586ff3739f30c0c27ae1df84f943e6b9be7d0f669c9505fda1888b'
	operation_name = 'ChannelPointsAutomaticRewards'
	def build_query(self, variables: ChannelPointsAutomaticRewardsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelLeaderboards(Endpoint):
	sha256Hash = 'ccc0fe65d86216ca35fae890e29e53e508dc3ff6bbe4fd893ca9b5b87dffbe5e'
	operation_name = 'ChannelLeaderboards'
	def build_query(self, variables: ChannelLeaderboardsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BannerNotificationQuery(Endpoint):
	sha256Hash = '5ab0ba7522eeac29c0ebbba94b81d1dd1bb0082298b04cbc01a5fd531e67c8e2'
	operation_name = 'BannerNotificationQuery'
	def build_query(self, variables: BannerNotificationQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StoryChannelQuery(Endpoint):
	sha256Hash = 'efa575524a7a86bf6172801278301584a366e59a8049c667fd4abea01522b8a2'
	operation_name = 'StoryChannelQuery'
	def build_query(self, variables: StoryChannelQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelSupportButtons(Endpoint):
	sha256Hash = '834a75e1c06cffada00f0900664a5033e392f6fb655fae8d2e25b21b340545a9'
	operation_name = 'ChannelSupportButtons'
	def build_query(self, variables: ChannelSupportButtonsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AcknowledgeUnbanRequestPrompt(Endpoint):
	sha256Hash = '814210afb9c7c392ce35028f3a3aebfff446c3be2925af8c9ff4c04a34fe8c5f'
	operation_name = 'AcknowledgeUnbanRequestPrompt'
	def build_query(self, variables: AcknowledgeUnbanRequestPromptRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoMarkersChatCommand(Endpoint):
	sha256Hash = 'c65f8b33e3bcccf2b16057e8f445311d213ecf8729f842ccdc71908231fa9a78'
	operation_name = 'VideoMarkersChatCommand'
	def build_query(self, variables: VideoMarkersChatCommandRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommercialCommandHandler_ChannelData(Endpoint):
	sha256Hash = 'ec415677f12d805693445931552fbbbf60f44f96826019578e15a8171dcd4cbb'
	operation_name = 'CommercialCommandHandler_ChannelData'
	def build_query(self, variables: CommercialCommandHandler_ChannelDataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsAffiliateQuery(Endpoint):
	sha256Hash = '5fe9382deefda20dc0720fd1b64b2e72607460c86cf14515509bd736ae003451'
	operation_name = 'AccessIsAffiliateQuery'
	def build_query(self, variables: AccessIsAffiliateQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsPartnerQuery(Endpoint):
	sha256Hash = 'c1744ef223c4e664367f6ae29d711ec91693b786e2c81bf84f6bdc4df4e1c87a'
	operation_name = 'AccessIsPartnerQuery'
	def build_query(self, variables: AccessIsPartnerQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunityPointsChatPrivateCalloutUser(Endpoint):
	sha256Hash = '15b66a0a6b743c72a63c273f2bfc4155c4209c1a85c29b6847474717877c3507'
	operation_name = 'CommunityPointsChatPrivateCalloutUser'
	def build_query(self, variables: CommunityPointsChatPrivateCalloutUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Chat_EarnedBadges_InitialSubStatus(Endpoint):
	sha256Hash = '85a95b95a12628668eaac4d2862b53bb376dba0325c80eae8f26539cedc5f1a3'
	operation_name = 'Chat_EarnedBadges_InitialSubStatus'
	def build_query(self, variables: Chat_EarnedBadges_InitialSubStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamEventsActiveCelebrationCalloutQuery(Endpoint):
	sha256Hash = '5aacb3d143a790543af385fe85f43b0bab5f005614a52fc8a3a63b2f9fa26a14'
	operation_name = 'StreamEventsActiveCelebrationCalloutQuery'
	def build_query(self, variables: StreamEventsActiveCelebrationCalloutQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CollaborationPromoPrivateCallout(Endpoint):
	sha256Hash = '076a3f5b956a40be7ae9fc47fd9d556ec9111c878fa5c7e68d83e1be7b433def'
	operation_name = 'CollaborationPromoPrivateCallout'
	def build_query(self, variables: CollaborationPromoPrivateCalloutRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CommunityPointsAvailableClaim(Endpoint):
	sha256Hash = '3a4ca75d2a784eea5c40f38a60fe9f6ab8c565c030de06c561398ee5099f818c'
	operation_name = 'CommunityPointsAvailableClaim'
	def build_query(self, variables: CommunityPointsAvailableClaimRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ExtensionsInfoBalloon(Endpoint):
	sha256Hash = '5081a05901d5a76e7cdab6078d21c08e63da4eef365303d4fbeaf6d4c50bed42'
	operation_name = 'ExtensionsInfoBalloon'
	def build_query(self, variables: ExtensionsInfoBalloonRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class updateUserViewedVideo(Endpoint):
	sha256Hash = 'bb58b1bd08a4ca0c61f2b8d323381a5f4cd39d763da8698f680ef1dfaea89ca1'
	operation_name = 'updateUserViewedVideo'
	def build_query(self, variables: updateUserViewedVideoRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelPanels(Endpoint):
	sha256Hash = '06d5b518ba3b016ebe62000151c9a81f162f2a1430eb1cf9ad0678ba56d0a768'
	operation_name = 'ChannelPanels'
	def build_query(self, variables: ChannelPanelsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ExtensionProducts(Endpoint):
	sha256Hash = 'f65c973904d0e7b66a25de0b6b01ee8ef81df8d1cb60850e8a88d4da41ab626d'
	operation_name = 'ExtensionProducts'
	def build_query(self, variables: ExtensionProductsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeOfflineCarousel(Endpoint):
	sha256Hash = '84e25789b04ac4dcaefd673cfb4259d39d03c6422838d09a4ed2aaf9b67054d8'
	operation_name = 'HomeOfflineCarousel'
	def build_query(self, variables: HomeOfflineCarouselRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelAvatar(Endpoint):
	sha256Hash = '12575ab92ea9444d8bade6de529b288a05073617f319c87078b3a89e74cd783a'
	operation_name = 'ChannelAvatar'
	def build_query(self, variables: ChannelAvatarRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class LowerHomeHeader(Endpoint):
	sha256Hash = '08af264bf5d5231cadb05acaddce0992622f86a0d3d7f6f59955316564d3c008'
	operation_name = 'LowerHomeHeader'
	def build_query(self, variables: LowerHomeHeaderRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RoleRestricted(Endpoint):
	sha256Hash = '7f57264e30ae6d9daa154bb62c8b0bcb1b38fc0b53a7b3cdecd60a060ff8332b'
	operation_name = 'RoleRestricted'
	def build_query(self, variables: RoleRestrictedRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelVideoShelvesQuery(Endpoint):
	sha256Hash = 'eea6c7a6baaa6ee60825f469c943cfda7e7c2415c01c64d7fd1407d172e82a7b'
	operation_name = 'ChannelVideoShelvesQuery'
	def build_query(self, variables: ChannelVideoShelvesQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeTrackQuery(Endpoint):
	sha256Hash = '129cbf14117ce8e95f01bd2043154089058146664df866d0314e84355ffb4e05'
	operation_name = 'HomeTrackQuery'
	def build_query(self, variables: HomeTrackQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatFilterContextManager_User(Endpoint):
	sha256Hash = '98821224809f26e3f3a627a0e30134b00c4db33b602b4249cec518a8c21fe902'
	operation_name = 'ChatFilterContextManager_User'
	def build_query(self, variables: ChatFilterContextManager_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PbyPGame(Endpoint):
	sha256Hash = 'f7444c6e187868a7b82e7659e59bb8ccd177cb4deca277e3a951fb2ef66c2389'
	operation_name = 'PbyPGame'
	def build_query(self, variables: PbyPGameRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FeaturedClipsShelfCover(Endpoint):
	sha256Hash = '90e7b62983b247aea06aafc7e20699889914e331daec97f68fd33d714cc17738'
	operation_name = 'FeaturedClipsShelfCover'
	def build_query(self, variables: FeaturedClipsShelfCoverRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPreviewCard__VideoMoments(Endpoint):
	sha256Hash = '7399051b2d46f528d5f0eedf8b0db8d485bb1bb4c0a2c6707be6f1290cdcb31a'
	operation_name = 'VideoPreviewCard__VideoMoments'
	def build_query(self, variables: VideoPreviewCard__VideoMomentsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipsCards__User(Endpoint):
	sha256Hash = '4eb8f85fc41a36c481d809e8e99b2a32127fdb7647c336d27743ec4a88c4ea44'
	operation_name = 'ClipsCards__User'
	def build_query(self, variables: ClipsCards__UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamSchedule(Endpoint):
	sha256Hash = '83552f5614707fd3e897495c18875b6fa9c83d8cf11e73b9f158f3173b4f3b75'
	operation_name = 'StreamSchedule'
	def build_query(self, variables: StreamScheduleRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FilterableVideoTower_Videos(Endpoint):
	sha256Hash = 'acea7539a293dfd30f0b0b81a263134bb5d9a7175592e14ac3f7c77b192de416'
	operation_name = 'FilterableVideoTower_Videos'
	def build_query(self, variables: Union[FilterableVideoTower_VideosRequest1, FilterableVideoTower_VideosRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class queryUserViewedVideo(Endpoint):
	sha256Hash = 'e249447c070b095eb599cceec239bbca567e30080795789f85bc25db3f7a27ad'
	operation_name = 'queryUserViewedVideo'
	def build_query(self, variables: queryUserViewedVideoRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VODMidrollManager(Endpoint):
	sha256Hash = 'dcfb8c8cd3b721da5720fda11b9a20a3ab94be85ec04e8c2ac48ff69f300e959'
	operation_name = 'VODMidrollManager'
	def build_query(self, variables: VODMidrollManagerRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_VODSeekbar(Endpoint):
	sha256Hash = 'c67d32eba8f1c93b02e7efa6a278be46009e390ed5195c02dd0621e4c7ca14ac'
	operation_name = 'VideoPlayer_VODSeekbar'
	def build_query(self, variables: VideoPlayer_VODSeekbarRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_ChapterSelectButtonVideo(Endpoint):
	sha256Hash = '71835d5ef425e154bf282453a926d99b328cdc5e32f36d3a209d0f4778b41203'
	operation_name = 'VideoPlayer_ChapterSelectButtonVideo'
	def build_query(self, variables: VideoPlayer_ChapterSelectButtonVideoRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoComments(Endpoint):
	sha256Hash = 'be06407e8d7cda72f2ee086ebb11abb6b062a7deb8985738e648090904d2f0eb'
	operation_name = 'VideoComments'
	def build_query(self, variables: VideoCommentsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoCommentsByOffsetOrCursor(Endpoint):
	sha256Hash = 'b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a'
	operation_name = 'VideoCommentsByOffsetOrCursor'
	def build_query(self, variables: Union[VideoCommentsByOffsetOrCursorRequest1, VideoCommentsByOffsetOrCursorRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoMetadata(Endpoint):
	sha256Hash = '45111672eea2e507f8ba44d101a61862f9c56b11dee09a15634cb75cb9b9084d'
	operation_name = 'VideoMetadata'
	def build_query(self, variables: VideoMetadataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_VODSeekbarPreviewVideo(Endpoint):
	sha256Hash = '07e99e4d56c5a7c67117a154777b0baf85a5ffefa393b213f4bc712ccaf85dd6'
	operation_name = 'VideoPlayer_VODSeekbarPreviewVideo'
	def build_query(self, variables: VideoPlayer_VODSeekbarPreviewVideoRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoAdRequestDecline(Endpoint):
	sha256Hash = '6f5d9fdc36a3c879cca7debdbe21c62d5cac4ad5b30b635263eff68335b96a71'
	operation_name = 'VideoAdRequestDecline'
	def build_query(self, variables: VideoAdRequestDeclineRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedIndex_CurrentUser(Endpoint):
	sha256Hash = '740647c696400dad6767b9407089fc2d52e88c4227dbb1f5cd763e015cc61df2'
	operation_name = 'FollowedIndex_CurrentUser'
	def build_query(self, variables: FollowedIndex_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedIndex_FollowCount(Endpoint):
	sha256Hash = '8945379bb5b05b905ba4e3669d02b863a3089fae81befc9f2a82dbd45ae6efc5'
	operation_name = 'FollowedIndex_FollowCount'
	def build_query(self, variables: FollowedIndex_FollowCountRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowingGames_CurrentUser(Endpoint):
	sha256Hash = 'f3c5d45175d623ed3d5ff4ca4c7de379ea6a1a4852236087dc1b81b7dbfd3114'
	operation_name = 'FollowingGames_CurrentUser'
	def build_query(self, variables: FollowingGames_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowingLive_CurrentUser(Endpoint):
	sha256Hash = 'ecadcf350272dde399a63385cf888903d7fcd4c8fc6809a8469fe3753579d1c6'
	operation_name = 'FollowingLive_CurrentUser'
	def build_query(self, variables: FollowingLive_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedVideos_CurrentUser(Endpoint):
	sha256Hash = '11d0ddb94121afab8fa8b641e01f038db35892f95b4e4b9e5380eaa33d5e4a8c'
	operation_name = 'FollowedVideos_CurrentUser'
	def build_query(self, variables: FollowedVideos_CurrentUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowingPage_RecommendedChannels(Endpoint):
	sha256Hash = '39c731d90e41de782e21c370c6e43bd23757fcaf98051e865016faef05c080b4'
	operation_name = 'FollowingPage_RecommendedChannels'
	def build_query(self, variables: FollowingPage_RecommendedChannelsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedStreamsContinueWatching(Endpoint):
	sha256Hash = 'c689d0645defdd63aaab322166a570c785cefa97b6e97c1a1e7fb66ccdfcad82'
	operation_name = 'FollowedStreamsContinueWatching'
	def build_query(self, variables: FollowedStreamsContinueWatchingRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowedStreams(Endpoint):
	sha256Hash = '10fbb27d9260e3688cd9febdbdd3e21e3331d698ca282dc5f0cf0d29bb468fdd'
	operation_name = 'FollowedStreams'
	def build_query(self, variables: FollowedStreamsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BrowsePage_AllDirectories(Endpoint):
	sha256Hash = '2f67f71ba89f3c0ed26a141ec00da1defecb2303595f5cda4298169549783d9e'
	operation_name = 'BrowsePage_AllDirectories'
	def build_query(self, variables: Union[BrowsePage_AllDirectoriesRequest1, BrowsePage_AllDirectoriesRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BrowseVerticalDirectory(Endpoint):
	sha256Hash = 'd27ea34dd3c0a4c183deb152c1223b44794e7fd3c336bdc15aa61abc65cc2b76'
	operation_name = 'BrowseVerticalDirectory'
	def build_query(self, variables: BrowseVerticalDirectoryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DirectoryCollection_BrowsableCollection(Endpoint):
	sha256Hash = '459f2a65ca11d3765450546a68980ac5868a6b4cce1a9e10bccb9a6e52d2c30d'
	operation_name = 'DirectoryCollection_BrowsableCollection'
	def build_query(self, variables: Union[DirectoryCollection_BrowsableCollectionRequest1, DirectoryCollection_BrowsableCollectionRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfEditor(Endpoint):
	sha256Hash = '1079fccbb422d5bd48594cd8fdbfe4998f2ac4f331e3db93cba1cf2203f9901d'
	operation_name = 'HomeShelfEditor'
	def build_query(self, variables: HomeShelfEditorRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfUsers(Endpoint):
	sha256Hash = '3d9e1494fe4b426aa3ea81ff63dc87e784529a150bdc362c01cdb2c30373440f'
	operation_name = 'HomeShelfUsers'
	def build_query(self, variables: HomeShelfUsersRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfVideos(Endpoint):
	sha256Hash = '951c268434dc36a482c6f854215df953cf180fc2757f1e0e47aa9821258debf7'
	operation_name = 'HomeShelfVideos'
	def build_query(self, variables: HomeShelfVideosRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HomeShelfGames(Endpoint):
	sha256Hash = 'cb7711739c2b520ebf89f3027863c0f985e8094df91cc5ef28896d57375a9700'
	operation_name = 'HomeShelfGames'
	def build_query(self, variables: HomeShelfGamesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OfflineBannerOverlay(Endpoint):
	sha256Hash = '64116eb1e0e2818e8d7a8afb2fa1e9a2fac5b2d1b5e8300b39209aa414f2e577'
	operation_name = 'OfflineBannerOverlay'
	def build_query(self, variables: OfflineBannerOverlayRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerOfflineRecommendationsOverlay(Endpoint):
	sha256Hash = '73794e55fa4149d5a17b31105f74e625f291ca68a4c034076053be0f647ba5ee'
	operation_name = 'VideoPlayerOfflineRecommendationsOverlay'
	def build_query(self, variables: VideoPlayerOfflineRecommendationsOverlayRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelClipCore(Endpoint):
	sha256Hash = 'a33067cdf92191dccfb53aa86f878a2c271e6a3587a6731dc8275e5751dd133f'
	operation_name = 'ChannelClipCore'
	def build_query(self, variables: ChannelClipCoreRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoAccessToken_Clip(Endpoint):
	sha256Hash = '6fd3af2b22989506269b9ac02dd87eb4a6688392d67d94e41a6886f1e9f5c00f'
	operation_name = 'VideoAccessToken_Clip'
	def build_query(self, variables: VideoAccessToken_ClipRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipMetadata(Endpoint):
	sha256Hash = '49817470e0129051cd93c86069aee755795f1a952688f0111bac71a49841ece7'
	operation_name = 'ClipMetadata'
	def build_query(self, variables: ClipMetadataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ShareClipRenderStatus(Endpoint):
	sha256Hash = 'f130048a462a0ac86bb54d653c968c514e9ab9ca94db52368c1179e97b0f16eb'
	operation_name = 'ShareClipRenderStatus'
	def build_query(self, variables: ShareClipRenderStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatClip(Endpoint):
	sha256Hash = '9aa558e066a22227c5ef2c0a8fded3aaa57d35181ad15f63df25bff516253a90'
	operation_name = 'ChatClip'
	def build_query(self, variables: ChatClipRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CanViewersExportQuery(Endpoint):
	sha256Hash = '8f5d5163e711a884a88079cbcd24d68adc6a90a7fcb4030a5aef266372c33fd0'
	operation_name = 'CanViewersExportQuery'
	def build_query(self, variables: CanViewersExportQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessGetFeatureClipRestrictionsQuery(Endpoint):
	sha256Hash = '14ae9c701ed1113c7c16a0cb613e7ba7eca000bc1b907c2969f2756e8af5a05b'
	operation_name = 'AccessGetFeatureClipRestrictionsQuery'
	def build_query(self, variables: AccessGetFeatureClipRestrictionsQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class incrementClipViewCount(Endpoint):
	sha256Hash = '6b2f169f994f2b93ff68774f6928de66a1e8cdb70a42f4af3a5a1ecc68ee759b'
	operation_name = 'incrementClipViewCount'
	def build_query(self, variables: incrementClipViewCountRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HappeningNowSettings(Endpoint):
	sha256Hash = '6945ce7f7df91e52f21edc98ea04f63e5ab38f4e6f4b5699bdd652171f9a7b48'
	operation_name = 'HappeningNowSettings'
	def build_query(self, variables: HappeningNowSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClaimCommunityPoints(Endpoint):
	sha256Hash = '46aaeebe02c99afdf4fc97c7c0cba964124bf6b0af229395f1f6d1feed05b3d0'
	operation_name = 'ClaimCommunityPoints'
	def build_query(self, variables: ClaimCommunityPointsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RewardCenter_BitsBalance(Endpoint):
	sha256Hash = '7fdcc9a5931b57016fcf5a70a9d8341b0946f02441c8f96c33c1ecd43af0098a'
	operation_name = 'RewardCenter_BitsBalance'
	def build_query(self, variables: RewardCenter_BitsBalanceRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelCheckoutService(Endpoint):
	sha256Hash = '868b57f4c88463e263805878465d3f753b894ce3054b4d16591dfcc171a7305c'
	operation_name = 'SupportPanelCheckoutService'
	def build_query(self, variables: SupportPanelCheckoutServiceRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelTrackingService(Endpoint):
	sha256Hash = '6b16029a6dd07696db9a8785a8358906b75a03d35a9a48c7c1f09501dd0d461b'
	operation_name = 'SupportPanelTrackingService'
	def build_query(self, variables: SupportPanelTrackingServiceRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GiftSubscriptionRewardPreviews(Endpoint):
	sha256Hash = '2dfadd0b52d2c55bb6ec2759a1895e75837b285894e9e9edd0eb4583ef949f3e'
	operation_name = 'GiftSubscriptionRewardPreviews'
	def build_query(self, variables: GiftSubscriptionRewardPreviewsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelCommunityGifting_GiftingOptions(Endpoint):
	sha256Hash = '4ddae541bd880334a21289bd7b5554319a377eb60b1bdf6afd030f3a57b590ed'
	operation_name = 'SupportPanelCommunityGifting_GiftingOptions'
	def build_query(self, variables: SupportPanelCommunityGifting_GiftingOptionsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelSubTokenBalance(Endpoint):
	sha256Hash = '170d23ae26cda040dfc45bc24a057f61180440619f725c2fa81264c168056b89'
	operation_name = 'SupportPanelSubTokenBalance'
	def build_query(self, variables: SupportPanelSubTokenBalanceRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OneClickEligibility(Endpoint):
	sha256Hash = 'ab0d03b2c38e3a570ca5f8fb4d0884bc7764c6f25a05345dc2014c611fa02de9'
	operation_name = 'OneClickEligibility'
	def build_query(self, variables: OneClickEligibilityRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelSubTokenOffers(Endpoint):
	sha256Hash = '524d0492e36d6df44e9d2d7416bfdefa0c8d1b37c1010fef107515be9934005f'
	operation_name = 'SupportPanelSubTokenOffers'
	def build_query(self, variables: SupportPanelSubTokenOffersRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelCommunityGifting_GifterBadgeProgress(Endpoint):
	sha256Hash = '13767ee11d9aaaedbe92816e3efef4a968e9184ac6fb63876b8ea38abd93a556'
	operation_name = 'SupportPanelCommunityGifting_GifterBadgeProgress'
	def build_query(self, variables: SupportPanelCommunityGifting_GifterBadgeProgressRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowButton_UnfollowUser(Endpoint):
	sha256Hash = 'f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880'
	operation_name = 'FollowButton_UnfollowUser'
	def build_query(self, variables: FollowButton_UnfollowUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowButton_FollowUser(Endpoint):
	sha256Hash = '800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08'
	operation_name = 'FollowButton_FollowUser'
	def build_query(self, variables: FollowButton_FollowUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelTitleSectionAvatar(Endpoint):
	sha256Hash = '4ad8c04d43eaca0df7ee2a7d93451388f9067ec0e28faa0e021f2d73bdf6e5bf'
	operation_name = 'SupportPanelTitleSectionAvatar'
	def build_query(self, variables: SupportPanelTitleSectionAvatarRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SubscriptionRewardPreviews(Endpoint):
	sha256Hash = 'e6598682b4e3e1fe0910b4d52c6a7429221064a23c2fa4f587a8730a303a0c6f'
	operation_name = 'SubscriptionRewardPreviews'
	def build_query(self, variables: SubscriptionRewardPreviewsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelSubscribeViewFooterPrime(Endpoint):
	sha256Hash = '02d85dc601efbdf6ac4583bc7e7b1c4b9855dadf1f8f051eef1d76adeb84eac6'
	operation_name = 'SupportPanelSubscribeViewFooterPrime'
	def build_query(self, variables: SupportPanelSubscribeViewFooterPrimeRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SupportPanelFooterPrimeStatus(Endpoint):
	sha256Hash = '7068914034996f65eaa5b1502273c6ede1ab31cff9bab3fad3f8c2df120e6e78'
	operation_name = 'SupportPanelFooterPrimeStatus'
	def build_query(self, variables: SupportPanelFooterPrimeStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PersonalSectionsHypeTrains(Endpoint):
	sha256Hash = '073ad6ed08cd7d57f2532cd9b2ae962c323343a8ed8a46e853cd9afa00712c06'
	operation_name = 'PersonalSectionsHypeTrains'
	def build_query(self, variables: PersonalSectionsHypeTrainsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class MinimalTopNav_MinimalUser(Endpoint):
	sha256Hash = '304ffa541474ba444ad0c71c9b90c47a8163518084183f55b6204175b91969ec'
	operation_name = 'MinimalTopNav_MinimalUser'
	def build_query(self, variables: MinimalTopNav_MinimalUserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class TurboProductInformation(Endpoint):
	sha256Hash = '1a11feb222a0722e20b78fd387f060d1e63074d7ca972650c25ae5d9af0975ce'
	operation_name = 'TurboProductInformation'
	def build_query(self, variables: TurboProductInformationRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Sub_Analytics(Endpoint):
	sha256Hash = '16c245170e5191a60d1608b96799c76258e548a744aba5e7ecf672e775ea1485'
	operation_name = 'Sub_Analytics'
	def build_query(self, variables: Sub_AnalyticsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelSocialButtons(Endpoint):
	sha256Hash = '597b4ee27086064ccd59bef5c02775e9963cc3354f2095159484e816ccc1aec2'
	operation_name = 'ChannelSocialButtons'
	def build_query(self, variables: ChannelSocialButtonsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class RewardList(Endpoint):
	sha256Hash = '5822bbafff9e03713e1733b70c03ecdf3253d3a7b00e3a38965f5091f931c3c9'
	operation_name = 'RewardList'
	def build_query(self, variables: RewardListRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SearchTray_SearchSuggestions(Endpoint):
	sha256Hash = '2749d8bc89a2ddd37518e23742a4287becd3064c40465d8b57317cabd0efe096'
	operation_name = 'SearchTray_SearchSuggestions'
	def build_query(self, variables: SearchTray_SearchSuggestionsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SearchResultsPage_SearchResults(Endpoint):
	sha256Hash = 'f6c2575aee4418e8a616e03364d8bcdbf0b10a5c87b59f523569dacc963e8da5'
	operation_name = 'SearchResultsPage_SearchResults'
	def build_query(self, variables: SearchResultsPage_SearchResultsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class LiveNotificationsToggle_User(Endpoint):
	sha256Hash = 'c559c3e45f42f8d04e855419ef294571395ef62d56d9c68003709d9250e6a2c3'
	operation_name = 'LiveNotificationsToggle_User'
	def build_query(self, variables: LiveNotificationsToggle_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Directory_DirectoryBanner(Endpoint):
	sha256Hash = '822ecf40c2a77568d2b223fd5bc4dfdc9c863f081dd1ca7611803a5330e88277'
	operation_name = 'Directory_DirectoryBanner'
	def build_query(self, variables: Directory_DirectoryBannerRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DirectoryPage_Game(Endpoint):
	sha256Hash = 'c7c9d5aad09155c4161d2382092dc44610367f3536aac39019ec2582ae5065f9'
	operation_name = 'DirectoryPage_Game'
	def build_query(self, variables: DirectoryPage_GameRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DirectoryRoot_Directory(Endpoint):
	sha256Hash = '99d3c9b5ceaadb36f77c8bc2d576a737c83d2e9f06c4d6190cf2c6b4f214cccb'
	operation_name = 'DirectoryRoot_Directory'
	def build_query(self, variables: DirectoryRoot_DirectoryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowGameButton_Game(Endpoint):
	sha256Hash = '8c5ac3233e26d9132ca2aaa8fb4b07ae97bc70f3c9a357967b9a764ebccaa9f0'
	operation_name = 'FollowGameButton_Game'
	def build_query(self, variables: FollowGameButton_GameRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DirectoryVideos_Game(Endpoint):
	sha256Hash = 'f19b861ed9c767a1c231be8f757958005cd537a6e9730bc01c6b4735c2eaf211'
	operation_name = 'DirectoryVideos_Game'
	def build_query(self, variables: Union[DirectoryVideos_GameRequest1, DirectoryVideos_GameRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Prime_PrimeOfferList_PrimeOffers_Eligibility(Endpoint):
	sha256Hash = '630945e9a3b4edbcadb1494b0c77b43301199ca0717ad35f712c2f81f7951690'
	operation_name = 'Prime_PrimeOfferList_PrimeOffers_Eligibility'
	def build_query(self, variables: Prime_PrimeOfferList_PrimeOffers_EligibilityRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OnsiteNotifications_View(Endpoint):
	sha256Hash = 'e8e06193f8df73d04a1260df318585d1bd7a7bb447afa058e52095513f2bfa4f'
	operation_name = 'OnsiteNotifications_View'
	def build_query(self, variables: OnsiteNotifications_ViewRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class OnsiteNotifications_ListNotifications(Endpoint):
	sha256Hash = 'df01411293c7de538f433f7f8f5d741e724bfb548c2841b432a8d9c8bc8b9ba0'
	operation_name = 'OnsiteNotifications_ListNotifications'
	def build_query(self, variables: OnsiteNotifications_ListNotificationsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SettingsNotificationsPage_User(Endpoint):
	sha256Hash = '066612d3d17cc710e325747455c45b76e7d60440bb115f7a1a1caa3e5b094235'
	operation_name = 'SettingsNotificationsPage_User'
	def build_query(self, variables: SettingsNotificationsPage_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SmartNotificationSettings_User(Endpoint):
	sha256Hash = '8c25c7a7d42bf79c2262f18837221ac5f8f57004cc8bd95b5c53d953ab8c7258'
	operation_name = 'SmartNotificationSettings_User'
	def build_query(self, variables: SmartNotificationSettings_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PlatformNotificationSettings_User(Endpoint):
	sha256Hash = 'a4985d4b0b0e57db35b4f12bb89b9d4cbaf8da6860f32989cf47b165b91fbb47'
	operation_name = 'PlatformNotificationSettings_User'
	def build_query(self, variables: PlatformNotificationSettings_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AdvancedNotificationSettings_User(Endpoint):
	sha256Hash = 'b0e25e3ffd4572bd6ec8d5460f21780edff3c7537552579f7c0018a58d006e37'
	operation_name = 'AdvancedNotificationSettings_User'
	def build_query(self, variables: AdvancedNotificationSettings_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UserDJStatusQuery(Endpoint):
	sha256Hash = '2aee497a53d55c20a145062a6aec5068f2965f46c731081009da6ec93d4c0576'
	operation_name = 'UserDJStatusQuery'
	def build_query(self, variables: UserDJStatusQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SunlightLoggedInUserMenuQuery(Endpoint):
	sha256Hash = '7b4a73d96cdd21b4282542151bbf1f2a3f09bb3d11b8f5c1bbb40153717f0fc9'
	operation_name = 'SunlightLoggedInUserMenuQuery'
	def build_query(self, variables: SunlightLoggedInUserMenuQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class HasNewBountiesContextQuery(Endpoint):
	sha256Hash = '581d96275f28ce8ef519d748e225d67244cd4c138e4345d52e6bc828288a2033'
	operation_name = 'HasNewBountiesContextQuery'
	def build_query(self, variables: HasNewBountiesContextQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsBountiesEnabledQuery(Endpoint):
	sha256Hash = '30e68974abf8a6396c3ae9fb0d8de1eeae0372b98ad1393ae7287bda6bb04791'
	operation_name = 'AccessIsBountiesEnabledQuery'
	def build_query(self, variables: AccessIsBountiesEnabledQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CharityNavItem(Endpoint):
	sha256Hash = '5f0494528bc8c9a199efa35d6f51e91e478d253712f6665ff7369453c4069d84'
	operation_name = 'CharityNavItem'
	def build_query(self, variables: CharityNavItemRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsExtensionsDeveloperQuery(Endpoint):
	sha256Hash = '583006a357eed0578f98f9e78b12b37ff622ca8e9d691640da98564f7c4da6ea'
	operation_name = 'AccessIsExtensionsDeveloperQuery'
	def build_query(self, variables: AccessIsExtensionsDeveloperQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsSiteAdminQuery(Endpoint):
	sha256Hash = '030b3cc3430cc192530eb7baf819133f84943e2b1de87a063b6446c55ca6ae9e'
	operation_name = 'AccessIsSiteAdminQuery'
	def build_query(self, variables: AccessIsSiteAdminQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessGetUserQuery(Endpoint):
	sha256Hash = '3761592aaf6d123836b6acfefc9608b4b9ac8517222dff51feabc8c773e15dda'
	operation_name = 'AccessGetUserQuery'
	def build_query(self, variables: AccessGetUserQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Dashboard_CensusGetBirthdate(Endpoint):
	sha256Hash = '3b314df01db471e20f9a26fcc83043e91daa42c641fbec136d092a35af9f03e6'
	operation_name = 'Dashboard_CensusGetBirthdate'
	def build_query(self, variables: Dashboard_CensusGetBirthdateRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsChannelPointsAvailableQuery(Endpoint):
	sha256Hash = 'b987a45e00f633c7e8941f02ade467c7bf1c2795db1995e108aa5c79eb94484f'
	operation_name = 'AccessIsChannelPointsAvailableQuery'
	def build_query(self, variables: AccessIsChannelPointsAvailableQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class broadcastLanguageQuery(Endpoint):
	sha256Hash = '3aed462280ec05cd9b1417de77b30153bd7005cb5f9a460bb056a8d5d16f479c'
	operation_name = 'broadcastLanguageQuery'
	def build_query(self, variables: broadcastLanguageQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DashboardChannelSettings(Endpoint):
	sha256Hash = '160cd94d5cb8af45ef3149a256b18bbfed52976ed7eb12b7d97054138321a8c2'
	operation_name = 'DashboardChannelSettings'
	def build_query(self, variables: DashboardChannelSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AnnouncementsIcon(Endpoint):
	sha256Hash = '90d083f65aa77b5b5a9b914cf975088d7ddbba6af7d8813aed4b12e30daed33e'
	operation_name = 'AnnouncementsIcon'
	def build_query(self, variables: AnnouncementsIconRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsCommunityMomentsEnabledQuery(Endpoint):
	sha256Hash = '7c8a45cf71a20e785ad3e87b55735dc87ba98ade065228c8695cb132270bb1fd'
	operation_name = 'AccessIsCommunityMomentsEnabledQuery'
	def build_query(self, variables: AccessIsCommunityMomentsEnabledQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SponsorshipChannelSettings(Endpoint):
	sha256Hash = '87720be022792af239a885a73b35a055f092c487145c2ff1488926d4dfa1d5fc'
	operation_name = 'SponsorshipChannelSettings'
	def build_query(self, variables: SponsorshipChannelSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UserEmoticonPrefix_Query(Endpoint):
	sha256Hash = '6eb368f3a785c358509cc0da9ff56ac76d535e255196d496dd7312487d3abbe1'
	operation_name = 'UserEmoticonPrefix_Query'
	def build_query(self, variables: UserEmoticonPrefix_QueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Settings_ProfilePage_AccountInfoSettings(Endpoint):
	sha256Hash = '60a54ebcbd29e095db489ed6268f33d5fe5ed1d4fa3176668d8091587ae81779'
	operation_name = 'Settings_ProfilePage_AccountInfoSettings'
	def build_query(self, variables: Settings_ProfilePage_AccountInfoSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SocialMedia(Endpoint):
	sha256Hash = '924cfc5e3c14d282d4a552abee7a735efc2ccccaf6631f57cf778763df86abe5'
	operation_name = 'SocialMedia'
	def build_query(self, variables: SocialMediaRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UpgradeTermsBannerQuery(Endpoint):
	sha256Hash = '4e4f3984b61da54d3cc1b6fa88e044702ec71cf830836c2e144cf4308d1dcb32'
	operation_name = 'UpgradeTermsBannerQuery'
	def build_query(self, variables: UpgradeTermsBannerQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CopyrightSchoolInvitation(Endpoint):
	sha256Hash = '49df04ff9fb52456723d7a0108238fe68814b08595a99c7037709db87e7b8d9e'
	operation_name = 'CopyrightSchoolInvitation'
	def build_query(self, variables: CopyrightSchoolInvitationRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Settings_ChannelClipsSettings(Endpoint):
	sha256Hash = '6aa8956a88df8b878d45667d15d45bfe88dd220827a1da2a7880ed1710cf3aa8'
	operation_name = 'Settings_ChannelClipsSettings'
	def build_query(self, variables: Settings_ChannelClipsSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ProductConsent(Endpoint):
	sha256Hash = 'b6c80042ea0b3ba828c6f4f79ff22db35e8733aaf3d30c2215fbecfd2aa5e8cc'
	operation_name = 'ProductConsent'
	def build_query(self, variables: ProductConsentRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UsernameRenameStatus(Endpoint):
	sha256Hash = 'caed6a3d336fc50251da7b944462ea321d7f276ee6fcccdf7e2e3de4d6ab5204'
	operation_name = 'UsernameRenameStatus'
	def build_query(self, variables: UsernameRenameStatusRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class TaxExpiryQuery(Endpoint):
	sha256Hash = 'e8a6e5e68c2a2ec1d06d9afc5102107eba06a76ffedb747b24bb54baa4a0cfc4'
	operation_name = 'TaxExpiryQuery'
	def build_query(self, variables: TaxExpiryQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetBitsButton_Bits(Endpoint):
	sha256Hash = '1622ab9e754d97acfb154caaf3d9d583c44408a76be6d4aba5a67cdba4e72452'
	operation_name = 'GetBitsButton_Bits'
	def build_query(self, variables: GetBitsButton_BitsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatHighlightSettings(Endpoint):
	sha256Hash = 'fcd2e02d5b06c04876f3236ce019089ae5ae3e9d04d13764fc445cb8517f5e67'
	operation_name = 'ChatHighlightSettings'
	def build_query(self, variables: ChatHighlightSettingsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FollowPanelOverlay(Endpoint):
	sha256Hash = 'e7415fc096fdec8cf7b4b85bbab7bc24a72349eecee788b804c33f3a89ed9ca2'
	operation_name = 'FollowPanelOverlay'
	def build_query(self, variables: FollowPanelOverlayRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class DashboardInsights_Channel(Endpoint):
	sha256Hash = '3bf3a6ae9bef78cb0b6b04a5161bda159f9e7e3716bf24b1b1638b689347a837'
	operation_name = 'DashboardInsights_Channel'
	def build_query(self, variables: DashboardInsights_ChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SunlightHomePage(Endpoint):
	sha256Hash = '53b454d3f69df4c60d2cfc812bb6bffda16899a553c52b03b1e1b888b8877462'
	operation_name = 'SunlightHomePage'
	def build_query(self, variables: SunlightHomePageRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GuestStarFavoriteGuests(Endpoint):
	sha256Hash = '331436e1bf23d0b2ba8dd44114b9bf809d87c3ca18a9fccddcb1530dabe00fca'
	operation_name = 'GuestStarFavoriteGuests'
	def build_query(self, variables: GuestStarFavoriteGuestsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CreatorHomeGetEmoteData(Endpoint):
	sha256Hash = '258d3ae2b04dd237e2b7dc96ba01065f531880f6dfbce2c81239e6578d2a4f73'
	operation_name = 'CreatorHomeGetEmoteData'
	def build_query(self, variables: CreatorHomeGetEmoteDataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SunlightHomePageCards(Endpoint):
	sha256Hash = '1b26ef1f3ea5ed41a1ef4324d2751832da89f1c633b317af6b5cb56e71e603cc'
	operation_name = 'SunlightHomePageCards'
	def build_query(self, variables: SunlightHomePageCardsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ShieldModeState(Endpoint):
	sha256Hash = '509fa996346e0317fd748fbb55c3f6bc3cbbc739deaccf78dec53ea29977ce5f'
	operation_name = 'ShieldModeState'
	def build_query(self, variables: ShieldModeStateRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AchievementsPage(Endpoint):
	sha256Hash = '5f39ad08c580e5d6c048d43e483c6c076f379df81cfa35cad439bba012f86f2e'
	operation_name = 'AchievementsPage'
	def build_query(self, variables: AchievementsPageRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class StreamSummaryPage_GetRecentStreamSessions(Endpoint):
	sha256Hash = 'd2cfb73f2f2acde23a0cac3e5218be1241254e5738e5544d27d79a86c7e6274b'
	operation_name = 'StreamSummaryPage_GetRecentStreamSessions'
	def build_query(self, variables: StreamSummaryPage_GetRecentStreamSessionsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ArtistAttributionChannels(Endpoint):
	sha256Hash = '01db52b51afa3b3f73790219a72d31303837bae7bff5460a44ed68c954f378ee'
	operation_name = 'ArtistAttributionChannels'
	def build_query(self, variables: ArtistAttributionChannelsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UseCreatorHomeActionDataQuery(Endpoint):
	sha256Hash = '5241cd192bf92d6e8a2aac60c879166a9732a4da2a2e964f5f51ada61af5b5ad'
	operation_name = 'UseCreatorHomeActionDataQuery'
	def build_query(self, variables: UseCreatorHomeActionDataQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CreatorHomeSuggestedExtensions(Endpoint):
	sha256Hash = '04e3b82dc80f76443b215559bb03e59d4be28a67e97bebaa9ba811267bc74f70'
	operation_name = 'CreatorHomeSuggestedExtensions'
	def build_query(self, variables: CreatorHomeSuggestedExtensionsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SubscriptionsManagement_SubscriptionBenefits(Endpoint):
	sha256Hash = 'b21eec80bf7f902cc52c3f6552cd79b0b651b61bf891c9033efef22c8c8bcca6'
	operation_name = 'SubscriptionsManagement_SubscriptionBenefits'
	def build_query(self, variables: SubscriptionsManagement_SubscriptionBenefitsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UnbanRequestsListCtx(Endpoint):
	sha256Hash = '10d5c968108784e9fc9a3ffdb73995bdf725dae9e7dc8cd2e4328078842b26dd'
	operation_name = 'UnbanRequestsListCtx'
	def build_query(self, variables: UnbanRequestsListCtxRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Inventory(Endpoint):
	sha256Hash = '09acb7d3d7e605a92bdfdcc465f6aa481b71c234d8686a9ba38ea5ed51507592'
	operation_name = 'Inventory'
	def build_query(self, variables: InventoryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelSharedBans(Endpoint):
	sha256Hash = '080ac7253c6001f5f2a48bbb2bb4b3613f75fe5e734582275ea620aa163416b3'
	operation_name = 'ChannelSharedBans'
	def build_query(self, variables: ChannelSharedBansRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetGuestStarSessionQuery(Endpoint):
	sha256Hash = '294ffccd2c46c6dfe73a821435092881cbfc2816c5d836a1074abee4e05d5807'
	operation_name = 'GetGuestStarSessionQuery'
	def build_query(self, variables: GetGuestStarSessionQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SettingsTabs_User(Endpoint):
	sha256Hash = 'e18a181ca5ddd8e66aad35edce34dd8a38ff9e1ade1c4ff7361652765a003ee0'
	operation_name = 'SettingsTabs_User'
	def build_query(self, variables: SettingsTabs_UserRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ProfileImageSetting(Endpoint):
	sha256Hash = '3d814a91606062a51f71e90c9b5a2d6e86792f52dacd912967d458067b5db44d'
	operation_name = 'ProfileImageSetting'
	def build_query(self, variables: ProfileImageSettingRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ProfileBannerSetting(Endpoint):
	sha256Hash = '0144838d4c979ed9c0bbac8f52df180be711e4a0afd9fde81d70a73d0316627c'
	operation_name = 'ProfileBannerSetting'
	def build_query(self, variables: ProfileBannerSettingRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class PaymentMethodsTab_UserPaymentMethods(Endpoint):
	sha256Hash = 'b2714864c4ee35279c5a844d6430039af1b66abd58a3a351f4d50f5e6c1efe3b'
	operation_name = 'PaymentMethodsTab_UserPaymentMethods'
	def build_query(self, variables: PaymentMethodsTab_UserPaymentMethodsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SubscriptionsManagement_ExpiredSubscriptions(Endpoint):
	sha256Hash = 'b559221b9a4d9be19a6fd97f315251080468435617600ddc7645a868f59cca57'
	operation_name = 'SubscriptionsManagement_ExpiredSubscriptions'
	def build_query(self, variables: SubscriptionsManagement_ExpiredSubscriptionsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class WalletBalances(Endpoint):
	sha256Hash = 'ace88ded9def4e1311a9c5a0016933c8042c415c44fd97e77b2a440c11a6c592'
	operation_name = 'WalletBalances'
	def build_query(self, variables: WalletBalancesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelFollows(Endpoint):
	sha256Hash = 'eecf815273d3d949e5cf0085cc5084cd8a1b5b7b6f7990cf43cb0beadf546907'
	operation_name = 'ChannelFollows'
	def build_query(self, variables: ChannelFollowsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UserEmotes(Endpoint):
	sha256Hash = '7c15c1c83a9cf574aa202ddf6f40594ff75b2715746d98a20eea068e0c1179b7'
	operation_name = 'UserEmotes'
	def build_query(self, variables: UserEmotesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Whispers_Thread_WhisperThread(Endpoint):
	sha256Hash = 'c11d356f7e2d8a2b7da3f90c11487414b7fb188649bafe331e93937a5da2310d'
	operation_name = 'Whispers_Thread_WhisperThread'
	def build_query(self, variables: Union[Whispers_Thread_WhisperThreadRequest1, Whispers_Thread_WhisperThreadRequest2] = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class Whispers_Thread_User_Activity(Endpoint):
	sha256Hash = '16a95093b9a256d5f94e63cbc37ccfd2d0bf58f2c917a02760d5056147febcf7'
	operation_name = 'Whispers_Thread_User_Activity'
	def build_query(self, variables: Whispers_Thread_User_ActivityRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayer_MutedSegmentsAlertOverlay(Endpoint):
	sha256Hash = 'c36e7400657815f4704e6063d265dff766ed8fc1590361c6d71e4368805e0b49'
	operation_name = 'VideoPlayer_MutedSegmentsAlertOverlay'
	def build_query(self, variables: VideoPlayer_MutedSegmentsAlertOverlayRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CollectionCarouselQuery(Endpoint):
	sha256Hash = '0ca5b673f0a160f85267d7c5fbfe797f1d7b8129025aedc353cb5c99f2c94fec'
	operation_name = 'CollectionCarouselQuery'
	def build_query(self, variables: CollectionCarouselQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipMetadataBroadcastInfoQuery(Endpoint):
	sha256Hash = 'e6bc9b21fdd69a40fc572dff806f22e4bae0274176a033f7c75f906306a2ea32'
	operation_name = 'ClipMetadataBroadcastInfoQuery'
	def build_query(self, variables: ClipMetadataBroadcastInfoQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CreateRawMedia(Endpoint):
	sha256Hash = '7b1460dd6fddd362a306fc529bff6b8b2a96968e447a44db2bc1a7c61a04253b'
	operation_name = 'CreateRawMedia'
	def build_query(self, variables: CreateRawMediaRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class GetRawMedia(Endpoint):
	sha256Hash = '19b97ccabc93b998bad0add789290fc40ca20de9786ff614c63b5356fecc2520'
	operation_name = 'GetRawMedia'
	def build_query(self, variables: GetRawMediaRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsChannelEditorQuery(Endpoint):
	sha256Hash = '67cafaccfaf78e4315e1e3c5a27758bb8541b2f2f9b24aa8238f74993ff98556'
	operation_name = 'AccessIsChannelEditorQuery'
	def build_query(self, variables: AccessIsChannelEditorQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class AccessIsChannelModeratorQuery(Endpoint):
	sha256Hash = '78e1e80d0ed0e7819eaaa2fb8d73cd3da7e15ffe17241666128b757cd2a72a46'
	operation_name = 'AccessIsChannelModeratorQuery'
	def build_query(self, variables: AccessIsChannelModeratorQueryRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ReportMenuItem(Endpoint):
	sha256Hash = '784bde9b3aa7638b3d2a99da0b1e1cf2ade81a8a7423410bd165e5d860913195'
	operation_name = 'ReportMenuItem'
	def build_query(self, variables: ReportMenuItemRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ReportUserModal_ReportWizardData(Endpoint):
	sha256Hash = '53e3604167556125620dfc8ceed34ab2a14fb1bdbd16a66c62a3db6a2e862ea8'
	operation_name = 'ReportUserModal_ReportWizardData'
	def build_query(self, variables: ReportUserModal_ReportWizardDataRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class CategoryChannels_InternationalSection(Endpoint):
	sha256Hash = '6b33bfa29864d56e808ae18af5e2df8a1bf1cec7d84e48183d3824e9bf3dc7eb'
	operation_name = 'CategoryChannels_InternationalSection'
	def build_query(self, variables: CategoryChannels_InternationalSectionRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class UpcomingSchedule(Endpoint):
	sha256Hash = 'ff65081a553470bf2fc8c973b68547f3333fa37f2e1604d0151841e65a1438e2'
	operation_name = 'UpcomingSchedule'
	def build_query(self, variables: UpcomingScheduleRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class FeaturedUpcomingStreams(Endpoint):
	sha256Hash = 'bd4cc0f014f4e00431b93ef517e116d1b61e5045c1431ef8073b00526e8eb93c'
	operation_name = 'FeaturedUpcomingStreams'
	def build_query(self, variables: FeaturedUpcomingStreamsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChannelVideoCore(Endpoint):
	sha256Hash = 'cf1ccf6f5b94c94d662efec5223dfb260c9f8bf053239a76125a58118769e8e2'
	operation_name = 'ChannelVideoCore'
	def build_query(self, variables: ChannelVideoCoreRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ChatSettings_Badges(Endpoint):
	sha256Hash = 'a0300a9d8c43ec7a6bf653d46478948cc943d4ad9b2b28654241916b621dbfe5'
	operation_name = 'ChatSettings_Badges'
	def build_query(self, variables: ChatSettings_BadgesRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class BrowsePage_Popular(Endpoint):
	sha256Hash = '75a4899f0a765cc08576125512f710e157b147897c06f96325de72d4c5a64890'
	operation_name = 'BrowsePage_Popular'
	def build_query(self, variables: BrowsePage_PopularRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClipsCards__Game(Endpoint):
	sha256Hash = 'ebcf54afb9aa5d6cec8aad2c35b84e2737a109dac5b184308aae73a27d176707'
	operation_name = 'ClipsCards__Game'
	def build_query(self, variables: ClipsCards__GameRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerStreamInfoOverlayChannel(Endpoint):
	sha256Hash = 'e785b65ff71ad7b363b34878335f27dd9372869ad0c5740a130b9268bcdbe7e7'
	operation_name = 'VideoPlayerStreamInfoOverlayChannel'
	def build_query(self, variables: VideoPlayerStreamInfoOverlayChannelRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ExtensionsNotificationBitsBalance(Endpoint):
	sha256Hash = '41de55499885688ab4f7021c858e9ff430f2a9d151cc021a312317c326d11e22'
	operation_name = 'ExtensionsNotificationBitsBalance'
	def build_query(self, variables: ExtensionsNotificationBitsBalanceRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class SubscribedContext(Endpoint):
	sha256Hash = '56f8d2d143e1045284432c96830b3fdb811876efb03f9b5c8504a0cee4fd1bbb'
	operation_name = 'SubscribedContext'
	def build_query(self, variables: SubscribedContextRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class ClientSideAdEventHandling_RecordAdEvent(Endpoint):
	sha256Hash = '7e6c69e6eb59f8ccb97ab73686f3d8b7d85a72a0298745ccd8bfc68e4054ca5b'
	operation_name = 'ClientSideAdEventHandling_RecordAdEvent'
	def build_query(self, variables: ClientSideAdEventHandling_RecordAdEventRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

class VideoPlayerVODPostplayRecommendations(Endpoint):
	sha256Hash = '2e29be981ae55ea4cf78cda648afa156928508c3cb03c6ca5c1726fdef1183d8'
	operation_name = 'VideoPlayerVODPostplayRecommendations'
	def build_query(self, variables: VideoPlayerVODPostplayRecommendationsRequest = {}) -> dict:
		draft = self.draft.copy(); draft['variables'] = variables
		return draft

\
class videoPlaybackAccessToken(Endpoint):
	def __init__(self):
		self.draft = '''{{"query": "{{\\n              videoPlaybackAccessToken(\\n                id: \\"{}\\",\\n                params: {{\\n                  platform: \\"web\\",\\n                  playerBackend: \\"mediaplayer\\",\\n                  playerType: \\"site\\"\\n                }}\\n              )\\n              {{\\n                value\\n                signature\\n              }}\\n            }}"}}'''

	def build_query(self, vod_id: str):
		return self.draft.format(vod_id)

class Endpoints:
	"""Placeholder for all endpoints in current module"""
	amount = 312
	Consent = Consent()
	Ads_Components_AdManager_User = Ads_Components_AdManager_User()
	Prime_PrimeOffers_CurrentUser = Prime_PrimeOffers_CurrentUser()
	UserMenuCurrentUser = UserMenuCurrentUser()
	TopNav_CurrentUser = TopNav_CurrentUser()
	StoryPreviewsWithOrder = StoryPreviewsWithOrder()
	SideNav = SideNav()
	FrontPageNew_User = FrontPageNew_User()
	Shelves = Shelves()
	PrefetchPlaybackAccessToken = PrefetchPlaybackAccessToken()
	GuestStarBatchCollaborationQuery = GuestStarBatchCollaborationQuery()
	CoreActionsCurrentUser = CoreActionsCurrentUser()
	FeaturedContentCarouselStreams = FeaturedContentCarouselStreams()
	TrackingManager_RequestInfo = TrackingManager_RequestInfo()
	Prime_PrimeOffers_PrimeOfferIds_Eligibility = Prime_PrimeOffers_PrimeOfferIds_Eligibility()
	ChannelPage_SetSessionStatus = ChannelPage_SetSessionStatus()
	Core_Services_Spade_CurrentUser = Core_Services_Spade_CurrentUser()
	DMCAViolationCountBanner = DMCAViolationCountBanner()
	VerifyEmail_CurrentUser = VerifyEmail_CurrentUser()
	OnsiteNotifications_Summary = OnsiteNotifications_Summary()
	Whispers_Whispers_UserWhisperThreads = Whispers_Whispers_UserWhisperThreads()
	ConnectAdIdentityMutation = ConnectAdIdentityMutation()
	VideoPreviewOverlay = VideoPreviewOverlay()
	VideoAdBanner = VideoAdBanner()
	ContentPolicyPropertiesQuery = ContentPolicyPropertiesQuery()
	GetUserID = GetUserID()
	VideoPlayer_AgeGateOverlayBroadcaster = VideoPlayer_AgeGateOverlayBroadcaster()
	VideoPlayer_VideoSourceManager = VideoPlayer_VideoSourceManager()
	VideoPlayerPixelAnalyticsUrls = VideoPlayerPixelAnalyticsUrls()
	StreamRefetchManager = StreamRefetchManager()
	AdRequestHandling = AdRequestHandling()
	NielsenContentMetadata = NielsenContentMetadata()
	ChannelSkins = ChannelSkins()
	ExtensionsUIContext_ChannelID = ExtensionsUIContext_ChannelID()
	PlayerTrackingContextQuery = PlayerTrackingContextQuery()
	ContentClassificationContext = ContentClassificationContext()
	VideoPlayerStreamMetadata = VideoPlayerStreamMetadata()
	ActiveWatchParty = ActiveWatchParty()
	VideoPlayerClipsButtonBroadcaster = VideoPlayerClipsButtonBroadcaster()
	SyncedSettingsCelebrations = SyncedSettingsCelebrations()
	CelebrationContextChannelID = CelebrationContextChannelID()
	GetDisplayName = GetDisplayName()
	PlaybackAccessToken = PlaybackAccessToken()
	ExtensionsForChannel = ExtensionsForChannel()
	CelebrationEmotes = CelebrationEmotes()
	ChannelProductsWithCommunityGiftOffers = ChannelProductsWithCommunityGiftOffers()
	RecapEligibilityQuery = RecapEligibilityQuery()
	BitsConfigContext_Global = BitsConfigContext_Global()
	BitsConfigContext_Channel = BitsConfigContext_Channel()
	ChannelShell = ChannelShell()
	UseLive = UseLive()
	UseViewCount = UseViewCount()
	ExtensionsOverlay = ExtensionsOverlay()
	StreamTagsTrackingChannel = StreamTagsTrackingChannel()
	VideoPlayerStatusOverlayChannel = VideoPlayerStatusOverlayChannel()
	DropCurrentSessionContext = DropCurrentSessionContext()
	GetIDFromLogin = GetIDFromLogin()
	SubsidizedSubscriptions = SubsidizedSubscriptions()
	ChatScreenReaderAutoAnnounce = ChatScreenReaderAutoAnnounce()
	SharedChatModeratorStrikes = SharedChatModeratorStrikes()
	ChatInput = ChatInput()
	CurrentUserBannedStatus = CurrentUserBannedStatus()
	ChatList_ActiveCharityCampaign = ChatList_ActiveCharityCampaign()
	GlobalBadges = GlobalBadges()
	ChatList_Badges = ChatList_Badges()
	ChatRestrictions = ChatRestrictions()
	BlockedUsers = BlockedUsers()
	MessageBufferChatHistory = MessageBufferChatHistory()
	MessageBuffer_Channel = MessageBuffer_Channel()
	PollChannelSettings = PollChannelSettings()
	CommunityPointsRewardRedemptionContext = CommunityPointsRewardRedemptionContext()
	ChannelPointsPredictionContext = ChannelPointsPredictionContext()
	ChannelPointsContext = ChannelPointsContext()
	ChannelPointsGlobalContext = ChannelPointsGlobalContext()
	SyncedSettingsChatPauseSetting = SyncedSettingsChatPauseSetting()
	SyncedSettingsDeletedMessageDisplaySetting = SyncedSettingsDeletedMessageDisplaySetting()
	SyncedSettingsEmoteAnimations = SyncedSettingsEmoteAnimations()
	SyncedSettingsReadableChatColors = SyncedSettingsReadableChatColors()
	ChatRoomState = ChatRoomState()
	Chat_UserData = Chat_UserData()
	Chat_ChannelData = Chat_ChannelData()
	CommonHooks_BlockedUsers = CommonHooks_BlockedUsers()
	PinnedCheersSettings = PinnedCheersSettings()
	CurrentUserStrikeStatus = CurrentUserStrikeStatus()
	StreamChat = StreamChat()
	OneTapFeed = OneTapFeed()
	SharedChatSession = SharedChatSession()
	ChannelCollaborationEligibilityQuery = ChannelCollaborationEligibilityQuery()
	GetHypeTrainExecutionV2 = GetHypeTrainExecutionV2()
	StoryPreviewChannel = StoryPreviewChannel()
	StreamEventCelebrationsChannelPageBadge = StreamEventCelebrationsChannelPageBadge()
	GuestStarActiveJoinRequest = GuestStarActiveJoinRequest()
	GuestStarChannelPageCollaborationQuery = GuestStarChannelPageCollaborationQuery()
	ChatRoomBanStatus = ChatRoomBanStatus()
	GuestListQuery = GuestListQuery()
	ChannelPage_SubscribeButton_User = ChannelPage_SubscribeButton_User()
	ChannelActiveCharityCampaign = ChannelActiveCharityCampaign()
	RealtimeStreamTagList = RealtimeStreamTagList()
	StreamMetadata = StreamMetadata()
	UseLiveBroadcast = UseLiveBroadcast()
	WatchTrackQuery = WatchTrackQuery()
	TurboAndSubUpsell = TurboAndSubUpsell()
	UserModStatus = UserModStatus()
	CommunityOnboardingAllowlist = CommunityOnboardingAllowlist()
	GetPinnedChat = GetPinnedChat()
	PinnedChatSettings = PinnedChatSettings()
	AvailableEmotesForChannelPaginated = AvailableEmotesForChannelPaginated()
	EmotesForChannelFollowStatus = EmotesForChannelFollowStatus()
	CurrentUserModeratorStatus = CurrentUserModeratorStatus()
	WithIsStreamLiveQuery = WithIsStreamLiveQuery()
	ChannelPollContext_GetViewablePoll = ChannelPollContext_GetViewablePoll()
	LastUnbanRequest = LastUnbanRequest()
	EmotePicker_EmotePicker_UserSubscriptionProducts = EmotePicker_EmotePicker_UserSubscriptionProducts()
	BitsCard_Bits = BitsCard_Bits()
	ChatModeratorStrikeStatus = ChatModeratorStrikeStatus()
	Chat_OrbisPresetText = Chat_OrbisPresetText()
	CommunitySupportSettings = CommunitySupportSettings()
	ClipsExperimentEnrollmentStatus = ClipsExperimentEnrollmentStatus()
	PaidPinnedChat = PaidPinnedChat()
	ChannelRoot_AboutPanel = ChannelRoot_AboutPanel()
	ActiveGoals = ActiveGoals()
	DropsHighlightService_AvailableDrops = DropsHighlightService_AvailableDrops()
	ShoutoutHighlightServiceQuery = ShoutoutHighlightServiceQuery()
	ChatInput_Badges = ChatInput_Badges()
	TitleMentions = TitleMentions()
	FollowButton_User = FollowButton_User()
	PartnerPlusPublicQuery = PartnerPlusPublicQuery()
	CanCreateClip = CanCreateClip()
	PersistentGoalFollowButton_User = PersistentGoalFollowButton_User()
	WatchStreakExperiment = WatchStreakExperiment()
	Chat_ShareBitsBadgeTier_ChannelData = Chat_ShareBitsBadgeTier_ChannelData()
	Chat_ShareResub_ChannelData = Chat_ShareResub_ChannelData()
	GetGuestSessionBlocksAndBans = GetGuestSessionBlocksAndBans()
	ChannelPointsAutomaticRewards = ChannelPointsAutomaticRewards()
	ChannelLeaderboards = ChannelLeaderboards()
	BannerNotificationQuery = BannerNotificationQuery()
	StoryChannelQuery = StoryChannelQuery()
	ChannelSupportButtons = ChannelSupportButtons()
	AcknowledgeUnbanRequestPrompt = AcknowledgeUnbanRequestPrompt()
	VideoMarkersChatCommand = VideoMarkersChatCommand()
	CommercialCommandHandler_ChannelData = CommercialCommandHandler_ChannelData()
	AccessIsAffiliateQuery = AccessIsAffiliateQuery()
	AccessIsPartnerQuery = AccessIsPartnerQuery()
	CommunityPointsChatPrivateCalloutUser = CommunityPointsChatPrivateCalloutUser()
	Chat_EarnedBadges_InitialSubStatus = Chat_EarnedBadges_InitialSubStatus()
	StreamEventsActiveCelebrationCalloutQuery = StreamEventsActiveCelebrationCalloutQuery()
	CollaborationPromoPrivateCallout = CollaborationPromoPrivateCallout()
	CommunityPointsAvailableClaim = CommunityPointsAvailableClaim()
	ExtensionsInfoBalloon = ExtensionsInfoBalloon()
	updateUserViewedVideo = updateUserViewedVideo()
	ChannelPanels = ChannelPanels()
	ExtensionProducts = ExtensionProducts()
	HomeOfflineCarousel = HomeOfflineCarousel()
	ChannelAvatar = ChannelAvatar()
	LowerHomeHeader = LowerHomeHeader()
	RoleRestricted = RoleRestricted()
	ChannelVideoShelvesQuery = ChannelVideoShelvesQuery()
	HomeTrackQuery = HomeTrackQuery()
	ChatFilterContextManager_User = ChatFilterContextManager_User()
	PbyPGame = PbyPGame()
	FeaturedClipsShelfCover = FeaturedClipsShelfCover()
	VideoPreviewCard__VideoMoments = VideoPreviewCard__VideoMoments()
	ClipsCards__User = ClipsCards__User()
	StreamSchedule = StreamSchedule()
	FilterableVideoTower_Videos = FilterableVideoTower_Videos()
	queryUserViewedVideo = queryUserViewedVideo()
	VODMidrollManager = VODMidrollManager()
	VideoPlayer_VODSeekbar = VideoPlayer_VODSeekbar()
	VideoPlayer_ChapterSelectButtonVideo = VideoPlayer_ChapterSelectButtonVideo()
	VideoComments = VideoComments()
	VideoCommentsByOffsetOrCursor = VideoCommentsByOffsetOrCursor()
	VideoMetadata = VideoMetadata()
	VideoPlayer_VODSeekbarPreviewVideo = VideoPlayer_VODSeekbarPreviewVideo()
	VideoAdRequestDecline = VideoAdRequestDecline()
	FollowedIndex_CurrentUser = FollowedIndex_CurrentUser()
	FollowedIndex_FollowCount = FollowedIndex_FollowCount()
	FollowingGames_CurrentUser = FollowingGames_CurrentUser()
	FollowingLive_CurrentUser = FollowingLive_CurrentUser()
	FollowedVideos_CurrentUser = FollowedVideos_CurrentUser()
	FollowingPage_RecommendedChannels = FollowingPage_RecommendedChannels()
	FollowedStreamsContinueWatching = FollowedStreamsContinueWatching()
	FollowedStreams = FollowedStreams()
	BrowsePage_AllDirectories = BrowsePage_AllDirectories()
	BrowseVerticalDirectory = BrowseVerticalDirectory()
	DirectoryCollection_BrowsableCollection = DirectoryCollection_BrowsableCollection()
	HomeShelfEditor = HomeShelfEditor()
	HomeShelfUsers = HomeShelfUsers()
	HomeShelfVideos = HomeShelfVideos()
	HomeShelfGames = HomeShelfGames()
	OfflineBannerOverlay = OfflineBannerOverlay()
	VideoPlayerOfflineRecommendationsOverlay = VideoPlayerOfflineRecommendationsOverlay()
	ChannelClipCore = ChannelClipCore()
	VideoAccessToken_Clip = VideoAccessToken_Clip()
	ClipMetadata = ClipMetadata()
	ShareClipRenderStatus = ShareClipRenderStatus()
	ChatClip = ChatClip()
	CanViewersExportQuery = CanViewersExportQuery()
	AccessGetFeatureClipRestrictionsQuery = AccessGetFeatureClipRestrictionsQuery()
	incrementClipViewCount = incrementClipViewCount()
	HappeningNowSettings = HappeningNowSettings()
	ClaimCommunityPoints = ClaimCommunityPoints()
	RewardCenter_BitsBalance = RewardCenter_BitsBalance()
	SupportPanelCheckoutService = SupportPanelCheckoutService()
	SupportPanelTrackingService = SupportPanelTrackingService()
	GiftSubscriptionRewardPreviews = GiftSubscriptionRewardPreviews()
	SupportPanelCommunityGifting_GiftingOptions = SupportPanelCommunityGifting_GiftingOptions()
	SupportPanelSubTokenBalance = SupportPanelSubTokenBalance()
	OneClickEligibility = OneClickEligibility()
	SupportPanelSubTokenOffers = SupportPanelSubTokenOffers()
	SupportPanelCommunityGifting_GifterBadgeProgress = SupportPanelCommunityGifting_GifterBadgeProgress()
	FollowButton_UnfollowUser = FollowButton_UnfollowUser()
	FollowButton_FollowUser = FollowButton_FollowUser()
	SupportPanelTitleSectionAvatar = SupportPanelTitleSectionAvatar()
	SubscriptionRewardPreviews = SubscriptionRewardPreviews()
	SupportPanelSubscribeViewFooterPrime = SupportPanelSubscribeViewFooterPrime()
	SupportPanelFooterPrimeStatus = SupportPanelFooterPrimeStatus()
	PersonalSectionsHypeTrains = PersonalSectionsHypeTrains()
	MinimalTopNav_MinimalUser = MinimalTopNav_MinimalUser()
	TurboProductInformation = TurboProductInformation()
	Sub_Analytics = Sub_Analytics()
	ChannelSocialButtons = ChannelSocialButtons()
	RewardList = RewardList()
	SearchTray_SearchSuggestions = SearchTray_SearchSuggestions()
	SearchResultsPage_SearchResults = SearchResultsPage_SearchResults()
	LiveNotificationsToggle_User = LiveNotificationsToggle_User()
	Directory_DirectoryBanner = Directory_DirectoryBanner()
	DirectoryPage_Game = DirectoryPage_Game()
	DirectoryRoot_Directory = DirectoryRoot_Directory()
	FollowGameButton_Game = FollowGameButton_Game()
	DirectoryVideos_Game = DirectoryVideos_Game()
	Prime_PrimeOfferList_PrimeOffers_Eligibility = Prime_PrimeOfferList_PrimeOffers_Eligibility()
	OnsiteNotifications_View = OnsiteNotifications_View()
	OnsiteNotifications_ListNotifications = OnsiteNotifications_ListNotifications()
	SettingsNotificationsPage_User = SettingsNotificationsPage_User()
	SmartNotificationSettings_User = SmartNotificationSettings_User()
	PlatformNotificationSettings_User = PlatformNotificationSettings_User()
	AdvancedNotificationSettings_User = AdvancedNotificationSettings_User()
	UserDJStatusQuery = UserDJStatusQuery()
	SunlightLoggedInUserMenuQuery = SunlightLoggedInUserMenuQuery()
	HasNewBountiesContextQuery = HasNewBountiesContextQuery()
	AccessIsBountiesEnabledQuery = AccessIsBountiesEnabledQuery()
	CharityNavItem = CharityNavItem()
	AccessIsExtensionsDeveloperQuery = AccessIsExtensionsDeveloperQuery()
	AccessIsSiteAdminQuery = AccessIsSiteAdminQuery()
	AccessGetUserQuery = AccessGetUserQuery()
	Dashboard_CensusGetBirthdate = Dashboard_CensusGetBirthdate()
	AccessIsChannelPointsAvailableQuery = AccessIsChannelPointsAvailableQuery()
	broadcastLanguageQuery = broadcastLanguageQuery()
	DashboardChannelSettings = DashboardChannelSettings()
	AnnouncementsIcon = AnnouncementsIcon()
	AccessIsCommunityMomentsEnabledQuery = AccessIsCommunityMomentsEnabledQuery()
	SponsorshipChannelSettings = SponsorshipChannelSettings()
	UserEmoticonPrefix_Query = UserEmoticonPrefix_Query()
	Settings_ProfilePage_AccountInfoSettings = Settings_ProfilePage_AccountInfoSettings()
	SocialMedia = SocialMedia()
	UpgradeTermsBannerQuery = UpgradeTermsBannerQuery()
	CopyrightSchoolInvitation = CopyrightSchoolInvitation()
	Settings_ChannelClipsSettings = Settings_ChannelClipsSettings()
	ProductConsent = ProductConsent()
	UsernameRenameStatus = UsernameRenameStatus()
	TaxExpiryQuery = TaxExpiryQuery()
	GetBitsButton_Bits = GetBitsButton_Bits()
	ChatHighlightSettings = ChatHighlightSettings()
	FollowPanelOverlay = FollowPanelOverlay()
	DashboardInsights_Channel = DashboardInsights_Channel()
	SunlightHomePage = SunlightHomePage()
	GuestStarFavoriteGuests = GuestStarFavoriteGuests()
	CreatorHomeGetEmoteData = CreatorHomeGetEmoteData()
	SunlightHomePageCards = SunlightHomePageCards()
	ShieldModeState = ShieldModeState()
	AchievementsPage = AchievementsPage()
	StreamSummaryPage_GetRecentStreamSessions = StreamSummaryPage_GetRecentStreamSessions()
	ArtistAttributionChannels = ArtistAttributionChannels()
	UseCreatorHomeActionDataQuery = UseCreatorHomeActionDataQuery()
	CreatorHomeSuggestedExtensions = CreatorHomeSuggestedExtensions()
	SubscriptionsManagement_SubscriptionBenefits = SubscriptionsManagement_SubscriptionBenefits()
	UnbanRequestsListCtx = UnbanRequestsListCtx()
	Inventory = Inventory()
	ChannelSharedBans = ChannelSharedBans()
	GetGuestStarSessionQuery = GetGuestStarSessionQuery()
	SettingsTabs_User = SettingsTabs_User()
	ProfileImageSetting = ProfileImageSetting()
	ProfileBannerSetting = ProfileBannerSetting()
	PaymentMethodsTab_UserPaymentMethods = PaymentMethodsTab_UserPaymentMethods()
	SubscriptionsManagement_ExpiredSubscriptions = SubscriptionsManagement_ExpiredSubscriptions()
	WalletBalances = WalletBalances()
	ChannelFollows = ChannelFollows()
	UserEmotes = UserEmotes()
	Whispers_Thread_WhisperThread = Whispers_Thread_WhisperThread()
	Whispers_Thread_User_Activity = Whispers_Thread_User_Activity()
	VideoPlayer_MutedSegmentsAlertOverlay = VideoPlayer_MutedSegmentsAlertOverlay()
	CollectionCarouselQuery = CollectionCarouselQuery()
	ClipMetadataBroadcastInfoQuery = ClipMetadataBroadcastInfoQuery()
	CreateRawMedia = CreateRawMedia()
	GetRawMedia = GetRawMedia()
	AccessIsChannelEditorQuery = AccessIsChannelEditorQuery()
	AccessIsChannelModeratorQuery = AccessIsChannelModeratorQuery()
	ReportMenuItem = ReportMenuItem()
	ReportUserModal_ReportWizardData = ReportUserModal_ReportWizardData()
	CategoryChannels_InternationalSection = CategoryChannels_InternationalSection()
	UpcomingSchedule = UpcomingSchedule()
	FeaturedUpcomingStreams = FeaturedUpcomingStreams()
	ChannelVideoCore = ChannelVideoCore()
	ChatSettings_Badges = ChatSettings_Badges()
	BrowsePage_Popular = BrowsePage_Popular()
	ClipsCards__Game = ClipsCards__Game()
	VideoPlayerStreamInfoOverlayChannel = VideoPlayerStreamInfoOverlayChannel()
	ExtensionsNotificationBitsBalance = ExtensionsNotificationBitsBalance()
	SubscribedContext = SubscribedContext()
	ClientSideAdEventHandling_RecordAdEvent = ClientSideAdEventHandling_RecordAdEvent()
	VideoPlayerVODPostplayRecommendations = VideoPlayerVODPostplayRecommendations()
	videoPlaybackAccessToken = videoPlaybackAccessToken()
	...
