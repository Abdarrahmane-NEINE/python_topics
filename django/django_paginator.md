# Django Paginator Guide

## Django Paginator (`django.core.paginator`)

### Basic Usage

#### Import:
```python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
```

#### Example Code:
```python
items = MyModel.objects.all()
paginator = Paginator(items, 10)  # 10 items per page
page = request.GET.get('page', 1)

try:
    page_obj = paginator.page(page)
except PageNotAnInteger:
    page_obj = paginator.page(1)
except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)
```

### Key Attributes & Methods

#### Paginator Object
- **count**: Returns the total number of items across all pages.
- **num_pages**: Returns the total number of pages.  
  *Example:* `total_pages = paginator.num_pages`
- **page_range**: Provides a range of page numbers (e.g., `range(1, paginator.num_pages + 1)`) which is handy for iterating over pages in templates.
- **object_list**: The original list of items that was passed to the paginator.

#### Page Object (returned by `paginator.page(page_number)`) 
- **object_list**: Contains the list of items for the current page.
- **number**: The current page number.
- **has_next()**: Returns `True` if there is a next page; otherwise, `False`.
- **has_previous()**: Returns `True` if there is a previous page; otherwise, `False`.
- **next_page_number()**: Returns the number of the next page. (Useful when `has_next()` is `True`.)
- **previous_page_number()**: Returns the number of the previous page. (Useful when `has_previous()` is `True`.)
- **start_index()**: Returns the 1-indexed position of the first item on the current page.
- **end_index()**: Returns the 1-indexed position of the last item on the current page.

### Advanced Usage

#### Error Handling
- Use `try/except` to gracefully fall back when a page number is invalid.
- **PageNotAnInteger**: Raised if the page number provided is not an integer.
- **EmptyPage**: Raised if the page number is out of range (e.g., too high).

#### Template Integration
- Utilize pagination template tags (e.g., iterate over `page_obj.paginator.page_range`).
- Implement custom logic in your view or template to display a subset of page numbers for better UI/UX.

## DRF Pagination (Django REST Framework)

### Basic Setup

#### Global Configuration in `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

#### Automatic Metadata
When returning a queryset, DRF paginates the response with metadata:
```json
{
    "count": 102,
    "next": "http://example.com/api/items/?page=3",
    "previous": "http://example.com/api/items/?page=1",
    "results": [ ... ]
}
```

### Pagination Classes

#### **PageNumberPagination**
- Simple page-based approach.
- Customizable via parameters like `page_size_query_param` (allowing clients to set a custom page size) and `max_page_size`.

#### **LimitOffsetPagination**
- Uses `limit` and `offset` query parameters.
- Example configuration:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}
```

#### **CursorPagination**
- Provides consistent ordering for large datasets.
- Set an `ordering` attribute to define cursor order.

### Advanced Customization

#### **Custom Pagination Class Example:**
```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
```

#### **Integration in Views:**
- Set `pagination_class = CustomPagination` in your view or viewset.

#### **Response Customization:**
- Override `get_paginated_response()` to adjust metadata (e.g., adding custom links or additional information).

