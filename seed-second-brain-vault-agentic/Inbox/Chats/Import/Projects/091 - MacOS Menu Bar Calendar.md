---
title: MacOS Menu Bar Calendar
category: Projects
priority: Medium
starred: None
created: 2024-12-18T06:04:51.118028
updated: 2024-12-18T06:41:43.637052
dg-publish: true
---
# MacOS Menu Bar Calendar

**Priority:** Medium

## Conversation

### Assistant

This SwiftUI view is essentially the main interface for a macOS menu bar application that manages a to-do list. Let’s break down what’s happening in detail:

### High-Level Overview
- The view displays a list of todos, each with a checkbox (done/undone state) and a delete button.
- Users can edit the text of a todo by clicking on it.
- There's a text field at the bottom to add new todos.
- A menu in the bottom-right corner provides quick actions like "Clear Done", "Clear All", and allows toggling the app to launch at login, showing an About window, and quitting the app.

### Key Points in the Code

1. **Imports and Dependencies:**
   ```swift
   import SwiftUI
   import Defaults
   import LaunchAtLogin
   ```
   - **SwiftUI**: For building the user interface.
   - **Defaults**: A third-party framework or property wrapper to easily store and retrieve user defaults (e.g. the `@Default` property wrapper).
   - **LaunchAtLogin**: A package that simplifies enabling/disabling the app to run at system startup.

2. **Property Wrappers and State Variables:**
   ```swift
   @Default(.todos) var todos
   @NSApplicationDelegateAdaptor private var appDelegate: AppDelegate
   @State private var text: String = ""
   @State private var editedItem: String = ""
   @State private var newTodo: String = ""
   @State private var editedItemIdx: Int = -1
   @State private var hoverItemIdx: Int = -1
   @State private var hoverIdx: Int = -1
   @FocusState private var isTextFieldFocused: Bool
   @FocusState private var IsTodoItemFocused: Bool
   ```
   - `@Default(.todos)` binds the `todos` array to a user default key, so changes persist.
   - `@NSApplicationDelegateAdaptor` injects the `AppDelegate` to use app-level functions like showing About window and quitting.
   - `text`, `editedItem`, `newTodo` are `@State` variables that keep track of current text input or edits.
   - `editedItemIdx` stores which todo index is currently being edited (`-1` means none).
   - `hoverItemIdx` and `hoverIdx` keep track of which row the mouse is currently hovering over.
   - `isTextFieldFocused` and `IsTodoItemFocused` are focus states used to manage which text field has keyboard focus.

3. **The Main Layout (VStack):**
   ```swift
   VStack {
       List($todos.indices, id: \.self) { index in
           ...
       }
       
       HStack {
           TextField("Type a task and hit enter", text: $newTodo)
           ...
           
           Spacer()
           
           Menu {
               ...
           } label: {
               Image(systemName: "chevron.down")
           }
           .labelsHidden()
           ...
       }
       .padding(8)
   }
   ```
   - The top part is a `List` showing each todo.
   - The bottom `HStack` contains:
     - A text field for adding new todos.
     - A `Menu` for additional actions.

