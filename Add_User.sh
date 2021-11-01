#----------------------------------------------------
#					Script par : Rose
#					Le : 09/02/2019
#----------------------------------------------------
#!/bin/bash

function log_event() {
	type="$1"
	msg="$2"
	today=$(date "+%d-%m-%Y")
	hour=$(date "+%H:%I:%S")
	file="/var/log/useradd_${today}.log"
	if [ ! -f "$file" ] ; then
		touch "$file"
	fi
	echo "$hour - $type - $msg" >> $(echo "$file")
	echo "[${type}] $msg"
}

# Afficher l'aide si nb arg = 0
if [ "$#" -eq 0 ] ; then
	echo "Usage : $0 <login> <password>"
	exit 0
fi

# Erreur si nb arg != 2
if [ "$#" -ne 2 ] ; then
	echo "[!] Wrong number of arguments"
	exit 1
fi

# Obtenir les valeurs
login="$1"
password="$2"

# Erreur si l'utilisateur existe deja
users=$(cut -d ':' -f 1 /etc/passwd)
for user in $users ; do
	if [ "$user" = "$login" ] ; then
		log_event "error" "User already exists"
		exit 1
	fi
done

# Check #1 : différent du login
if [ "$login" = "$password" ] ; then
	log_event "error" "Password same as login"
	exit 1
# Check #2 : non nul
elif [ -z "$password" ] ; then
	log_event "error" "Password is null"
	exit 1
# Check #3 : différent de password
elif [ "$password" = "password" ] ; then
	log_event "error" "Password is password"
	exit 1
# Check #4 : différent de motdepasse
elif [ "$password" = "motdepasse" ] ; then
	log_event "error" "Password is motdepasse"
	exit 1
# Check 5 : seulement des chiffres
elif [ "$password" -eq "$password" ] 2> /dev/null ; then
	log_event "error" "Password contains only digits"
	exit 1
fi

# Vérifier si le mot de passe est dans le dictionnaire
while read line ; do
	if [ "$line" = "$password" ] ; then
		log_event "error" "Password is in dictionary"
		exit 1
	fi
done < dict.txt

# Hacher le mot de passe
hash=$(mkpasswd -m sha-512 "$password")

# Ajouter l'utilisateur
useradd -m -p "$hash" -s /bin/bash "$login" > /dev/null 2> /dev/null

if [ "$?" -ne 0 ] ; then
	log_event "error" "useradd failed with exit status $?"
else
	log_event "success" "User $login added"
fi
