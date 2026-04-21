from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .model import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)<1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    try:
        note_data = request.get_json()
        note_id = note_data.get('noteId')
        
        if not note_id:
            return jsonify({'error': 'Note ID missing'}), 400
            
        note = Note.query.get(note_id)
        if note:
            if note.user_id == current_user.id:
                db.session.delete(note)
                db.session.commit()
                return jsonify({'success': True}), 200
            else:
                return jsonify({'error': 'Unauthorized'}), 403
        else:
            return jsonify({'error': 'Note not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500