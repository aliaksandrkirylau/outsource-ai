# Question Bank: Mobile Application Discovery

**Purpose**: Curated questions for mobile app projects (iOS, Android, or cross-platform)

**Usage**: Select relevant questions based on project unknowns. Batch for discovery sessions.

---

## 1. Platform & Distribution Strategy

### Platform Selection
- [ ] iOS only, Android only, or both platforms?
- [ ] What's the priority platform (launch first)?
- [ ] Any platform-specific features (iOS widgets, Android home screen)?
- [ ] What minimum OS versions to support (iOS 14+, Android 10+)?

### Cross-Platform vs Native
- [ ] Native development or cross-platform (React Native, Flutter)?
- [ ] What's the deciding factor (performance, time-to-market, budget)?
- [ ] Are there platform-specific UI requirements?
- [ ] Do you need native modules or plugins?

### App Store Strategy
- [ ] What app store categories?
- [ ] Free app, paid app, or freemium?
- [ ] In-app purchases planned?
- [ ] Subscription model?
- [ ] What's the app store name and description concept?

---

## 2. Device & Hardware Integration

### Device Support
- [ ] Phone only, tablet only, or both?
- [ ] What screen sizes must be supported?
- [ ] Landscape orientation needed or portrait only?
- [ ] Support for foldable devices?

### Hardware Features
- [ ] Does the app need camera access?
  - Photo capture, video recording, or QR/barcode scanning?
- [ ] Does the app need location services?
  - Background location? Continuous tracking?
- [ ] Does the app need microphone access?
- [ ] Does the app use device sensors (accelerometer, gyroscope)?
- [ ] Does the app need Bluetooth connectivity?
- [ ] Does the app need NFC capabilities?
- [ ] Does the app need biometric authentication (Face ID, Touch ID, fingerprint)?

### Media & Files
- [ ] Can users take photos/videos within the app?
- [ ] Can users upload from photo library?
- [ ] What file types can users access (PDF, images, videos)?
- [ ] What's the maximum file size?
- [ ] Does the app play audio or video?

---

## 3. Offline Functionality

### Offline Requirements
- [ ] Must the app work offline?
- [ ] What features work offline vs require connection?
- [ ] How much data should be cached locally?
- [ ] What happens when user goes from offline to online?

### Data Synchronization
- [ ] How does offline data sync when back online?
- [ ] What happens if there are sync conflicts?
- [ ] Should users see sync status/progress?
- [ ] Can users force a manual sync?
- [ ] What's the sync frequency (real-time, periodic, manual)?

### Local Storage
- [ ] How much local storage is expected?
- [ ] What data persists between app sessions?
- [ ] Is local data encrypted?
- [ ] Can users clear local cache?

---

## 4. Push Notifications

### Notification Strategy
- [ ] Does the app send push notifications?
- [ ] What events trigger notifications?
- [ ] Time-sensitive vs standard notifications?
- [ ] Rich notifications (images, actions)?
- [ ] Notification categories or channels?

### User Control
- [ ] Can users control notification preferences?
- [ ] Granular control (by category) or all/none?
- [ ] Quiet hours or do-not-disturb?
- [ ] In-app notification center?

### Notification Infrastructure
- [ ] Push notification service (Firebase, APNs, OneSignal)?
- [ ] Notification analytics needed?
- [ ] Deep linking from notifications?

---

## 5. Authentication & Security

### User Authentication
- [ ] How do users sign up (email, phone, social)?
- [ ] Social login providers (Google, Apple, Facebook)?
- [ ] Phone number verification (SMS OTP)?
- [ ] Email verification required?
- [ ] Apple Sign-In required (iOS App Store requirement if other social logins)?

### Session Management
- [ ] How long do sessions last?
- [ ] Remember me / stay logged in?
- [ ] Biometric login (Face ID, Touch ID)?
- [ ] PIN or pattern lock?
- [ ] Multi-device login allowed?

### Security Requirements
- [ ] Is sensitive data stored locally?
- [ ] Certificate pinning needed?
- [ ] Root/jailbreak detection needed?
- [ ] Secure enclave usage?
- [ ] Screen capture blocking for sensitive screens?

