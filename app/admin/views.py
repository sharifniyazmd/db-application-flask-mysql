# Views for admin blueprint
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
# from forms import PatientForm, EmployeeAssignForm, RoleForm
from .. import db
from ..models import Patient, Employee


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)


# Patient Views


@admin.route('/patient', methods=['GET', 'POST'])
@login_required
def list_patients():
    """
    List all patients
    """
    #check_admin()

    patient = Patient.query.all()

    return render_template('admin/patients.html',
                           patient=patient, title="Patients")