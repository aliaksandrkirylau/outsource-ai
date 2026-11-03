# Designs Folder - README

**Purpose**: Optional folder for storing UI/UX design artifacts alongside your specification.

---

## What Goes in This Folder?

**Design artifacts that support your requirements:**

- Wireframes (low-fidelity mockups)
- Mockups (high-fidelity designs)
- User flow diagrams
- Prototypes (interactive designs)
- Design system assets
- Screenshots (reference designs, competitors)
- Style guides

---

## When to Use This Folder

### Use This Folder When:
- [ ] **You have design artifacts** from client or designer
- [ ] **You're creating wireframes** to clarify requirements
- [ ] **Client provides reference designs** or screenshots
- [ ] **Multiple design iterations** need tracking
- [ ] **Design review process** requires organized storage

### Don't Use This Folder When:
- [no] No designs exist yet (empty folder is fine)
- [no] Designs are in Figma/design tool only (link in specs instead)
- [no] Solo project with designs in your head (document in feature specs)
- [no] Designs are continuously changing (use design tool, not files)

> **Rule of thumb**: Use this folder as a **repository**, not a design tool. Active design work happens in Figma/Sketch/etc.

---

## Folder Organization

**Recommended structure:**

```
04_Designs/
|-- Wireframes/
|   |-- Home_v1.png
|   |-- Dashboard_v1.png
|   +-- UserProfile_v1.png
|
|-- Mockups/
|   |-- Epic-01_UserManagement/
|   |   |-- Login.png
|   |   +-- Registration.png
|   +-- Epic-02_Dashboard/
|       +-- Dashboard_Final.png
|
|-- Flows/
|   |-- UserOnboarding_Flow.png
|   +-- CheckoutProcess_Flow.png
|
|-- Reference/
|   |-- Competitor_A_Homepage.png
|   +-- Competitor_B_Dashboard.png
|
+-- StyleGuide/
    |-- ColorPalette.png
    +-- Typography.png
```

---

## File Naming Conventions

### Wireframes
- **Format**: `[Screen/Feature]_v[N].png`
- **Examples**: 
  - `Home_v1.png`
  - `Dashboard_v2.png`
  - `Settings_v1.pdf`

### Mockups
- **Format**: `[Epic-NN]_[Feature]_[State].png`
- **Examples**:
  - `Epic-01_Login_Default.png`
  - `Epic-01_Login_Error.png`
  - `Epic-02_Dashboard_Empty.png`

### Flows
- **Format**: `[ProcessName]_Flow_v[N].png`
- **Examples**:
  - `UserOnboarding_Flow_v1.png`
  - `CheckoutProcess_Flow_v2.pdf`

### Reference
- **Format**: `Reference_[Source]_[What].png`
- **Examples**:
  - `Reference_Airbnb_Homepage.png`
  - `Reference_Stripe_Checkout.png`

---

## Linking Designs to Specs

**Reference design files from your Epic/Feature files:**

### In Epic Files
```markdown
## UI/UX Considerations

**Design References**:
- Wireframes: `04_Designs/Wireframes/Dashboard_v1.png`
- User flow: `04_Designs/Flows/UserOnboarding_Flow_v1.png`

**Design Inspiration**:
- Similar to: `04_Designs/Reference/Reference_Notion_Dashboard.png`
```

### In Feature Files
```markdown
## UI/UX Notes

**Mockups**:
- Default state: `04_Designs/Mockups/Epic-01_UserManagement/Login.png`
- Error state: `04_Designs/Mockups/Epic-01_UserManagement/Login_Error.png`

**Interactions**:
- Click "Login" -> validate -> show loading -> redirect
- See flow diagram: `04_Designs/Flows/Authentication_Flow_v1.png`
```

---

## Design Sources & Tools

### If Using Design Tools

**Don't duplicate files - link instead:**

```markdown
## Design Links

**Figma**: https://figma.com/file/abc123/ProjectName
- Page: User Management Screens
- Last Updated: 2025-12-31

**Miro (Flows)**: https://miro.com/board/xyz789/
- User Onboarding Flow
- Purchase Flow

**Exported Snapshots**: `04_Designs/Exports/` (for reference only)
```

> **Best practice**: Keep designs in design tools, export snapshots to this folder for specification reviews.

---

## When to Export Designs Here

### Good Reasons to Export:
- [x] **Client review**: Need to share designs without design tool access
- [x] **Version snapshots**: Preserving design decisions at milestones
- [x] **Developer handoff**: Final approved designs for implementation
- [x] **Documentation**: Archiving what was designed vs. what was built

### Bad Reasons to Export:
- [no] Active design iteration (keep in tool)
- [no] Every minor change (too many files)
- [no] "Just in case" (no clear purpose)

---

## Design Versioning

**Track design iterations:**

### Option 1: Version Numbers in Filename
```
Home_v1.png  -> Initial wireframe
Home_v2.png  -> After client feedback
Home_v3.png  -> After usability review
Home_Final.png  -> Approved for development
```

### Option 2: Date-Based
```
Dashboard_2025-12-01.png
Dashboard_2025-12-15.png  <- After revisions
Dashboard_2025-12-31_Final.png
```

