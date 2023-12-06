import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyfiglet
from termcolor import colored

def envoyer_email(adresse_expediteur, mot_de_passe, adresse_destinataire, nom_expediteur, sujet, message):
    serveur_smtp = 'Serveur'
    port_smtp = 0.0.0.0

    msg = MIMEMultipart()
    msg['From'] = f'{nom_expediteur} <{adresse_expediteur}>'
    msg['To'] = adresse_destinataire
    msg['Subject'] = sujet
    msg.attach(MIMEText(message, 'plain'))

    serveur = smtplib.SMTP(serveur_smtp, port_smtp)
    serveur.starttls()
    serveur.login(adresse_expediteur, mot_de_passe)
    serveur.sendmail(adresse_expediteur, adresse_destinataire, msg.as_string())
    serveur.quit()

if __name__ == "__main__":
    out = pyfiglet.figlet_format("BlackSpam", font="avatar")
    print(colored(out, 'green'))
    print(colored("                                                    par Marc Regis", 'red'))
    print(colored("                                              Telegram: https://t.me/the_667_hacker", 'red'))

    parser = argparse.ArgumentParser(description='Envoi d\'e-mail')
    parser.add_argument('--adresse-expediteur', required=True, help='Adresse e-mail de l\'expéditeur')
    parser.add_argument('--mot-de-passe', required=True, help='Mot de passe du compte e-mail')
    parser.add_argument('--adresse-destinataire', required=True, help='Adresse e-mail du destinataire')
    parser.add_argument('--nom-expediteur', default='jumia', help='Nom personnalisé de l\'expéditeur')
    parser.add_argument('--sujet', default='Test', help='Sujet de l\'e-mail')
    parser.add_argument('--message', default='Ceci est un test', help='Corps du message')

    args = parser.parse_args()

    print("\nArguments fournis :")
    print(f"Adresse expéditeur : {args.adresse_expediteur}")
    print(f"Adresse destinataire : {args.adresse_destinataire}")
    print(f"Nom expéditeur : {args.nom_expediteur}")
    print(f"Sujet : {args.sujet}")
    print(f"Message : {args.message}\n")

    envoyer_email(args.adresse_expediteur, args.mot_de_passe, args.adresse_destinataire, args.nom_expediteur, args.sujet, args.message)
    print(colored('E-mail envoyé avec succès', 'green'))
