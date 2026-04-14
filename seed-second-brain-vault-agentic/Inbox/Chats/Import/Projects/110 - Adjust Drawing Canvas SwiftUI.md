---
title: Adjust Drawing Canvas SwiftUI
category: Projects
priority: Medium
starred: None
created: 2024-06-17T15:57:59.702528
updated: 2024-06-17T18:55:43.401874
dg-publish: true
---
# Adjust Drawing Canvas SwiftUI

**Priority:** Medium

## Conversation

### Assistant

For persisting the drawing data in your application, you should use a data model that captures the necessary information about the drawing, such as the strokes, their coordinates, color, and width. One efficient way to store this data is by using Core Data, a framework provided by Apple for managing the model layer objects in your application. 

Here's an example of how you can set up a Core Data model for your drawing app:

1. **Set Up Core Data in Your Project**:
   - Add a new data model file (e.g., `DrawingDataModel.xcdatamodeld`) to your project.
   - Define entities and attributes in the data model file.

2. **Define Entities**:
   - **Drawing**: Represents a complete drawing.
     - `id`: UUID
     - `name`: String
     - `createdAt`: Date
     - `strokes`: Relationship to `Stroke` (one-to-many)

   - **Stroke**: Represents a single stroke in the drawing.
     - `id`: UUID
     - `color`: Data (to store `UIColor`)
     - `width`: Float
     - `points`: Data (to store an array of `CGPoint` as Data)
     - `drawing`: Relationship to `Drawing` (many-to-one)

3. **Generate NSManagedObject Subclasses**:
   - Generate the `NSManagedObject` subclasses for `Drawing` and `Stroke`.

4. **Implement the Drawing Persistence Logic**:
   - Save, fetch, and delete drawings using Core Data.

Here is an example implementation:

### Data Model Setup

#### DrawingDataModel.xcdatamodeld

**Drawing Entity:**
- id: UUID
- name: String
- createdAt: Date
- strokes: Relationship (To Many, Destination: Stroke, Inverse: drawing)

**Stroke Entity:**
- id: UUID
- color: Data
- width: Float
- points: Data
- drawing: Relationship (To One, Destination: Drawing, Inverse: strokes)

### NSManagedObject Subclasses

```swift
import CoreData
import UIKit

// Drawing Entity
@objc(Drawing)
public class Drawing: NSManagedObject {
    @NSManaged public var id: UUID
    @NSManaged public var name: String
    @NSManaged public var createdAt: Date
    @NSManaged public var strokes: NSSet?
}

extension Drawing {
    @nonobjc public class func fetchRequest() -> NSFetchRequest<Drawing> {
        return NSFetchRequest<Drawing>(entityName: "Drawing")
    }
    
    @objc(addStrokesObject:)
    @NSManaged public func addToStrokes(_ value: Stroke)
    
    @objc(removeStrokesObject:)
    @NSManaged public func removeFromStrokes(_ value: Stroke)
    
    @objc(addStrokes:)
    @NSManaged public func addToStrokes(_ values: NSSet)
    
    @objc(removeStrokes:)
    @NSManaged public func removeFromStrokes(_ values: NSSet)
}

// Stroke Entity
@objc(Stroke)
public class Stroke: NSManagedObject {
    @NSManaged public var id: UUID
    @NSManaged public var color: Data
    @NSManaged public var width: Float
    @NSManaged public var points: Data
    @NSManaged public var drawing: Drawing?
}

extension Stroke {
    @nonobjc public class func fetchRequest() -> NSFetchRequest<Stroke> {
        return NSFetchRequest<Stroke>(entityName: "Stroke")
    }
}
```

### Saving and Loading Drawings

```swift
import CoreData
import UIKit

class DrawingPersistenceManager {
    static let shared = DrawingPersistenceManager()
    
    private let persistentContainer: NSPersistentContainer
    
    private init() {
        persistentContainer = NSPersistentContainer(name: "DrawingDataModel")
        persistentContainer.loadPersistentStores { (description, error) in
            if let error = error {
                fatalError("Unable to load persistent stores: \(error)")
            }
        }
    }
    
    var context: NSManagedObjectContext {
        return persistentContainer.viewContext
    }
    
    func saveDrawing(name: String, strokes: [Stroke]) {
        let drawing = Drawing(context: context)
        drawing.id = UUID()
        drawing.name = name
        drawing.createdAt = Date()
        drawing.addToStrokes(NSSet(array: strokes))
        
        do {
            try context.save()
        } catch {
            print("Failed to save drawing: \(error)")
        }
    }
    
    func fetchDrawings() -> [Drawing] {
        let fetchRequest: NSFetchRequest<Drawing> = Drawing.fetchRequest()
        do {
            return try context.fetch(fetchRequest)
        } catch {
            print("Failed to fetch drawings: \(error)")
            return []
        }
    }
    
    func deleteDrawing(_ drawing: Drawing) {
        context.delete(drawing)
        do {
            try context.save()
        } catch {
            print("Failed to delete drawing: \(error)")
        }
    }
}

// Usage Example:

// Convert UIColor to Data
func colorToData(color: UIColor) -> Data? {
    return try? NSKeyedArchiver.archivedData(withRootObject: color, requiringSecureCoding: false)
}

// Convert Data to UIColor
func dataToColor(data: Data) -> UIColor? {
    return try? NSKeyedUnarchiver.unarchiveTopLevelObjectWithData(data) as? UIColor
}

// Convert [CGPoint] to Data
func pointsToData(points: [CGPoint]) -> Data? {
    return try? NSKeyedArchiver.archivedData(withRootObject: points, requiringSecureCoding: false)
}

// Convert Data to [CGPoint]
func dataToPoints(data: Data) -> [CGPoint]? {
    return try? NSKeyedUnarchiver.unarchiveTopLevelObjectWithData(data) as? [CGPoint]
}
```

### Integrate with DrawingView

In your `DrawingView`, you can create `Stroke` objects and save them to Core Data when needed. When loading a drawing, you can fetch the strokes from Core Data and render them.

This approach allows you to persist drawings with their strokes, colors, and widths in a structured way using Core Data.

---

