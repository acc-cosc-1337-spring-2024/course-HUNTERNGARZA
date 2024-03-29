def add_inventory(widgets: dict, widget_name, quantity):
    if widgets.get(widget_name) is None:
        widgets[widget_name] = quantity
        return

    widgets[widget_name] += quantity


def remove_inventory(widgets: dict, widget_name):
    if widgets.get(widget_name) is not None:
        del widgets[widget_name]
        return "Record Deleted"
    
    return "Item not found"
