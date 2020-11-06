# Cinemahole.
In the Great Era Entertainment, Cinema play a important role in our life.Cinema is important because it's the only art form that allows you to truly experience life through/in another person's eyes/head. We can create reality's that are otherwise inaccessible or impossible to grasp alone in our own heads.Movies affect many of us powerfully because the combined impact of images, music, dialogue, lighting, sound and special effects can elicit deep feelings and help us reflect on our lives. They can help us to better understand our own lives, the lives of those around us and even how our society and culture operate.
Beyond just entertaining us, in uncertain times great movies remind us of fundamental values that sometimes get lost in the commotion but that time and again have seen us through. Qualities that sound almost quaint when you name them, like integrity, courage and compassion.
And for this come forth my project CinemaHole.We know that everyone have their own  distinct flavour for movies.And for that I Created this project. It recommand person a movie acording to thier flavour. 
Its a WebApp, completely build on Django Framework and a ML model I've trained. What it does is that it shows you accurate recommendation on movies based on your profile.

# Requirements
Libraries required for this project-:
1. Django (Read the documentation if you don't know how to install and run https://docs.djangoproject.com/en/3.1/topics/install/).
2. Django-Restframework ( Installation Tutorial https://www.django-rest-framework.org/#installation).
3. Database (I suggest PostGres for faster search here is documentation for database setup https://docs.djangoproject.com/en/3.1/ref/databases/ ).
4. SKlearn ( Installation Guide https://scikit-learn.org/stable/install.html ).
5. Pandas ( Installation Guide https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html ).
6. Django-Taggit ( Installation https://pypi.org/project/django-taggit/ )
                      
                      ( ******* And After All of that You must have python in your machine  ******* )

# How ot run
1. Clone the project to your local Directorty.
2. Then Cd "Project_Folder"
3. Create a virtual environment ( On macOS and Linux: python3 -m venv your_env_name , On Windows(****Creep****): py -m venv your_env_name )
4. Activate Environment ( On macOS and Linux: env/bin/activate On Windows(****Again Creeps****): .\env\Scripts\activate )
                    
                    [****** Important All this above and below Commands must run on your project Source Directories *****]
                    
5. Now install All the required libraries with pip as mentioned in menioned in documentation.
6. After that run: 'python manage.py loaddata Movie.json
7. Now Create a Super User by running following command 'python manage.py createsuperuser' and fill the asked details.
8. Now test of your patience ends here Run the following command for starting project 'python manage.py runserver'
9. Now run towards your browser and type 'localhost:port_number_mention when you run the previous command/CinemaHole'
10. Hmm How's it, please give your feedback at 'balwantdod223@gmail.com' and please don't complain about the design or make fun of it.I got all the recommandation from my family(farmers) they never touched a computer in their life. Then don't expect a good design from them,all you gonna see is green and coral.........
