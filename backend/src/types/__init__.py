from .class_invite import (
    ClassInviteModel,
)
from .course import (
    CreateModuleModel,
    CreateTaskModel,
    FullCourseDataModel,
    FullModuleModel,
    FullTaskModel,
    ReadCourseDataModel,
    ReadModuleModel,
    ReadTaskModel,
    UpdateTaskModel,
)
from .course.course import (
    CourseCreateModel,
    CourseFullModel,
    CourseUpdateModel,
    CourseUserReadModel,
    CourseWithDataModel,
)
from .extra_params import ExtraParamsModel
from .simple_solution import (
    CreateSimpleSolutionModel,
    FullSimpleSolutionModel,
    ReadSimpleSolutionModel,
    UpdateSimpleSolutionModel,
)
from .solution import (
    CreateSolutionModel,
    FullSolutionModel,
    ReadSolutionModel,
    UpdateSolutionModel,
)
from .user import (
    UserReadModel,
)

__all__ = (
    "CourseWithDataModel",
    "CourseUserReadModel",
    "CourseCreateModel",
    "CourseUpdateModel",
    "CourseFullModel",
    "FullModuleModel",
    "ReadModuleModel",
    "FullCourseDataModel",
    "ReadCourseDataModel",
    "FullTaskModel",
    "ReadTaskModel",
    "ClassInviteModel",
    "CreateModuleModel",
    "UserReadModel",
    "CreateTaskModel",
    "UpdateTaskModel",
    "ExtraParamsModel",

    "CreateSolutionModel",
    "ReadSolutionModel",
    "UpdateSolutionModel",
    "FullSolutionModel",

    "CreateSimpleSolutionModel",
    "ReadSimpleSolutionModel",
    "UpdateSimpleSolutionModel",
    "FullSimpleSolutionModel",
)
