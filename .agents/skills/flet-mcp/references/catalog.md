# Catálogo Flet MCP

Instantâneo obtido em 2026-10-12 com `list_controls(limit=1000)` e conferência de `package` usando `get_api`. Contém 247 controles e serviços da indexação consultada. Cada linha traz apenas nome e descrição breve, como solicitado.

Esta enumeração não é um inventário de todos os símbolos Python do Flet: enums, dataclasses, classes de eventos e outros tipos não são enumerados por `list_controls`. Consulte esses símbolos pelo nome com `get_api`. As extensões abaixo são os pacotes encontrados nos símbolos indexados por esta instância; não representam necessariamente todas as extensões publicadas pelo ecossistema.

## Controles e serviços

| Nome | Descrição |
|---|---|
| `Component` (control) | Functional component wrapper used by the component renderer. |
| `Tester` (service) | Class that programmatically interacts with page controls and the test environment. |
| `AdaptiveControl` (control) | Base class for controls that support adaptive behavior, which allows them to adjust their appearance and behavior based on the target platform (ex: Material design on Android/Windows/Linux, Cupertino design on iOS/macOS). |
| `Control` (control) | Base class for controls. |
| `LayoutControl` (control) | Base class for visual controls that participate in page layout. |
| `DialogControl` (control) | A base class for dialog controls. |
| `MultiView` (control) | Represents an additional app view managed by a multi-view session. |
| `BasePage` (control) | A visual container representing a top-level view in a Flet application. |
| `Overlay` (control) | Internal container for controls displayed above main page content. |
| `Dialogs` (control) | Internal container tracking dialogs currently managed by a page. |
| `ActionControl` (control) | Base class for controls that can perform :class:`~flet.ClientAction` work when |
| `ScrollableControl` (control) | Shared scroll behavior for controls that expose a scrollable viewport. |
| `ServiceRegistry` (service) | Internal container that hosts page-level service controls. |
| `Page` (control) | Page is a container for :class:`~flet.View` controls. |
| `CupertinoSlider` (control) | An iOS-type slider. |
| `CupertinoPicker` (control) | An iOS-styled picker. |
| `CupertinoSwitch` (control) | An iOS-style switch. |
| `CupertinoAppBar` (control) | An iOS-styled app bar. |
| `CupertinoSlidingSegmentedButton` (control) | A cupertino sliding segmented button. |
| `CupertinoContextMenu` (control) | A full-screen modal route that opens up when the :attr:`content` is long-pressed. |
| `CupertinoDialogAction` (control) | A dialog action button. |
| `CupertinoAlertDialog` (control) | An iOS-style alert dialog. |
| `CupertinoContextMenuAction` (control) | A cupertino context menu action. |
| `CupertinoTextField` (control) | An iOS-style text field. |
| `CupertinoBottomSheet` (control) | A Cupertino bottom sheet. |
| `CupertinoRadio` (control) | A macOS-styled radio button, allowing the user to select a single option from two or more choices. |
| `CupertinoActivityIndicator` (control) | An iOS-style activity indicator that spins clockwise. |
| `CupertinoTintedButton` (control) | An iOS-style button filled with default background color. |
| `CupertinoListTile` (control) | An iOS-style list tile. |
| `CupertinoFilledButton` (control) | An iOS-style button filled with default background color. |
| `CupertinoSegmentedButton` (control) | An iOS-style segmented button. |
| `CupertinoDatePicker` (control) | An iOS-styled date picker. |
| `CupertinoButton` (control) | An iOS-style button. |
| `CupertinoTimerPicker` (control) | A countdown timer picker in iOS style. |
| `CupertinoCheckbox` (control) | A macOS style checkbox. |
| `CupertinoActionSheet` (control) | An iOS-style action sheet. |
| `CupertinoNavigationBar` (control) | An iOS-styled bottom navigation tab bar. |
| `CupertinoActionSheetAction` (control) | An action button typically used in a CupertinoActionSheet. |
| `Chip` (control) | Chips are compact elements that represent an attribute, text, entity, or action. |
| `Switch` (control) | A toggle represents a physical switch that allows someone to choose between two mutually exclusive options. |
| `DropdownOption` (control) | Represents an item in a dropdown. |
| `Dropdown` (control) | A dropdown control that allows users to select a single option from a list of :attr:`options`. |
| `OutlinedButton` (control) | Outlined buttons are medium-emphasis buttons. They contain actions that are important, but aren't the primary action in an app. Outlined buttons pair well with filled buttons to indicate an alternative, secondary action. |
| `DateRangePicker` (control) | A Material-style date range picker dialog. |
| `AutoComplete` (control) | Helps the user make a selection by entering some text and choosing from among a list of displayed options. |
| `NavigationRailDestination` (control) | Represents a destination in a `NavigationRail`. |
| `NavigationRail` (control) | A material widget that is meant to be displayed at the left or right of an app to navigate between a small number of views, typically between three and five. |
| `ContextMenu` (control) | Wraps its :attr:`content` and displays contextual menus for specific mouse events. |
| `FilledButton` (control) | Filled buttons have the most visual impact after the :class:`~flet.FloatingActionButton`, and is typically used for important, final actions that complete a flow, like "Save", "Join now", or "Confirm". |
| `Segment` (control) | A segment for a :class:`~flet.SegmentedButton`. |
| `SegmentedButton` (control) | A segmented button control. |
| `Checkbox` (control) | Checkbox allows to select one or more items from a group, or switch between two mutually exclusive options (checked or unchecked, on or off). |
| `Radio` (control) | Radio buttons let people select a single option from two or more choices. |
| `FloatingActionButton` (control) | A floating action button is a circular icon button that hovers over content to promote a primary action in the application. Floating action button is usually set to `page.floating_action_button`, but can also be added as a regular control at any place on a page. |
| `Option` (control) | Represents an item in a dropdown. |
| `DropdownM2` (control) | A dropdown lets the user select from a number of items. The dropdown shows the currently selected item as well as an arrow that opens a menu for selecting another item. |
| `MenuItemButton` (control) | A button for use in a MenuBar or on its own, that can be activated by click or keyboard navigation. |
| `DatePicker` (control) | A Material-style date picker dialog. |
| `Slider` (control) | A slider provides a visual indication of adjustable content, as well as the current setting in the total range of content. |
| `ListTile` (control) | A single fixed-height row that typically contains some text as well as a leading or trailing icon. |
| `PopupMenuItem` (control) | A popup menu item. |
| `PopupMenuButton` (control) | An icon button which displays a menu when clicked. |
| `Card` (control) | A material design card: a panel with slightly rounded corners and an elevation shadow. |
| `RangeSlider` (control) | A Material Design range slider. Used to select a range from a range of values. |
| `ReorderableListView` (control) | A scrollable list of controls that can be reordered. |
| `SnackBarAction` (control) | A button that can be used as an action in a :class:`~flet.SnackBar`. |
| `SnackBar` (control) | A lightweight message with an optional action which briefly displays at the bottom of the screen. |
| `FormFieldControl` (control) | Base class for Material form-field controls with a decorated input area. |
| `Tabs` (control) | Used for navigating frequently accessed, distinct content categories. Tabs allow for navigation between two or more content views and relies on text headers to articulate the different sections of content. |
| `TabBarView` (control) | A page view with one child per tab. |
| `TabBar` (control) | Used for navigating frequently accessed, distinct content categories. Tabs allow for navigation between two or more content views and relies on text headers to articulate the different sections of content. |
| `Tab` (control) | A Material Design :class:`~flet.TabBar` tab. |
| `TextField` (control) | A text field lets the user enter text, either with hardware keyboard or with an onscreen keyboard. |
| `DataColumn` (control) | Column configuration for a :class:`~flet.DataTable`. |
| `DataCell` (control) | The data for a cell of a :class:`~flet.DataTable`. |
| `DataRow` (control) | Row configuration and cell data for a :class:`~flet.DataTable`. |
| `DataTable` (control) | A Material Design data table. |
| `Container` (control) | Allows to decorate a control with background color and border and position it with padding, margin and alignment. |
| `AlertDialog` (control) | Can be used to inform the user about situations that require acknowledgement. |
| `CircleAvatar` (control) | A circle that represents a user. |
| `ExpansionPanel` (control) | A material expansion panel. It can either be expanded or collapsed. Its body is only visible when it is expanded. |
| `ExpansionPanelList` (control) | A material expansion panel list that lays out its children and animates expansions. |
| `IconButton` (control) | An icon button is a round button with an icon in the middle that reacts to touches by filling with color (ink). |
| `FilledIconButton` (control) | A filled variant of :class:`~flet.IconButton`. |
| `FilledTonalIconButton` (control) | A filled tonal variant of :class:`~flet.IconButton`. |
| `OutlinedIconButton` (control) | An outlined variant of :class:`~flet.IconButton`. |
| `TimePicker` (control) | A Material-style time picker dialog. |
| `RadioGroup` (control) | Radio buttons let people select a single option from two or more choices. |
| `Divider` (control) | A thin horizontal line (divider), with padding on either side. |
| `SelectionArea` (control) | Flet controls are not selectable by default. SelectionArea is used to enable selection for its child control. |
| `TextButton` (control) | Text buttons are used for the lowest priority actions, especially when presenting multiple options. Text buttons can be placed on a variety of backgrounds. Until the button is interacted with, its container isn’t visible. |
| `Badge` (control) | Badges are used to show notifications, counts, or status information on navigation items such as :class:`~flet.NavigationBar` or :class:`~flet.NavigationRail` destinations or a button's icon. |
| `Button` (control) | A material button. |
| `SubmenuButton` (control) | A menu button that displays a cascading menu. |
| `NavigationDrawerDestination` (control) | Displays an icon with a label, for use in NavigationDrawer destinations. |
| `NavigationDrawer` (control) | Material Design Navigation Drawer component. |
| `AppBar` (control) | A material design app bar. |
| `SearchBar` (control) | Manages a "search view" route that allows the user to select one of the suggested completions for a search query. |
| `ExpansionTile` (control) | A single-line ListTile with an expansion arrow icon that expands or collapses the tile to reveal or hide its controls. |
| `FilledTonalButton` (control) | A filled tonal button is an alternative middle ground between FilledButton and OutlinedButton buttons. They're useful in contexts where a lower-priority button requires slightly more emphasis than an outline would give, such as "Next" in an onboarding flow. Tonal buttons use the secondary color mapping. |
| `MenuBar` (control) | A menu bar that manages cascading child menus. |
| `BottomSheet` (control) | A modal bottom sheet. |
| `Banner` (control) | A banner displays an important, succinct message, and provides actions for users to address (or dismiss the banner). A user action is required for it to be dismissed. |
| `BottomAppBar` (control) | A material design bottom app bar. |
| `ProgressRing` (control) | A material design circular progress indicator, which spins to indicate that the application is busy. |
| `VerticalDivider` (control) | A thin vertical line, with padding on either side. |
| `ProgressBar` (control) | A material design linear progress indicator, also known as a progress bar. |
| `NavigationBarDestination` (control) | Defines the appearance of the button items that are arrayed within the navigation bar. |
| `NavigationBar` (control) | Material 3 Navigation Bar component. |
| `ShakeDetector` (service) | Detects phone shakes. |
| `SemanticsService` (service) | Allows access to the platform's accessibility services. |
| `BrowserContextMenu` (service) | Controls the browser's context menu on the web platform. |
| `HapticFeedback` (service) | Allows access to the haptic feedback interface on the device. |
| `FilePicker` (service) | A control that allows you to use the native file explorer to pick single or multiple files, with extensions filtering support and upload. |
| `Magnetometer` (service) | Streams magnetometer :class:`flet.MagnetometerReadingEvent` reporting the ambient magnetic field (`uT`) per axis for compass-style use cases. |
| `Share` (service) | Shares text, links, or files using the platform share sheet. |
| `Accelerometer` (service) | Streams raw accelerometer :class:`flet.AccelerometerReadingEvent`, which describe the acceleration of the device, in `m/s^2`, including the effects of gravity. |
| `Connectivity` (service) | Provides device connectivity status and change notifications. |
| `UrlLauncher` (service) | Provides access to URL launching capabilities. |
| `SharedPreferences` (service) | Provides access to persistent key-value storage. |
| `Clipboard` (service) | Provides access to the system clipboard. |
| `StoragePaths` (service) | Provides access to commonly used storage paths on the device. |
| `Service` (control) | Base class for user services. |
| `Battery` (service) | Provides access to device battery information and state changes. |
| `Wakelock` (service) | Prevents the device from sleeping while enabled. |
| `Barometer` (service) | Streams barometer :class:`~flet.BarometerReadingEvent` samples (atmospheric pressure in `hPa`). Useful for altitude calculations and weather-related experiences. |
| `ScreenBrightness` (service) | Provides access to control and observe system and application screen brightness. |
| `Gyroscope` (service) | Streams gyroscope :class:`flet.GyroscopeReadingEvent`, reporting device rotation rate around each axis in `rad/s`. |
| `UserAccelerometer` (service) | Streams linear acceleration readings. |
| `Markdown` (control) | Renders text in markdown format. |
| `Placeholder` (control) | A placeholder box. |
| `AnimatedSwitcher` (control) | Used to switch between controls with an animation. |
| `ReorderableDragHandle` (control) | Used to drag an item in a :class:`~flet.ReorderableListView`. |
| `Column` (control) | Arranges child controls vertically, optionally aligning and spacing them within the available space. |
| `Stack` (control) | Positions its children on top of each other, following a LIFO (Last In First Out) order. |
| `DragTarget` (control) | A control that completes drag operation when a :class:`~flet.Draggable` control is dropped. |
| `FletApp` (control) | Renders another Flet app in the current app, similar to HTML IFrame, but for Flet. |
| `RawImage` (control) | Displays pixel frames pushed from Python at full bandwidth. |
| `Dismissible` (control) | A control that can be dismissed by dragging in the indicated :attr:`dismiss_direction`. |
| `GridView` (control) | A scrollable, 2D array of controls. |
| `Draggable` (control) | A control that can be dragged from to a :class:`~flet.DragTarget`. |
| `Image` (control) | Draws an image. |
| `Text` (control) | Draws :attr:`value` with :attr:`style` at the given (:attr:`x`, :attr:`y`) point. |
| `ShaderMask` (control) | Applies a mask generated by a shader to its :attr:`content`. |
| `KeyboardListener` (control) | A control that calls a callback whenever the user presses or releases a key on a keyboard. |
| `Icon` (control) | A control that displays an icon from a built-in or custom icon set. |
| `TransparentPointer` (control) | TransparentPointer is the solution to ["How to pass through all gestures between two widgets in Stack"](https://stackoverflow.com/questions/65269190/pass-trough-all-gestures-between-two-widgets-in-stack) problem. |
| `InteractiveViewer` (control) | Allows you to pan, zoom, and rotate its :attr:`content`. |
| `PageView` (control) | Displays its child :attr:`controls` one page at a time and lets users swipe |
| `MergeSemantics` (control) | A control that merges the semantics of its descendants. |
| `Screenshot` (control) | Takes a screenshot of containing control. |
| `Hero` (control) | Marks the :attr:`content` as a shared element for route transitions. |
| `GestureDetector` (control) | A control that detects gestures. |
| `WindowDragArea` (control) | It mimics the behavior (drag, move, maximize, restore) of a native OS window title bar on the :attr:`content` control. |
| `TextSpan` (control) | A text span. |
| `Window` (control) | Controls the app window. |
| `SafeArea` (control) | A control that insets its :attr:`content` by sufficient padding to avoid intrusions by the operating system. |
| `ResponsiveRow` (control) | Allows aligning child controls to virtual columns. |
| `AutofillGroup` (control) | Used to group autofill controls together. |
| `ListView` (control) | A scrollable list of controls arranged linearly. |
| `Semantics` (control) | Provides semantic annotations for the control tree, describing the meaning and purpose of controls. |
| `Row` (control) | Displays its children in a horizontal array. |
| `Shimmer` (control) | Applies an animated shimmering effect to its :attr:`content`. |
| `RotatedBox` (control) | Rotates its :attr:`content` by an integral number of quarter turns. |
| `View` (control) | View is the top most container for all other controls. |
| `Pagelet` (control) | Implements the basic Material Design visual layout structure. |
| `Color` (control) | Paints the given `color` onto the canvas, applying the given `blend_mode`, with the given color being the source and the background being the destination. |
| `Canvas` (control) | Canvas is a control for drawing arbitrary graphics using a set of primitives or "shapes" such as line, arc, path and text. |
| `Arc` (control) | Draws an arc scaled to fit inside the given rectangle. |
| `Rect` (control) | Draws a rectangle. |
| `Shape` (control) | A base class for canvas shapes. |
| `Oval` (control) | Draws an axis-aligned oval that fills the given axis-aligned rectangle with the given :attr:`paint`. |
| `Line` (control) | Draws a line between the given points using the given paint. |
| `Fill` (control) | Fills the canvas with the given :attr:`paint`. |
| `Circle` (control) | Draws a circle. |
| `Points` (control) | Draws a sequence of points according to the given :attr:`point_mode`. |
| `Path` (control) | Draws a path with given :attr:`elements` |
| `Shadow` (control) | Draws a shadow for a :attr:`path` representing the given material :attr:`elevation`. |
| `NativeAd` (control) | Renders a native ad. |
| `BannerAd` (control) | Displays a banner ad. |
| `BaseAd` (control) | Base class for all Ad controls. |
| `InterstitialAd` (service) | Displays a full-screen interstitial ad. |
| `ConsentManager` (service) | Gathers and manages user consent for ads using |
| `Audio` (service) | A control to simultaneously play multiple audio sources. |
| `AudioRecorder` (service) | A control that allows you to record audio from your device. |
| `Camera` (control) | A control that provides camera preview and capture capabilities. |
| `BarChart` (control) | Draws a bar chart. |
| `LineChartDataPoint` (control) | A :class:`~flet_charts.LineChartData` point. |
| `ScatterChart` (control) | A scatter chart control. |
| `MatplotlibChartWithToolbar` (control) | Composite control that combines a `MatplotlibChart` with a ready-made toolbar UI. |
| `BarChartRodStackItem` (control) | Colored segment used to build a stacked bar rod. |
| `RadarDataSetEntry` (control) | A single data point rendered on a :class:`~flet_charts.RadarChart`. |
| `RadarDataSet` (control) | A collection of :class:`~flet_charts.RadarDataSetEntry` drawn as a filled radar shape. |
| `PieChart` (control) | A pie chart control displaying multiple sections as slices of a circle. |
| `BarChartGroup` (control) | Groups one or more bar rods rendered at the same X-axis position. |
| `RadarChartTitle` (control) | Custom title configuration displayed around a :class:`~flet_charts.RadarChart`. |
| `RadarChart` (control) | A radar chart made of multiple datasets. |
| `CandlestickChart` (control) | Draws a candlestick chart representing OHLC values. |
| `ScatterChartSpot` (control) | A spot on a scatter chart. |
| `MatplotlibChartCanvas` (control) | Display widget for matplotlib WebAgg-style image streams. |
| `MatplotlibChart` (control) | Displays a [Matplotlib](https://matplotlib.org/) chart. |
| `CandlestickChartSpot` (control) | Represents a candlestick rendered on a :class:`~flet_charts.CandlestickChart`. |
| `LineChartData` (control) | Styling and geometry configuration for a single line series. |
| `ChartAxisLabel` (control) | Configures a custom label for specific value. |
| `ChartAxis` (control) | Configures chart axis. |
| `PieChartSection` (control) | Configures a :class:`~flet_charts.PieChart` section. |
| `BarChartRod` (control) | A bar rod in a :class:`~flet_charts.BarChartGroup`. |
| `PlotlyChart` (control) | Displays a [Plotly](https://plotly.com/python/) chart. |
| `LineChart` (control) | Draws a line chart. |
| `CodeEditor` (control) | Edit and highlight source code. |
| `BlockPicker` (control) | A color picker that lets users choose a color from a grid of available |
| `MaterialPicker` (control) | A material palette picker for selecting primary and shade colors, with |
| `HueRingPicker` (control) | A hue ring color picker that lets users select a hue on a circular ring, |
| `SlidePicker` (control) | A slider-based color picker that exposes RGB/HSV/HSL channels with optional |
| `MultipleChoiceBlockPicker` (control) | A color picker that lets users choose multiple colors from a grid of available |
| `ColorPicker` (control) | A full-featured color picker with palette, sliders, labels, and optional |
| `DataRow2` (control) | Extends :class:`flet.DataRow`, adding row-level `tap` events. |
| `DataColumn2` (control) | Extends :class:`flet.DataColumn`, |
| `DataTable2` (control) | Provides sticky header row, scrollable data rows, |
| `Flashlight` (service) | A control to use FlashLight. Works on iOS and Android. |
| `Geolocator` (service) | A control that allows you to fetch GPS data from your device. |
| `Lottie` (control) | Displays lottie animations. |
| `Marker` (control) | A marker displayed on the Map at the specified location |
| `MarkerLayer` (control) | A layer to display Markers. |
| `SimpleAttribution` (control) | A simple attribution layer displayed on the Map. |
| `CircleMarker` (control) | A circular marker displayed on the Map at the specified |
| `CircleLayer` (control) | A layer to display :class:`~flet_map.CircleMarker`. |
| `PolygonMarker` (control) | A marker for the :class:`~flet_map.PolygonLayer`. |
| `PolygonLayer` (control) | A layer to display PolygonMarkers. |
| `PolylineMarker` (control) | A marker for the :class:`~flet_map.PolylineLayer`. |
| `PolylineLayer` (control) | A layer to display :class:`~flet_map.PolylineMarker`s. |
| `SourceAttribution` (control) | Abstract class for source attribution controls: |
| `ImageSourceAttribution` (control) | An image attribution permanently displayed adjacent to the |
| `TextSourceAttribution` (control) | A text source attribution displayed on the Map. |
| `MapLayer` (control) | Abstract class for all map layers. |
| `BaseOverlayImage` (control) | Abstract class for image overlays displayed through |
| `OverlayImage` (control) | An unrotated image overlay that spans between a given bounding box. |
| `RotatedOverlayImage` (control) | An image overlay transformed across three corner points. |
| `OverlayImageLayer` (control) | A layer to display image overlays. |
| `TileLayer` (control) | Displays square raster images in a continuous grid, |
| `RichAttribution` (control) | An animated and interactive attribution layer that supports both images and text |
| `Map` (control) | An interactive map that displays various layers. |
| `PermissionHandler` (service) | Manages permissions for the application. |
| `Rive` (control) | Displays rive animations. |
| `SecureStorage` (service) | A class to manage secure storage in a Flet application across multiple platforms. |
| `Video` (control) | A control that displays a video from a playlist. |
| `WebView` (control) | Easily load webpages while allowing user interaction. |

## Pacotes de extensão encontrados

| Nome | Descrição |
|---|---|
| `flet-ads` | Controles e serviços para anúncios e gestão de consentimento. |
| `flet-audio` | Reprodução de áudio. |
| `flet-audio-recorder` | Gravação de áudio. |
| `flet-camera` | Prévia e captura pela câmera. |
| `flet-charts` | Gráficos de barras, linhas, pizza, radar, dispersão, candles e Matplotlib/Plotly. |
| `flet-code-editor` | Editor de código com realce de sintaxe. |
| `flet-color-pickers` | Seletores de cores e paletas. |
| `flet-datatable2` | Tabelas de dados com recursos adicionais. |
| `flet-flashlight` | Acesso à lanterna do dispositivo. |
| `flet-geolocator` | Localização e dados GPS. |
| `flet-lottie` | Animações Lottie. |
| `flet-map` | Mapas, camadas, marcadores e imagens. |
| `flet-permission-handler` | Gerenciamento de permissões do aplicativo. |
| `flet-rive` | Animações Rive. |
| `flet-secure-storage` | Armazenamento seguro. |
| `flet-video` | Reprodução de vídeo. |
| `flet-webview` | Exibição e interação com páginas web. |