---

## 6. Performance & Technical Requirements

### Performance Expectations
- [ ] Maximum app startup time?
- [ ] Maximum screen load time?
- [ ] How many concurrent users expected?
- [ ] What's acceptable for slow network (3G)?

### Battery & Data Usage
- [ ] Any battery usage constraints?
- [ ] Should app work well on low-power mode?
- [ ] Data usage concerns (cellular data limits)?
- [ ] Ability to use app on wifi-only?

### App Size
- [ ] Maximum acceptable app download size?
- [ ] On-demand resources or app slicing needed?
- [ ] Will there be large asset downloads post-install?

---

## 7. User Experience & Navigation

### Navigation Pattern
- [ ] Tab bar navigation, hamburger menu, or other?
- [ ] How many main sections/tabs?
- [ ] Bottom navigation or top navigation?
- [ ] Search functionality location and behavior?

### Gestures & Interactions
- [ ] Swipe gestures needed (swipe to delete, pull to refresh)?
- [ ] Long-press actions?
- [ ] Pinch to zoom?
- [ ] Drag and drop?
- [ ] Shake to trigger action?

### Accessibility
- [ ] VoiceOver / TalkBack support required?
- [ ] Dynamic text sizing support?
- [ ] Color contrast requirements?
- [ ] Voice control support?
- [ ] Any regulatory accessibility requirements?

---

## 8. Background Functionality

### Background Tasks
- [ ] Does app need to run in background?
- [ ] Background data sync?
- [ ] Background location tracking?
- [ ] Background audio playback?
- [ ] Background downloads?

### App Lifecycle
- [ ] What happens when app goes to background?
- [ ] What happens when app returns from background?
- [ ] Does app state need to be preserved?
- [ ] How long can app be in background before reset?

---

## 9. Social & Sharing Features

### Social Integration
- [ ] Share content to social media?
- [ ] Which platforms (Facebook, Instagram, Twitter, LinkedIn)?
- [ ] Share via messaging apps (WhatsApp, Messenger)?
- [ ] Share via email or SMS?
- [ ] Deep linking from shared content?

### In-App Social
- [ ] User profiles?
- [ ] Follow/friend system?
- [ ] Activity feeds?
- [ ] Comments or reactions?
- [ ] User-to-user messaging?

---

## 10. App Updates & Versioning

### Update Strategy
- [ ] Force update for critical versions?
- [ ] Optional update prompts?
- [ ] How often are updates expected?
- [ ] Backward compatibility requirements?
- [ ] Can different versions coexist on backend?

### Feature Flags
- [ ] Remote feature toggles needed?
- [ ] A/B testing capabilities?
- [ ] Gradual rollout of features?
- [ ] Kill switch for problematic features?

---

## 11. Analytics & Monitoring

### Analytics Requirements
- [ ] What analytics platform (Firebase, Mixpanel, Amplitude)?
- [ ] What user events to track?
- [ ] Screen view tracking?
- [ ] User journey/funnel tracking?
- [ ] Custom event properties?

### Error Monitoring
- [ ] Crash reporting tool (Crashlytics, Sentry)?
- [ ] Performance monitoring?
- [ ] Network call monitoring?
- [ ] User feedback/bug reporting tool?

### Privacy & Compliance
- [ ] What analytics are GDPR/CCPA compliant?
- [ ] User opt-in/opt-out for analytics?
- [ ] Data retention policies?
- [ ] User data export/deletion capabilities?

---

## 12. Integrations & Third-Party Services

### External Services
- [ ] Payment processing (Stripe, Apple Pay, Google Pay)?
- [ ] Maps integration (Google Maps, Apple Maps, Mapbox)?
- [ ] Chat or messaging SDK?
- [ ] Video calling integration?
- [ ] Cloud storage (iCloud, Google Drive)?

### APIs & Backends
- [ ] Custom backend API?
- [ ] Backend-as-a-Service (Firebase, AWS Amplify, Supabase)?
- [ ] Real-time database or websockets?
- [ ] GraphQL or REST?
- [ ] API authentication method?

---

## 13. App Store Requirements

