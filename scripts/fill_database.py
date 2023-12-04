from accounts.models import User
from plots.models import Plot
from django.contrib.gis.geos import Polygon


user_1 = User.objects.create(username='user_1', email='user_1@example.com')
user_2 = User.objects.create(username='user_2', email='user_2@example.com')

coords_1 = (
	(3.961469542247613, 49.334629365425116),
	(3.9645490407681905, 49.335888470660024),
	(3.9669643337260254, 49.333763711892175),
	(3.9638848352041407, 49.33163886140392),
	(3.9621337478103555, 49.33250455230413),
	(3.961469542247613, 49.334629365425116)
	)

coords_2 = (
	(3.9687299914146195, 49.34166675762563),
	(3.973245391434858, 49.34384454980244),
	(3.9760015446957198, 49.34231628467697),
	(3.9705478797345677, 49.3398709617494),
	(3.9687299914146195, 49.34166675762563)
	)

coords_3 = (
	(3.959608302910221, 49.33996627477725),
	(3.96396858848021, 49.3409696673109),
	(3.96396858848021, 49.3377130217818),
	(3.95932036248885, 49.3377130217818),
	(3.959608302910221, 49.33996627477725)
	)

plot_1 = Plot.objects.create(
	name='plot_1',
	zone=Polygon(coords_1),
	user=user_1
	)

plot_2 = Plot.objects.create(
	name='plot_2',
	zone=Polygon(coords_2),
	user=user_2
	)

plot_3 = Plot.objects.create(
	name='plot_3',
	zone=Polygon(coords_3),
	user=user_2
	)
