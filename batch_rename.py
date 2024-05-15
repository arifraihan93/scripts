#Name: batch_rename
#Label: Batch Rename
#Icon: SOP_name

import hou

# Get selected nodes
selected_nodes = hou.selectedNodes()

# List to store modified string data
modified_string_data_list = []

# Function to recursively collect string parameters from a node
def collect_string_data(node):
    # Iterate over parameters
    for parm in node.parms():
        # Check if parameter is a string type
        if parm.parmTemplate().type() == hou.parmTemplateType.String:
            # Append parameter value to the list
            modified_string_data_list.append(parm.evalAsString())
    
    # Recursively process child nodes
    for child in node.children():
        collect_string_data(child)

# Iterate over selected nodes and collect string data
for node in selected_nodes:
    collect_string_data(node)

# Prompt the user for search and replacement strings
dialog_result = hou.ui.readMultiInput('Enter search and replace strings:', input_labels=('Search:', 'Replace:'), buttons=('OK', 'Cancel'))

# Check if the user clicked OK
if dialog_result[0] == 0:
    search, replace = dialog_result[1]
    
    # Iterate over the collected string data and replace occurrences of the search string with the replacement string
    modified_string_data_list = [data.replace(search, replace) for data in modified_string_data_list]
    
    # Iterate over selected nodes
    for node in selected_nodes:
        # Function to recursively set modified string parameters to a node
        def set_modified_string_data(node):
            # Iterate over parameters
            for parm in node.parms():
                # Check if parameter is a string type
                if parm.parmTemplate().type() == hou.parmTemplateType.String:
                    # Set modified string data to the parameter
                    parm.set(modified_string_data_list.pop(0))
            
            # Recursively process child nodes
            for child in node.children():
                set_modified_string_data(child)
        
        # Call the function to set modified string data to the node parameters
        set_modified_string_data(node)
    
    #print("String data modified successfully.")
#else:
    #print("User canceled.")
