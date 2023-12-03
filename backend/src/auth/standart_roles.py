__all__ = ("standart_roles",)

standart_roles = [
    {
        'id': 1,
        'name': 'student',
        'permissions': None
    },
    {
        'id': 2,
        'name': 'teacher',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 3,
        'name': 'tester',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 4,
        'name': 'moderator',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 5,
        'name': 'admin',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 6,
        'name': 'creator',
        'permissions': {
            'create_classrooms': True
        }
    }
]
