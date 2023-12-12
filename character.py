"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name:      Le nom de l'arme
	:param power:     Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20
	
	# TODO: __init__
	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	# TODO: Propriétés
	@property
	def name(self):
		return self.__name
	
	# TODO: use
	def use(self, user, opponent):
		# TODO: Caculer et appliquer le dommage en utilisant la méthode compute_damage
		#damage, crit = ...
		damage = pass
		msg = ""
		if crit:
			msg += "Critical hit! "
		msg += f"{opponent.name} took {damage} dmg"
		return msg

	# TODO: compute_damage

	# TODO: make_unarmed
	@classmethod
	def make_unarmed(cls):
		return cls('Unarmed', 20, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name:    Le nom du personnage
	:param max_hp:  HP maximum
	:param attack:  Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level:   Le niveau d'expérience du personnage
	"""
	
	# TODO: __init__
	def __ini__(self, name, max_hp, attack, defense, level):
		self.__name = name

	
	# TODO: Propriétés

	def apply_turn(self, opponent):
		msg = f"{self.name} used {self.weapon.name}\n"
		msg += self.weapon.use(self, opponent)
		return msg