### iOS App Store
- [ ] Apple Developer account type (individual, organization)?
- [ ] Privacy policy URL required?
- [ ] App permissions explanations (why camera, location, etc.)?
- [ ] Age rating considerations?
- [ ] TestFlight beta testing planned?

### Google Play Store
- [ ] Google Play Developer account?
- [ ] Content rating requirements?
- [ ] Privacy policy requirements?
- [ ] App signing strategy (Google Play or self-managed)?
- [ ] Internal testing / closed beta planned?

### Compliance
- [ ] COPPA compliance (children under 13)?
- [ ] GDPR compliance needed?
- [ ] Health data regulations (HIPAA)?
- [ ] Financial regulations (PCI-DSS)?
- [ ] Any region-specific regulations (China, EU)?

---

## 14. Launch & Marketing

### Pre-Launch
- [ ] Soft launch strategy (specific countries first)?
- [ ] Beta testing program?
- [ ] App preview video needed?
- [ ] Screenshot requirements (multiple device sizes)?
- [ ] App Store Optimization (ASO) strategy?

### Launch Support
- [ ] Launch date target?
- [ ] Marketing website or landing page?
- [ ] Press kit needed?
- [ ] Support email or system ready?
- [ ] FAQ or help documentation?

---

## 15. Post-Launch Operations

### Support & Maintenance
- [ ] In-app help or support chat?
- [ ] How do users report issues?
- [ ] Customer support ticketing system?
- [ ] Expected response time for support?
- [ ] App rating/review prompts?

### Content Management
- [ ] Does content update without app updates?
- [ ] CMS for dynamic content?
- [ ] Localized content by region?
- [ ] Scheduled content publishing?

### Monitoring & Response
- [ ] App Store review monitoring?
- [ ] Social media monitoring?
- [ ] Response plan for negative reviews?
- [ ] Rollback plan for bad releases?

---

## Platform-Specific Considerations

### iOS-Specific
- [ ] iPad-specific layouts needed?
- [ ] Apple Watch companion app?
- [ ] Widgets (home screen, lock screen)?
- [ ] Siri integration or shortcuts?
- [ ] CarPlay integration?
- [ ] iCloud sync?
- [ ] Handoff between devices?

### Android-Specific
- [ ] Wear OS companion app?
- [ ] Home screen widgets?
- [ ] Android Auto integration?
- [ ] Custom quick settings tiles?
- [ ] App shortcuts (long-press icon)?
- [ ] Support for different Android UI layers (Samsung One UI, MIUI)?

---

## Using This Question Bank

### For Projects with High Unknowns (>60%)
**Use**: Sections 1-5 heavily (core platform decisions)  
**Goal**: Define platform, offline strategy, and core UX

### For Projects with Moderate Clarity (30-60%)
**Use**: Sections 6-10 (technical depth)  
**Goal**: Understand performance needs and background functionality

### For Nearly Complete Projects (<30%)
**Use**: Sections 11-15 (launch and operations)  
**Goal**: Prepare for app store submission and post-launch

---

## Tips for Mobile App Discovery Sessions

1. **Show examples** - Pull out your phone and demo similar apps
2. **Discuss platform early** - iOS vs Android vs both affects budget 3x
3. **Clarify offline needs** - Huge technical implications, often underestimated
4. **Push notification strategy** - Can be overwhelming, need clear priority
5. **App store requirements** - Many clients unaware of Apple/Google policies
6. **Consider phased approach** - Maybe iOS first, Android later (or vice versa)

---

## Mobile App MVP Scoping Framework

**Must-Have for MVP**:
- Core user value (the main thing app does)
- Basic authentication
- Essential notifications
- Crash reporting

**Probably MVP**:
- Offline mode (if core to value prop)
- Social sharing (if growth mechanism)
- Basic settings/preferences

**Likely Post-MVP**:
- Widgets
- Wearable companions
- Advanced gestures
- Multiple themes
- Extensive customization

---

**Related**:
- [Web App Questions](Web_App_Questions.md)
- [SaaS Questions](SaaS_Questions.md)
- [Integration Questions](Integration_Questions.md)
- [Open Questions Template](../../03_Discussions/Open_Questions.md)


