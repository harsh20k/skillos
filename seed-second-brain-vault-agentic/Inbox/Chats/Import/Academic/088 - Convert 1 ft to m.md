---
title: Convert 1 ft to m
category: Academic
priority: Medium
starred: None
created: 2024-06-25T09:36:21.338754
updated: 2024-06-26T08:25:14.579683
dg-publish: true
---
# Convert 1 ft to m

**Priority:** Medium

## Conversation

### Assistant

In SwiftUI, there isn't a built-in way to change the background color of the whole alert dialog directly. However, you can customize the appearance of the alert dialog to some extent by using custom views or creating your own custom modal view.

Here's an example of how you can create a custom modal view that changes color based on the question number:

```swift
struct ContentView: View {
    @State private var showingScore = false
    @State private var questionNumber = 8
    @State private var score = 7
    
    var body: some View {
        VStack {
            Button("Show Alert") {
                showingScore = true
            }
        }
        .alert(isPresented: $showingScore) {
            Alert(
                title: Text(questionNumber == 8 ? "Final Score" : "Score"),
                message: Text(questionNumber == 8 ? "Your Final Score Is \(score)/8" : "Your score is \(score)"),
                dismissButton: .default(Text(questionNumber == 8 ? "Restart" : "Continue"), action: askQuestion)
            )
        }
    }
    
    func askQuestion() {
        // Your ask question logic here
    }
}
```

If you want to fully customize the dialog including the background color, you can use a custom modal view like this:

```swift
struct ContentView: View {
    @State private var showingScore = false
    @State private var questionNumber = 8
    @State private var score = 7
    
    var body: some View {
        VStack {
            Button("Show Custom Dialog") {
                showingScore = true
            }
        }
        .overlay(
            CustomDialog(show: $showingScore, questionNumber: $questionNumber, score: $score)
                .background(Color.white) // Default background color for overlay
                .edgesIgnoringSafeArea(.all)
        )
    }
}

struct CustomDialog: View {
    @Binding var show: Bool
    @Binding var questionNumber: Int
    @Binding var score: Int
    
    var body: some View {
        if show {
            VStack {
                Text(questionNumber == 8 ? "Your Final Score Is \(score)/8" : "Your score is \(score)")
                    .font(questionNumber == 8 ? .title2 : .body)
                    .padding()
                Button(questionNumber == 8 ? "Restart" : "Continue") {
                    show = false
                    // Call askQuestion or other logic here
                }
                .padding()
            }
            .frame(width: 300, height: 200)
            .background(questionNumber == 8 ? Color.red : Color.gray)
            .cornerRadius(20)
            .shadow(radius: 20)
        }
    }
}

```

In this example, `CustomDialog` is a custom view that acts as a modal dialog. You can customize the background color and other styles as needed. The dialog appears as an overlay when `showingScore` is true, and it hides when the button is pressed. Adjust the `CustomDialog` view to fit your styling needs.

---