### Option 3: Milestone-Based Folders
```
04_Designs/
|-- 01_Initial_Wireframes/
|-- 02_Client_Review_Mockups/
|-- 03_Revised_Designs/
+-- 04_Final_Approved/
```

**Choose what works for your project** - consistency matters more than the method.

---

## Design Review Process

### 1. Before Client Review
```markdown
## Pre-Review Checklist
- [ ] All key screens designed
- [ ] Consistent UI patterns across screens
- [ ] Accessibility considerations addressed
- [ ] Mobile/responsive versions (if applicable)
- [ ] Designs exported to `04_Designs/Mockups/`
- [ ] Links added to Epic/Feature specs
```

### 2. Collecting Feedback
Create `04_Designs/Feedback/Design_Review_[Date].md`:

```markdown
# Design Review Feedback - 2025-12-31

## Attendees
- Client: John Doe
- Designer: Jane Smith
- BA: You

## Screen: Login (Epic-01)
- [x] Approved: Overall layout
- [~] Revise: "Forgot Password" link should be more prominent
- [?] Question: Do we need social login buttons?

## Screen: Dashboard (Epic-02)
- [x] Approved
- [~] Revise: Add empty state illustration

## Action Items
1. Revise Login screen - more prominent password reset
2. Add empty state to Dashboard
3. Clarify social login requirements
```

### 3. After Revisions
- Update design files with version numbers
- Document changes in `Decision_Log.md`
- Mark designs as "Final" when approved

---

## Design Deliverables

**What developers need:**

### For Developers
- [x] High-fidelity mockups (final approved designs)
- [x] Design specs (spacing, colors, fonts)
- [x] Asset exports (icons, logos, images)
- [x] Interaction notes (hover states, transitions, animations)

### Create a Handoff Doc
`04_Designs/Developer_Handoff.md`:

```markdown
# Design Handoff - Developer Guide

## Design Assets Location
- Final mockups: `04_Designs/Mockups/`
- Icons/images: `04_Designs/Assets/`
- Style guide: [document in this folder or Platform_Specification.md]

## Screen Index
| Screen | Epic | File | Status |
|:---|:---|:---|:---:|
| Login | Epic-01 | `Mockups/Epic-01_Login.png` | [x] Final |
| Dashboard | Epic-02 | `Mockups/Epic-02_Dashboard.png` | [x] Final |
| Settings | Epic-03 | `Mockups/Epic-03_Settings.png` | [~] In Progress |

## Design Tool Access
- **Figma**: [Link] (for inspect mode, spacing, colors)
- **Zeplin**: [Link] (if using)

## Key Interactions
- Login form validation: Real-time on blur
- Dashboard filters: Debounced search (300ms)
- See: `04_Designs/Flows/` for detailed flows

## Questions?
Contact: designer@example.com
```

---

## Asset Management

### Exporting Assets

**Organized asset folders:**

```
04_Designs/Assets/
|-- Icons/
|   |-- icon_user.svg
|   |-- icon_settings.svg
|   +-- icon_logout.svg
|
|-- Logos/
|   |-- logo_full.svg
|   |-- logo_icon.svg
|   +-- logo_white.svg
|
|-- Images/
|   |-- hero_image.jpg
|   |-- empty_state_illustration.svg
|   +-- onboarding_step1.png
|
+-- README.md  <- Asset usage guide
```

**Asset README example:**
```markdown
# Assets Usage Guide

## Icons
- Format: SVG (vector, scalable)
- Color: Single color, use CSS to tint
- Size: 24x24px default

## Logos
- Full logo: Use on light backgrounds
- White logo: Use on dark/colored backgrounds
- Min width: 120px (maintain aspect ratio)

## Images
- Hero images: 1920x1080px, JPEG, optimized
- Illustrations: SVG preferred, PNG fallback
```

---

## Design + Requirements Workflow

**Integrating designs with specifications:**

1. **Draft requirements first** -> Identify UI needs
2. **Create wireframes** -> Validate flow and structure
3. **Get client feedback** -> Adjust wireframes
4. **Create high-fidelity mockups** -> Visual design
5. **Link mockups to features** -> Reference in specs
6. **Final review** -> Sign off on designs
7. **Export for developers** -> Handoff package

---

## AI Prompts for Design Documentation

### Generate Design Notes from Mockups
```
I have design mockups in 04_Designs/Mockups/.

For each screen, extract and document:
1. Key UI elements and layout
2. Interaction patterns
3. States (default, loading, error, empty)
4. Responsive behavior notes

Add to relevant Feature specs in UI/UX Notes section.
```

### Create Design Checklist
```
Based on all Epics and Features, generate a design checklist:
- Which screens/components need designs?
- What states need to be designed (loading, error, empty)?
- What responsive breakpoints?
- Any complex interactions requiring detailed flows?

Output as 04_Designs/Design_Checklist.md
```

---

## Related Files

- **Design Guidelines**: document in this folder as needed
- **Feature Templates**: `00_Meta/Templates/Feature_Template.md` (has UI/UX section)
- **System Overview**: `01_Context/System_Overview.md` (high-level UX approach)

---

**[!] Remember**: Designs support requirements, not replace them. Even with perfect mockups, you still need written specs for edge cases, logic, and validation rules.



