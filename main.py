def number_of_lines():
    file_path = '/cxldata/datasets/project/mbox-short.txt'
    with open(file_path, 'r') as file:
        inp = file.read()
    lines = inp.split('\n')
    return len(lines) - 1

def count_number_of_lines():
    file_path = '/cxldata/datasets/project/mbox-short.txt'
    with open(file_path, 'r') as file:
        count = sum(1 for line in file if line.startswith('Subject:'))
    return count

def average_spam_confidence():
    file_path = '/cxldata/datasets/project/mbox-short.txt'
    total_confidence = 0.0
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                count += 1
                confidence = float(line.split(':')[1].strip())
                total_confidence += confidence
    return total_confidence / count if count > 0 else 0

def find_email_sent_days():
    file_path = '/cxldata/datasets/project/mbox-short.txt'
    days_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                day = words[2]
                days_count[day] = days_count.get(day, 0) + 1
    return days_count

def count_message_from_email():
    file_path = '/cxldata/datasets/project/mbox-short.txt'
    email_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                email = words[1]
                email_count[email] = email_count.get(email, 0) + 1
    return email_count

def count_message_from_domain():
    file_path = '/cxldata/datasets/project/mbox-short.txt'
    domain_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                email = words[1]
                domain = email.split('@')[1]
                domain_count[domain] = domain_count.get(domain, 0) + 1
    return domain_count

# Main code
if __name__ == "__main__":
    print("Number of lines:", number_of_lines())
    print("Number of lines starting with 'Subject:':", count_number_of_lines())
    print("Average spam confidence:", average_spam_confidence())
    print("Emails sent on each day of the week:", find_email_sent_days())
    print("Number of messages from each email address:", count_message_from_email())
    print("Number of messages from each domain:", count_message_from_domain())