4. **The List of Todos:**
   ```swift
   List($todos.indices, id: \.self) { index in
       HStack {
           // Checkbox button
           Button(action: {
               todos[index].isDone.toggle()
           }) {
               Image(systemName: todos[index].isDone ? "checkmark.circle" : "circle")
                   .resizable()
                   .frame(width: 18, height: 18)
                   .padding(.top, 1)
           }.buttonStyle(PlainButtonStyle())
           
           // Editable text
           if editedItemIdx == index {
               TextField("", text: $editedItem, axis: .vertical)
                   .focused($IsTodoItemFocused)
                   .onSubmit {
                       // On pressing Enter: Finish editing
                       editedItemIdx = -1
                       todos[index] = Todo(text: editedItem, isDone: todos[index].isDone)
                       IsTodoItemFocused = false
                   }
                   .onExitCommand {
                       // On pressing Esc: Also finish editing
                       editedItemIdx = -1
                       todos[index] = Todo(text: editedItem, isDone: todos[index].isDone)
                       IsTodoItemFocused = false
                   }
                   .onChange(of: IsTodoItemFocused) { isFocused in
                       // If focus lost by clicking outside, also finalize editing
                       if !IsTodoItemFocused {
                           editedItemIdx = -1
                           todos[index] = Todo(text: editedItem, isDone: todos[index].isDone)
                       }
                   }
                   .padding(2)
                   .overlay(
                       RoundedRectangle(cornerRadius: 8)
                           .stroke(Color(nsColor: NSColor.controlColor), lineWidth: 1)
                   )
           } else {
               // Normal text display mode
               Text(todos[index].text)
                   .foregroundColor(todos[index].isDone ? .secondary : .primary)
                   .strikethrough(todos[index].isDone)
                   .onTapGesture {
                       // Enter editing mode on click
                       editedItemIdx = index
                       editedItem = todos[index].text
                       IsTodoItemFocused = true
                   }
                   .onHover { isHovered in
                       // Update hover index for cursor changes
                       if isHovered {
                           self.hoverIdx = index
                       } else {
                           self.hoverIdx = -1
                       }
                       // Change cursor to I-beam when hovering text
                       DispatchQueue.main.async {
                           if (self.hoverIdx == index) {
                               NSCursor.iBeam.push()
                           } else {
                               NSCursor.pop()
                           }
                       }
                   }
           }
           
           Spacer()
           
           // Trash button
           Button(action: {
               todos.remove(at: index)
           }) {
               Image(systemName: "trash.circle")
                   .resizable()
                   .frame(width: 18, height: 18)
                   .padding(.top, 1)
                   // Hover effect: icon more visible if hovered
                   .foregroundColor(hoverItemIdx == index ? .primary : .secondary)
                   .opacity(hoverItemIdx == index ? 1 : 0.2)
           }
           .buttonStyle(PlainButtonStyle())
           .onHover { isHovered in
               // Show trash icon more prominently when hovered
               if isHovered {
                   withAnimation {
                       self.hoverItemIdx = index
                   }
               } else {
                   self.hoverItemIdx = -1
               }
           }
           .listRowSeparator(.hidden)
       }
       .listRowSeparator(.hidden)
   }
   ```
   
   **What’s happening in detail:**
   - Each todo item is displayed in a horizontal row.
   - The left button toggles the `isDone` state.
   - The text of the todo is either displayed normally or as a TextField if the user is editing it.
   - Hover actions change the cursor and icon styling.
   - The trash button deletes the todo.

5. **Adding New Todos:**
   ```swift
   TextField("Type a task and hit enter", text: $newTodo)
       .padding(.vertical, 8)
       .padding(.horizontal, 8)
       .padding(.leading, 22)
       .textFieldStyle(PlainTextFieldStyle())
       .focused($isTextFieldFocused)
       .focusable(true) { isFocused in
           self.isTextFieldFocused = isFocused
       }
       .overlay(
           Image(systemName: "plus.circle.fill")
               .frame(maxWidth: .infinity, alignment: .leading)
               .foregroundColor(.gray)
               .padding(.leading, 8)
       )
       .onSubmit {
           // On pressing enter, append new todo to the list
           self.todos.append(Todo(text: newTodo))
           newTodo = ""
       }
       .onAppear {
           // Set focus to the text field when the view appears
           isTextFieldFocused = true
       }
   ```
   The text field at the bottom allows users to type in a new todo. Pressing Enter adds it to the list and clears the text field.

6. **Menu Actions:**
   ```swift
   Menu {
       Button(action: {
           // Removes all completed (isDone) todos
           todos = todos.filter{!$0.isDone}
       }) {
           Label("Clear Done", systemImage: "eyeglasses")
       }
       Button(action: {
           // Removes all todos
           todos.removeAll()
       }) {
           Label("Clear All", systemImage: "book")
       }
       Divider()
       LaunchAtLogin.Toggle()
       Divider()
       Button(action: { appDelegate.openAboutWindow(nil) } ) {
           Label("About ToDoBar", systemImage: "books.vertical")
       }
       Button(action: { appDelegate.quit() }) {
           Label("Quit", systemImage: "books.vertical")
       }
   } label: {
       Image(systemName: "chevron.down")
   }
   .menuStyle(BorderlessButtonMenuStyle())
   .menuIndicator(.hidden)
   .frame(width: 16, height: 16)
   .padding(.vertical, 8)
   .padding(.leading, 10)
   .padding(.trailing, 6)
   .background(Color.accentColor)
   .cornerRadius(8)
   .contentShape(Rectangle())
   ```
   This is a context menu providing:
   - **Clear Done**: Removes completed tasks.
   - **Clear All**: Removes all tasks.
   - **LaunchAtLogin.Toggle()**: Toggles launching the app at login.
   - **About ToDoBar**: Opens about window (via `appDelegate`).
   - **Quit**: Exits the application.

   The `appDelegate` is being used to perform actions that are outside the immediate SwiftUI view scope, such as quitting the app or showing an About window.

### Summary
- The code defines a SwiftUI-based to-do list interface inside a menu bar application.
- It uses state variables to manage editing, hovering, and focusing.
- Persistent storage is handled via `@Default(.todos)`.
- A contextual menu at the bottom offers quick batch actions and app-level controls.
- Overall, this component acts as the main interactive UI for adding, listing, editing, and removing to-do items in a compact menu bar interface.

---

