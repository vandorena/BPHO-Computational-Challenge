## Sequence of Events to Dynamically update graphs and charts

1. The requested **html** page loads in the Browser
2. That page then makes an **ajax** request to ge tnew data.
3. The **ajax** request returns the data as text.
4. The original page pareses the text returned by the **ajax** request, into a useable format, such as an array, and then produces a chart with it.

## What We can use to render the graphs

There is this library called **RGraph** which is a JS based library that can create charts. We would parse the text data to this.

### We need to acknowledge the fact that we might need to migrate the processing of the data from the serverside to the client side, and thus may need to rewrite the functions in JS. This would have advantages such as increasing performance (decreasing time taken to make requests). This is the approach that Desmos took, and thier calculator is noticably faster than others such as mathaway or symbolab.