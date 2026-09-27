### Question 1  
Create a simple table to display course information.  
a) Create a table with a border of 1.  
b) Add a header row with two columns: “Course Name” and “Duration”.  
c) Add two data rows with the following information:  
   - Web Development – 4 months  
   - Data Analytics – 5 months  

### Question 2  
Create a table that includes a caption.  
a) Create a table with a border of 1.  
b) Add the caption “Monthly Workshop Schedule”.  
c) Create a header row with “Workshop” and “Month”.  
d) Add two data rows of your choice related to workshops.  

### Question 3  
Create a table that uses colspan.  
a) Create a table with a border of 1.  
b) In the first row, create a single header cell that spans 2 columns and contains the text “Institute Programs”.  
c) In the next row, add two normal data cells with program names of your choice.  

### Question 4  
Create a table that uses rowspan.  
a) Create a table with a border of 1.  
b) In the first data row, create a cell with the text “Programming Track” that spans 2 rows.  
c) Next to it, add “Semester 1” in the first row and “Semester 2” in the second row.  

### Question 5  
Create a table using semantic grouping elements.  
a) Create a table with a border of 1 and a caption “Student Performance Report”.  
b) Use `<thead>` for a header row containing “Student Name” and “Grade”.  
c) Use `<tbody>` to add two student records.  
d) Use `<tfoot>` to add a footer row that spans both columns and shows “End of Report”.  

### Question 6  
Create a table that uses `scope="col"`.  
a) Create a table with a border of 1.  
b) In the header row, add three header cells: “Name”, “Age”, and “City”.  
c) Give each header cell `scope="col"`.  
d) Add two data rows with suitable information.  

### Question 7  
Create a table that uses `scope="row"`.  
a) Create a table with a border of 1.  
b) Create three rows where the first cell of each row is a header cell with `scope="row"`.  
c) Use the row headers: “Course”, “Duration”, and “Mode”.  
d) Add suitable data in the second column.  

### Question 8  
Create a table that uses both `id` and `headers` attributes for accessibility.  
a) Create a table with a border of 1.  
b) In the header row, give the header cells the ids `subject`, `marks`, and `result`.  
c) In the data rows, use the `headers` attribute on each `<td>` to correctly link them to the related header ids.  
d) Add at least two data rows.  

### Question 9  
Create a more complete table using multiple features together.  
a) Create a table with a border of 1 and a caption “Department Summary”.  
b) Use `<thead>` with column headers that have `scope="col"`.  
c) Use `<tbody>` to add two department records.  
d) Use `<tfoot>` to show an overall total row that uses `colspan`.  

### Question 10  
Create one complete table that includes **all** of the following features:  
a) A border of 1  
b) A caption  
c) A header row using `<thead>` and `scope="col"`  
d) At least one cell that uses `colspan` or `rowspan`  
e) Body content inside `<tbody>`  
f) A footer row inside `<tfoot>`  
g) At least one row header using `scope="row"` **or** proper use of `id` and `headers` attributes  


### Question 11  
Create a timetable-style table using rowspan.  
a) Create a table with a border of 1.  
b) Add a caption “Weekly Class Schedule”.  
c) In the first column, create a cell with the text “Monday” that spans 3 rows using `rowspan`.  
d) Next to it, add three different subjects in separate rows (for example: HTML, CSS, JavaScript).  
e) Add a proper header row for the columns.  

### Question 12  
Create a comparison table using both colspan and rowspan.  
a) Create a table with a border of 1.  
b) In the first row, create a header cell that spans 3 columns with the text “Course Comparison”.  
c) In the following rows, use `rowspan` on one cell to merge two rows for a common category (for example “Duration”).  
d) Fill the remaining cells with suitable comparison data.  

### Question 13  
Create a detailed marks table with semantic structure and accessibility.  
a) Create a table with a border of 1 and caption “Internal Assessment Marks”.  
b) Use `<thead>` with column headers and give each header `scope="col"`.  
c) Use `<tbody>` to add three student records.  
d) Use `<tfoot>` to show the highest score, and make that footer cell span appropriate columns using `colspan`.  

