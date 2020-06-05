from flask import render_template, flash, redirect, url_for
from app.forms import Email
from app import app
from app.src.ward import find_ward
from app.src.contact_aldermxn import ContactAldermxn

@app.route('/', methods=['GET','POST'])
def index():
    form = Email()
    if form.validate_on_submit():
        contact = ContactAldermxn(form.ward.data)
        if not contact:
            flash('Please enter a ward between 1 and 50.')
            return redirect(url_for('index'))
        else:
            
            return redirect(f"mailto:{contact[1]}?subject=Call%20to%20Action&body=ATTN:%20{contact[0]}%0D%0A%0D%0AMy%20name%20is%20{form.name.data}%20and%20I%20am%20a%20resident%20of%20the%2046th%20ward%20in%20Chicago.%0D%0A%0D%0AI%20am%20demanding%20that%20you%20%20call%20for%20an%20emergency%20city%20council%20meeting%20and%20deny%20mayor%20Lori%20Lightfoot's%20proposed%20budget.%0D%0A%0D%0AI%20would%20like%20to%20redirect%20money%20away%20from%20the%20CPD%20and%20into%20social%20service%20programs%20like%20SWAP%2C%20RCP%2C%20WRAP%2C%20drug%20treatment%20programs%2C%20and%20creating%20therapeutic%20communities%2C%20which%20are%20better%20alternatives%20to%20incarceration.%0D%0A%0D%0AThis%20call%20to%20action%20as%20officers%20are%20being%20paid%20overtime%20for%20suppressing%20protesters.%0D%0A%0D%0AThank%20you.")
           
    return render_template('index.html', form=form)