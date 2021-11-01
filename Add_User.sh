#----------------------------------------------------
#					Script par : Rose
#					Le : 09/02/2019
#----------------------------------------------------
#!/bin/bash
login="$1"
password="$2"
utilisateurs=$(cut -d ':' -f 1 /etc/passwd)

for user in $utilisateurs ; do
	if [ "$user" = "$login" ] ; then
		echo "Cette utilisateur existe déjà."
		exit 1
	fi
done

if [ "$#" -eq 0 ] ; then
	echo "Afin d'être enregistré entrer un : <login> <password>."
	exit 0
fi

if [ "$#" -ne 2 ] ; then
	echo "Il vous faut 2 atguments pour être enregistré."
	exit 1
fi

elif [ -z "$password" ] ; then
	echo "Veillez entrer un mot de passe."
	exit 1

elif [ "$password" = "password" ] || [ "$password" = "motdepasse" ] || [ "$login" = "$password" ] ; then
	echo "Ce mot de passe n'est pas conforme."
	exit 1

hash=$(mkpasswd -m sha-512 "$password")
useradd -m -p "$hash" -s /bin/bash "$login"
echo "Utilisateur correctement enregistré."