### Question 14  
Create a table that properly uses both `scope` and `headers` attributes together.  
a) Create a table with a border of 1.  
b) Give the column headers ids and `scope="col"`.  
c) Make the first cell of each data row a row header with `scope="row"` and also give it an id.  
d) In the data cells, use the `headers` attribute to link each cell to both its column header and row header.  
e) Add at least two complete data rows.  

### Question 15  
Create one advanced table that combines multiple features.  
a) Create a table with a border of 1.  
b) Add a meaningful caption.  
c) Use `<thead>`, `<tbody>`, and `<tfoot>`.  







---

**Answers**

---




<!DOCTYPE html>
<html>
<head>
    <title>HTML Table Questions 1-15</title>
</head>

<body>

    <h1>HTML Table Practice</h1>


    <h2>Question 1</h2>

    <table border="1">
        <tr>
            <th>Course Name</th>
            <th>Duration</th>
        </tr>
        <tr>
            <td>Web Development</td>
            <td>4 months</td>
        </tr>
        <tr>
            <td>Data Analytics</td>
            <td>5 months</td>
        </tr>
    </table>


    <h2>Question 2</h2>

    <table border="1">
        <caption>Monthly Workshop Schedule</caption>

        <tr>
            <th>Workshop</th>
            <th>Month</th>
        </tr>

        <tr>
            <td>Web Development</td>
            <td>January</td>
        </tr>

        <tr>
            <td>Python Programming</td>
            <td>February</td>
        </tr>
    </table>


    <h2>Question 3</h2>

    <table border="1">
        <tr>
            <th colspan="2">Institute Programs</th>
        </tr>

        <tr>
            <td>Web Development</td>
            <td>Data Science</td>
        </tr>
    </table>


    <h2>Question 4</h2>

    <table border="1">
        <tr>
            <td rowspan="2">Programming Track</td>
            <td>Semester 1</td>
        </tr>

        <tr>
            <td>Semester 2</td>
        </tr>
    </table>


    <h2>Question 5</h2>

    <table border="1">
        <caption>Student Performance Report</caption>

        <thead>
            <tr>
                <th>Student Name</th>
                <th>Grade</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>Rahul</td>
                <td>A</td>
            </tr>

            <tr>
                <td>Ankit</td>
                <td>B+</td>
            </tr>
        </tbody>

        <tfoot>
            <tr>
                <td colspan="2">End of Report</td>
            </tr>
        </tfoot>
    </table>


    <h2>Question 6</h2>

    <table border="1">
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Age</th>
            <th scope="col">City</th>
        </tr>

        <tr>
            <td>Rahul</td>
            <td>20</td>
            <td>Delhi</td>
        </tr>

        <tr>
            <td>Ankit</td>
            <td>21</td>
            <td>Mumbai</td>
        </tr>
    </table>


    <h2>Question 7</h2>

    <table border="1">
        <tr>
            <th scope="row">Course</th>
            <td>Web Development</td>
        </tr>

        <tr>
            <th scope="row">Duration</th>
            <td>4 Months</td>
        </tr>

        <tr>
            <th scope="row">Mode</th>
            <td>Online</td>
        </tr>
    </table>


    <h2>Question 8</h2>

    <table border="1">
        <tr>
            <th id="subject">Subject</th>
            <th id="marks">Marks</th>
            <th id="result">Result</th>
        </tr>

        <tr>
            <td headers="subject">Mathematics</td>
            <td headers="marks">85</td>
            <td headers="result">Pass</td>
        </tr>

        <tr>
            <td headers="subject">Science</td>
            <td headers="marks">90</td>
            <td headers="result">Pass</td>
        </tr>
    </table>


    <h2>Question 9</h2>

    <table border="1">
        <caption>Department Summary</caption>

        <thead>
            <tr>
                <th scope="col">Department</th>
                <th scope="col">Students</th>
                <th scope="col">Faculty</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>Computer Science</td>
                <td>120</td>
                <td>10</td>
            </tr>

            <tr>
                <td>Data Science</td>
                <td>80</td>
                <td>8</td>
            </tr>
        </tbody>

        <tfoot>
            <tr>
                <td colspan="3">Overall Total: 200 Students</td>
            </tr>
        </tfoot>
    </table>


    <h2>Question 10</h2>

    <table border="1">
        <caption>Student Course Report</caption>

        <thead>
            <tr>
                <th scope="col">Student</th>
                <th scope="col">Course</th>
                <th scope="col">Duration</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <th scope="row">Rahul</th>
                <td>Web Development</td>
                <td rowspan="2">4 Months</td>
            </tr>

            <tr>
                <th scope="row">Ankit</th>
                <td>Web Development</td>
            </tr>
        </tbody>

        <tfoot>
            <tr>
                <td colspan="3">End of Report</td>
            </tr>
        </tfoot>
    </table>


    <h2>Question 11</h2>

    <table border="1">
        <caption>Weekly Class Schedule</caption>

        <thead>
            <tr>
                <th scope="col">Day</th>
                <th scope="col">Subject</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <th rowspan="3" scope="row">Monday</th>
                <td>HTML</td>
            </tr>

            <tr>
                <td>CSS</td>
            </tr>

            <tr>
                <td>JavaScript</td>
            </tr>
        </tbody>
    </table>


    <h2>Question 12</h2>

    <table border="1">
        <tr>
            <th colspan="3">Course Comparison</th>
        </tr>

        <tr>
            <th>Category</th>
            <th>Web Development</th>
            <th>Data Science</th>
        </tr>

        <tr>
            <th rowspan="2">Duration</th>
            <td>4 Months</td>
            <td>5 Months</td>
        </tr>

        <tr>
            <td>Online</td>
            <td>Online</td>
        </tr>
    </table>


    <h2>Question 13</h2>

    <table border="1">
        <caption>Internal Assessment Marks</caption>

        <thead>
            <tr>
                <th scope="col">Student Name</th>
                <th scope="col">Maths</th>
                <th scope="col">Science</th>
                <th scope="col">Total</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>Rahul</td>
                <td>85</td>
                <td>90</td>
                <td>175</td>
            </tr>

            <tr>
                <td>Ankit</td>
                <td>80</td>
                <td>88</td>
                <td>168</td>
            </tr>

            <tr>
                <td>Rohan</td>
                <td>92</td>
                <td>95</td>
                <td>187</td>
            </tr>
        </tbody>

        <tfoot>
            <tr>
                <td colspan="3">Highest Score</td>
                <td>187</td>
            </tr>
        </tfoot>
    </table>


    <h2>Question 14</h2>

    <table border="1">
        <thead>
            <tr>
                <th id="student" scope="col">Student</th>
                <th id="maths" scope="col">Maths</th>
                <th id="science" scope="col">Science</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <th id="rahul" scope="row">Rahul</th>
                <td headers="rahul maths">85</td>
                <td headers="rahul science">90</td>
            </tr>

            <tr>
                <th id="ankit" scope="row">Ankit</th>
                <td headers="ankit maths">80</td>
                <td headers="ankit science">88</td>
            </tr>
        </tbody>
    </table>


    <h2>Question 15</h2>

    <table border="1">
        <caption>Advanced Course Report</caption>

        <thead>
            <tr>
                <th scope="col">Department</th>
                <th scope="col">Course</th>
                <th scope="col">Duration</th>
                <th scope="col">Mode</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <th rowspan="2" scope="row">Computer Science</th>
                <td>Web Development</td>
                <td>4 Months</td>
                <td>Online</td>
            </tr>

            <tr>
                <td>Python Programming</td>
                <td>3 Months</td>
                <td>Offline</td>
            </tr>

            <tr>
                <th scope="row">Data Science</th>
                <td>Data Analytics</td>
                <td>5 Months</td>
                <td>Online</td>
            </tr>
        </tbody>

        <tfoot>
            <tr>
                <td colspan="4">End of Course Report</td>
            </tr>


</body>
</html>
d) Include at least one `colspan` and one `rowspan`.  
e) Use `scope="col"` on column headers and `scope="row"` on at least one row header.  
f) Optionally use `id` and `headers` for better accessibility.  
