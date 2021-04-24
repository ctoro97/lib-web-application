function binary_insert(column, child, row_tracker, row_index, left_index, right_index) {
    var middle_index;

    if (column.length == 0) {
        column.push(child);
        row_tracker.push(row_index);
        return;
    }

    if (column.length == 1) {
        if (column[0] >= child) {
            column.unshift(child);
            row_tracker.unshift(row_index);
            return;
        }
        column.push(child);
        row_tracker.push(row_index);
        return;
    }

    middle_index = ((left_index + right_index - 1) / 2) | 0;
    // console.log("--------------------------------------------------------------");
    // console.log(column);
    // console.log(child);
    // console.log(middle_index);
    
    if (column[middle_index] == child) {
        column.splice(middle_index, 0, child);
        row_tracker.splice(middle_index, 0, row_index);
        return;
    }

    if (column[middle_index] > child) {
        if (middle_index == 0) {
            column.unshift(child);
            row_tracker.unshift(row_index)
            return;
        }
        
        if (column[middle_index - 1] < child) {
            column.splice(middle_index, 0, child);
            row_tracker.splice(middle_index, 0, row_index);
            return;
        }
        binary_insert(column, child, row_tracker, row_index, left_index, middle_index - 1);
        return;
    }

    if (column[middle_index] < child) {
        if (middle_index == column.length - 1) {
            column.push(child);
            row_tracker.push(row_index);
            return;
        }

        if (column[middle_index + 1] > child) {
            column.splice(middle_index + 1, 0, child);
            row_tracker.splice(middle_index + 1, 0, row_index);
            return;
        }
        binary_insert(column, child, row_tracker, row_index, middle_index + 1, right_index);
        return;
    }

}

function sortTable(index) {
    var column = [], row_tracker = [], new_rows = [];
    var table, rows, i;
    
    rows = document.getElementsByTagName("tr");
    table = document.getElementById("results");
    
    for (i = 1; i < rows.length; i++) {
        child = rows[i].children[index].innerHTML.toLowerCase();
        binary_insert(column, child, row_tracker, i, 0, column.length);
    }

    for (i = 0; i < row_tracker.length; i++) {
        console.log(row_tracker[i]);
        console.log(rows[row_tracker[i]]);
        new_rows.push(rows[row_tracker[i]]);
    }

    for (i = 0; i < row_tracker.length; i++) {
        table.deleteRow(1);
    }

    for (i = 0; i < new_rows.length; i++) {
        table.appendChild(new_rows[i]);
    }

    console.log(column);
    console.log(new_rows);
}