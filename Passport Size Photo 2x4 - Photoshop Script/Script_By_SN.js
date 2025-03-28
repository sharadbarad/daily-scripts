// Get the resolution of the active document (original image)
var res = app.activeDocument.resolution;
var roundedNumber = Math.round(res);
resolution = (Math.floor(roundedNumber));

var docWidth = 4*resolution; //it is set as 4x6 print paper
var docHeight = 6*resolution;
var docRes = resolution;

var documentWidth = app.activeDocument.width;
var documentHeight = app.activeDocument.height;

app.activeDocument.selection.selectAll();

// Set stroke properties
var strokeColor = new SolidColor();	
strokeColor.rgb.red = 0; 
strokeColor.rgb.green = 0; 
strokeColor.rgb.blue = 0; 
var strokeWidth =  0.00039*(docRes*25.4); // Stroke width in pixels

// Apply stroke to the selection
app.activeDocument.selection.stroke(strokeColor, strokeWidth, StrokeLocation.INSIDE);

// Define the new canvas dimensions
var newWidth = documentWidth + ((3*resolution)/25.4); // New width in pixels
var newHeight = documentHeight + ((3*resolution)/25.4); // New height in pixels

// Resize the canvas
app.activeDocument.resizeCanvas(newWidth, newHeight, AnchorPosition.MIDDLECENTER);

app.activeDocument.selection.selectAll();
var strokeColor = new SolidColor(); // Create a new SolidColor object
strokeColor.rgb.red = 54; // Set RGB values for stroke color
strokeColor.rgb.green = 53;
strokeColor.rgb.blue = 53;
var strokeOpacity = 50;
var strokeWidth =  0.0001*(docRes*25.4);

// Create a new art layer
var strokeLayer = app.activeDocument.artLayers.add();
strokeLayer.name = "Stroke"; // Set the layer name

// Apply stroke to the selection on the new layer
app.activeDocument.selection.stroke(strokeColor, strokeWidth, StrokeLocation.INSIDE);

// Change opacity of the stroke layer
strokeLayer.opacity = strokeOpacity;

// Deselect the selection
app.activeDocument.selection.deselect()

// Merge the stroke layer with another layer
var strokeLayer = app.activeDocument.artLayers.getByName("Stroke"); // Assuming the stroke layer is named "Stroke"
var targetLayer = app.activeDocument.layers[1]; // Assuming the target layer is the first layer in the document

strokeLayer.merge(targetLayer); // Merge the stroke layer with the target layer

// Rotate the canvas 90 deg to fit in next doc
app.activeDocument.rotateCanvas(90); 

app.activeDocument.selection.selectAll();

// Copy the current selection
app.activeDocument.selection.copy();

// Create a new Photoshop document
var newDoc = app.documents.add(docWidth, docHeight, docRes, "4x6_Image")

// Paste the content from the clipboard
app.activeDocument.paste();

// Reference the pasted layer
var pastedLayer = app.activeDocument.activeLayer;

// Move the pasted layer to the top left corner
pastedLayer.translate(-pastedLayer.bounds[0].value, -pastedLayer.bounds[1].value);

// Duplicate the current layer
var duplicateLayer = pastedLayer.duplicate();

// Move the duplicate layer after the pastedLayer layer in layer tab
duplicateLayer.move(pastedLayer, ElementPlacement.PLACEAFTER);

// Move the duplicate layer after the pastedLayer layer
duplicateLayer.translate(pastedLayer.bounds[2].value - pastedLayer.bounds[0].value, pastedLayer.bounds[1].value - pastedLayer.bounds[1].value);

var frst = app.activeDocument.layers[0];
var scnd = app.activeDocument.layers[1];
frst.merge(scnd);

// Reference the active document
var doc = app.activeDocument;

// Reference the background layer
var backgroundLayer = doc.layers[1];

// Reference the first layer
var firstLayer = doc.layers[0];

// Calculate the horizontal center of the background layer
var backgroundCenterX = backgroundLayer.bounds[0].value + (backgroundLayer.bounds[2].value - backgroundLayer.bounds[0].value) / 2;

// Calculate the horizontal center of the first layer
var firstLayerCenterX = firstLayer.bounds[0].value + (firstLayer.bounds[2].value - firstLayer.bounds[0].value) / 2;

// Calculate the horizontal offset to align the first layer with the background layer
var offsetX = backgroundCenterX - firstLayerCenterX;

// Move the first layer to align its horizontal center with the background layer
firstLayer.translate(offsetX, 0);
	
for (var i =1; i<=2; i++){
	newlayer = doc.layers[0].duplicate();
	// Reference the above layer and the below layer
	var aboveLayer = doc.layers[1]; // Assuming the above layer is the first layer
	var belowLayer = doc.layers[0]; // Assuming the below layer is the second layer

	// Get the vertical distance between the two layers
	var verticalDistance = aboveLayer.bounds[3].value - belowLayer.bounds[1].value;

	// Move the duplicated layer vertically below the original layer
	belowLayer.translate(0, verticalDistance);
	var frst = app.activeDocument.layers[0];
	var scnd = app.activeDocument.layers[1];
	frst.merge(scnd);
}


// Reference the active document
var doc = app.activeDocument;

// Reference the background layer
var backgroundLayer =  doc.layers[1]// Replace "Background" with the name of your background layer

// Reference the first layer
var firstLayer = doc.layers[0]; // Assuming the first layer is at index 0

// Calculate the vertical center position of the background layer
var backgroundCenterY = backgroundLayer.bounds[1].value + (backgroundLayer.bounds[3].value - backgroundLayer.bounds[1].value) / 2;

// Calculate the vertical center position of the first layer
var firstLayerCenterY = firstLayer.bounds[1].value + (firstLayer.bounds[3].value - firstLayer.bounds[1].value) / 2;

// Calculate the vertical offset needed to align the centers
var yOffset = backgroundCenterY - firstLayerCenterY;

// Move the first layer to align its vertical center with the background layer
firstLayer.translate(0, yOffset);