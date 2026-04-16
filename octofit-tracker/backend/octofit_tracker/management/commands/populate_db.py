from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Limpar dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Criar times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Criar usuários
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='captain', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', first_name='Bruce', last_name='Wayne', team=dc)
        diana = User.objects.create_user(username='diana', email='diana@prince.com', password='wonder', first_name='Diana', last_name='Prince', team=dc)

        # Criar atividades
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=diana, type='yoga', duration=50, distance=0)

        # Criar workouts
        Workout.objects.create(name='Cardio Blast', description='Intenso treino de cardio', duration=40)
        Workout.objects.create(name='Força Total', description='Treino de força para super-heróis', duration=60)

        # Criar leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=95)
        Leaderboard.objects.create(user=diana, points=98)

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de super-heróis!'))
