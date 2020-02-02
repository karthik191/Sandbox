import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(senderEmail):
    firstName = senderEmail.split('.')[0]
    firstName = firstName.capitalize()
    print(firstName)
    subject = "Fulltime Opportunity"
    body = "Hello "+firstName+",\n\nIt is with great professional enthusiasm that I approach you with a goal of exploring Entry-level Full-time opportunities. I’m Karthik Shekarappa, pursuing master studies in California State University Sacramento. I presently work with Intel Corporation, Folsom in a physical design team focusing on Design Automation, supporting, improving efficiency of Physical designers. This internship has helped me grow exponentially in terms of both technical and personality development.\nI'm seeking full time opportunity in the field of Analog/Digital Logic design, Design Verification / Validation, Physical design or Computer Architecture. I'm well-prepared to align my skill set with any position that requires a proactive individual who strives to exceed expectations on every assignment.\nPlease find the attached resume for your reference.\nHere is a summary of my profile:\n\
    \t1. In-depth understanding of CMOS digital, analog, and I/O circuit design. Knowledge in transistor level circuit simulation tools as PSpice.\n\
    \t2. Skilled in defining functionality and RTL design abstracts.\n\
    \t3. Good understanding and knowledge about ASIC design flow\n\
    \t4. Related Coursework in Micro Computer System Design and Advance Computer Architecture.\n\
    \t5. Significant knowledge in Static Timing Analysis and scripting languages.\n\
    \t6. Familiarity with Synopsys RTL synthesis tools.\n\
    \t7. Good understanding in industry standard design environment.\n\
    \t8. Knowledge of DRC, LVS, and post-layout extraction tools.\n\
    \t9. Strong Practical Experience in using EDA tools such as Cadence Virtuoso\n\
    \t10. Proficient in Mixed Signal IC Design, ASIC / SOC RTL Design and Verification, Physical Design flow and Timing Signoff.\n\
    \t11. Superior written and oral communication skills.\nKindly let me know if you find any match for positions in your knowledge.\nThank you for your time and consideration. Looking forward to hearing from you soon.\n\
    \n\n\nThank you,\nKarthik\
    "
    sender_email = "YOUR GMAIL ID"
    receiver_email = senderEmail
    password = "YOUR GMAIL PASSWORD"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "resume.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    print('Mail sent to ',senderEmail)


mailingList = ['anything@xyz.com']
for mailId in mailingList:
    sendMail(mailId)