// Variables to assist with sort order and hiding dropdown
var title_ascending = true, date_ascending = true, hidden = true;

// A function that uses binary search to place the text in sorted position
// Row_tracker keeps track of what the original index was in the table.
function binary_insert(column, child, row_tracker, row_index, left_index, right_index) {
    var middle_index;

    // Add to array if no items present
    if (column.length == 0) {
        column.push(child);
        row_tracker.push(row_index);
        return;
    }

    // Add to array either in the back or front if only one item present
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

    // Get the middle index using bitwise or 0
    middle_index = ((left_index + right_index - 1) / 2) | 0;
    
    // If the value at the middle index is the same then insert the new row before the current row
    // at that index.
    if (column[middle_index] == child) {
        column.splice(middle_index, 0, child);
        row_tracker.splice(middle_index, 0, row_index);
        return;
    }

    // If the value at the middle index is greaterl then if it is at the 0 index
    // insert at the beginning. Otherwise check to see if the previous number is less
    // than the new number.
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

    // If the value at the middle index is less, then if it is at the last index
    // insert at the end. Otherwise check to see if the following number is greater
    // than the new number.
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

// Function that sorts the variable
function sortTable(index) {
    var column = [], row_tracker = [], new_rows = [];
    var table, rows, i;
    
    // Get all the row elements and the table as a whole
    rows = document.getElementsByTagName("tr");
    table = document.getElementById("results");
    
    // Loop through the rows (ommitting the table header)
    // to get the text in the row of the selected column.
    // Will then insert into column array sorted.
    for (i = 1; i < rows.length; i++) {
        child = rows[i].children[index].innerHTML.toLowerCase();
        binary_insert(column, child, row_tracker, i, 0, column.length);
    }

    // Push the table row elements into new_row
    for (i = 0; i < row_tracker.length; i++) {
        new_rows.push(rows[row_tracker[i]]);
    }

    // Delete the row elements from the DOM
    for (i = 0; i < row_tracker.length; i++) {
        table.deleteRow(1);
    }

    // For the title, check whether to sort via ascending or descending
    if (index == 0) {
        if (title_ascending == true) {
            for (i = 0; i < new_rows.length; i++) {
                table.appendChild(new_rows[i]);
            }
            title_ascending = false;
            date_ascending = true;
        } else {
            for (i = new_rows.length - 1; i >= 0; i--) {
                table.appendChild(new_rows[i]);
            }
            title_ascending = true;
            date_ascending = true;
        }
    }

    // For the date, check whether to sort via ascending or descending
    if (index == 3) {
        if (date_ascending == true) {
            for (i = 0; i < new_rows.length; i++) {
                table.appendChild(new_rows[i]);
            }
            date_ascending = false;
            title_ascending = true;
        } else {
            for (i = new_rows.length - 1; i >= 0; i--) {
                table.appendChild(new_rows[i]);
            }
            date_ascending = true;
            title_ascending = true;
        }
    }

    // Close the sort option dropdown
    toggleDropdown()
}

// Function that toggles the dropdown menu when the dropdown button is selected
function toggleDropdown() {
    if (hidden) {
        document.getElementById("dropdown-items").classList.remove("hide");
        hidden = false;
    } else {
        document.getElementById("dropdown-items").classList.add("hide");
        hidden = true;
    } 
}

// Function that hides dropdown when clicking in the window
// Works by adding the hide class which contains display: none
window.onclick = function(event) {
    if (!event.target.matches('.sort-option') && !event.target.matches('.sort-button') && !hidden) {
        document.getElementById("dropdown-items").classList.add("hide");
        hidden = true
    }
}