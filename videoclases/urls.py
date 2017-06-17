from django.contrib import admin
from django.conf.urls import url

import videoclases.views.views as vv
import videoclases.views.pegadogical_questions as pq

admin.autodiscover()

urlpatterns = [
    url(r'^$', vv.IndexView.as_view(), name='index'),

    url(r'^student/evaluate-conceptual-test-form/(?P<pk>\d+)/$',
        pq.ResponsePedagogicalQuestion.as_view(),
        name='evaluate_pedagogical_questions'),

    url(r'^student/send-videoclase/(?P<homework_id>\d+)/$',
        vv.EnviarVideoclaseView.as_view(),
        name='enviar_videoclase'),
    url(r'^student/evaluar-video/$',
        vv.EvaluacionesDeAlumnosFormView.as_view(),
        name='evaluar_video'),
    url(r'^student/evaluar-videoclase/(?P<homework_id>\d+)/$',
        vv.EvaluarVideoclaseView.as_view(),
        name='evaluar_videoclase'),
    url(r'^student/evaluar-videoclase-form/$',
        vv.EvaluarVideoclaseFormView.as_view(),
        name='evaluar_videoclase_form'),
    url(r'^student/ver-videoclase/(?P<homework_id>\d+)/$',
        vv.VerVideoclaseView.as_view(),
        name='ver_videoclase'),
    url(r'^student/',
        vv.AlumnoView.as_view(),
        name='student'),
    url(r'^cambiar-contrasena/',
        vv.ChangePasswordView.as_view(),
        name='change_password'),
    url(r'^cambiar-contrasena-student/(?P<course_id>\d+)/$',
        vv.ChangeStudentPasswordView.as_view(),
        name='change_student_password'),
    url(r'^cambiar-contrasena-student/',
        vv.ChangeStudentPasswordSelectCursoView.as_view(),
        name='change_student_password_select_course'),
    url(r'^login/',
        vv.IndexView.as_view(),
        name='login'),
    url(r'^logout/',
        vv.logout_view,
        name='logout'),
    url(r'^perfil/',
        vv.PerfilView.as_view(),
        name='perfil'),
    url(r'^teacher/students/(?P<student_id>\d+)/$',
        vv.VideoclasesAlumnoView.as_view(),
        name='videoclases_student'),
    url(r'^teacher/asignar-group-form/',
        vv.AsignarGrupoFormView.as_view(),
        name='asignar_group_form'),
    url(r'^teacher/borrar-student/(?P<course_id>\d+)/(?P<student_id>\d+)/$',
        vv.BorrarAlumnoView.as_view(),
        name='borrar_student'),
    url(r'^teacher/borrar-course/(?P<course_id>\d+)/$',
        vv.BorrarCursoFormView.as_view(),
        name='borrar_course'),
    url(r'^teacher/borrar-homework/',
        vv.BorrarTareaFormView.as_view(),
        name='borrar_homework'),
    url(r'^teacher/new-course/',
        vv.CrearCursoFormView.as_view(),
        name='crear_course'),
    url(r'^teacher/new-homework/',
        vv.CrearTareaView.as_view(),
        name='crear_homework'),
    url(r'^teacher/new-homework-form/',
        vv.CrearTareaFormView.as_view(),
        name='crear_homework_form'),

    url(r'^teacher/new-conceptual-test/create/$',
        pq.ConceptualTestsView.as_view(),
        name='new_conceptual_test_create'),
    url(r'^teacher/new-conceptual-test/$',
        pq.PedagogicalQuestionCreateView.as_view(),
        name='new_conceptual_test'),
    url(r'^teacher/new-test-conceptual-form/',
        pq.ConceptualTestsFormView.as_view(),
        name='new_conceptual_test_form'),
    url(r'^teacher/download-homeworks/(?P<course_id>\d+)/$',
        pq.download_homeworks,
        name='download_homeworks'),
    url(r'^teacher/download-pedagogical-questions/(?P<pk>\d+)/$',
        pq.DownloadPedagogicalQuestionAsExcel.as_view(),
        name='download_pedagogical_questions'),
    url(r'^teacher/download-pedagogical-questions-answers/(?P<pk>\d+)/$',
        pq.DownloadPedagogicalQuestionAnswersAsExcel.as_view(),
        name='download_pedagogical_questions_answers'),
    url(r'^teacher/pedagogical-questions/(?P<pk>\d+)/$',
        pq.PedagogicalQuestionEditView.as_view(),
        name='pedagogical_questions'),


    url(r'^teacher/course/(?P<course_id>\d+)/$',
        vv.CursoView.as_view(),
        name='course'),
    url(r'^teacher/descargar-course/(?P<course_id>\d+)/$',
        vv.descargar_course,
        name='descargar_course'),
    url(r'^teacher/descargar-groups-homework/(?P<homework_id>\d+)/$',
        vv.descargar_groups_homework,
        name='descargar_groups_homework'),
    url(r'^teacher/edit-student/(?P<course_id>\d+)/(?P<student_id>\d+)/$',
        vv.EditarAlumnoView.as_view(),
        name='editar_student'),
    url(r'^teacher/edit-course/(?P<course_id>\d+)/$',
        vv.EditarCursoView.as_view(),
        name='editar_course'),
    url(r'^teacher/edit-group-form/',
        vv.EditarGrupoFormView.as_view(),
        name='editar_group_form'),
    url(r'^teacher/edit-homework-form/(?P<homework_id>\d+)/$',
        vv.EditarTareaView.as_view(),
        name='editar_homework_form'),
    url(r'^teacher/subir-nota/',
        vv.SubirNotaFormView.as_view(),
        name='subir_nota'),
    url(r'^teacher/homework/(?P<homework_id>\d+)/$',
        vv.EditarTareaView.as_view(),
        name='homework'),
    url(r'^teacher/videoclases-homework/(?P<homework_id>\d+)/',
        vv.VideoclasesTareaView.as_view(),
        name='videoclases_homework'),
    url(r'^teacher/',
        vv.ProfesorView.as_view(),
        name='teacher'),
]
