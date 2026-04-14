---
title: ForEach in SwiftUI
category: Projects
priority: Medium
starred: None
created: 2024-06-25T01:04:39.592873
updated: 2024-06-25T04:35:37.287732
dg-publish: true
---
# ForEach in SwiftUI

**Priority:** Medium

## Conversation

### Assistant

In SwiftUI, there's no direct way to disable a specific selection within a `Picker`. However, you can achieve this by using a custom approach where you filter out or disable the unselectable items visually and programmatically prevent selection. One common method is to use a conditional statement to alter the appearance of the items and handle the selection logic.

Here’s an example of how you can create a picker where certain items are visually disabled and cannot be selected:

### Custom Picker with Disabled Options

1. **Create a Custom View for Picker Items**: Use a view modifier to indicate disabled items.
2. **Filter Logic in the Picker**: Ensure the disabled items cannot be selected.

### Example Code

```swift
import SwiftUI

struct ContentView: View {
    @State private var numberOfPeople = 2 // Default value
    @State private var showPicker = false // State to control picker presentation
    
    let disabledIndices = [4, 6, 8] // Indices of disabled options
    
    var body: some View {
        VStack {
            // Display the current selection in a button
            Button(action: {
                showPicker = true // Show the picker when button is clicked
            }) {
                HStack {
                    Text("Number of people: ")
                    Text("\(numberOfPeople)")
                        .fontWeight(.bold)
                        .foregroundColor(.blue)
                }
            }
            .padding()
            .background(Color(.systemGray5))
            .cornerRadius(10)
            
            // Rest of your form content
            Form {
                // Example sections from your previous code
                Section("How much tip?") {
                    Picker("Tip percentages", selection: $tipPercentage) {
                        ForEach(tipPercentages, id: \.self) {
                            Text($0, format: .percent)
                        }
                    }
                    .pickerStyle(.segmented)
                }
                Section {
                    Text(totalPerPerson, format: .currency(code: Locale.current.currency?.identifier ?? "INR"))
                }
            }
        }
        .sheet(isPresented: $showPicker) {
            // The picker presented as a sheet
            VStack {
                Text("Select Number of People")
                    .font(.headline)
                    .padding()

                Picker("Number of people", selection: $numberOfPeople) {
                    ForEach(2..<20) { index in
                        if disabledIndices.contains(index) {
                            Text("\(index) people")
                                .foregroundColor(.gray) // Indicate disabled option
                                .onTapGesture {
                                    // Prevent selection
                                }
                        } else {
                            Text("\(index) people")
                                .foregroundColor(.primary) // Normal color for selectable option
                        }
                    }
                }
                .pickerStyle(.wheel)
                .frame(maxWidth: .infinity, maxHeight: 200) // Customizing frame size
                .clipped()
                .padding()
                .background(Color(.systemGray6)) // Customizing background color
                .cornerRadius(10)
                .shadow(radius: 10) // Adding shadow
                
                // Done button to close the sheet
                Button("Done") {
                    showPicker = false
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            .padding()
        }
    }
}

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

### Explanation

1. **State Variables**:
   - `@State private var numberOfPeople = 2`: Holds the current selection.
   - `@State private var showPicker = false`: Controls the picker presentation.
   - `let disabledIndices = [4, 6, 8]`: An array of indices representing the disabled options.

2. **Button**:
   - Displays the current selection and triggers the picker presentation.

3. **Picker with Disabled Options**:
   - Inside the `Picker`, use a conditional statement to check if the index is in `disabledIndices`.
   - If the index is disabled, change the text color to gray and prevent selection using an empty `onTapGesture`.
   - For selectable options, use the primary color.

4. **Picker Presentation**:
   - The picker is presented as a sheet with the `.sheet` modifier.
   - Customizations include frame size, background color, and shadow for visual appeal.

### Conclusion

This approach visually disables certain options in the picker and prevents them from being selected. By using a combination of conditional views and gesture handling, you can effectively control which items in a picker are selectable and which are not.

---

