from flask import Blueprint, render_template, request, redirect, url_for
 
main = Blueprint('main', __name__)


@main.route('/')
def search():
    return render_template('search.html')

@main.route('/results', methods=['POST','GET'])
def find_res():
    from .mainscr import func
    if request.method == "POST" :
        keyword = request.form.get('comment')
        func(keyword)
        return render_template('result.html')
    
    return render_template('result.html')
