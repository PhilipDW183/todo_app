from flask import session

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'Create new item' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Complete this item' },
    { 'id': 3, 'status': 'Not Started', 'title': 'Completed item' },
]


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS.copy())


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def remove_item(id):
    """
    Removes an existing item from the session. If not existing item matches the ID of the specified item, nothing
    is removed

    Args:
        id: item id to be removed

    Returns:

    """
    existing_items = get_items()

    updated_items = [item for item in existing_items if int(item['id']) != int(id)]

    session['items'] = updated_items

    return id

def update_item(id, status):
    """
    Updates the status of the item.

    Args:
        id: item id to be updated
        status: item status to be updated to
    
    returns:
        item_to_update
    """
    item_to_update = get_item(id)
    item_to_update["status"] = status
    save_item(item_to_update)

    return item_to_update
