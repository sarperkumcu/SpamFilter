import os
import random
class DataLoader:
    def init_lists(self,folder):
        a_list = []
        file_list = os.listdir(folder)
        for a_file in file_list:
            with open(folder + a_file, 'rb') as f:
                a_list.append(f.read())
        f.close()
        return a_list

    def getMails(self):
        spam_emails = [(email,'spam') for email in DataLoader.init_lists(self,"/home/sarper/Desktop/arabamcom/data/enron1/spam/")]
        ham_emails = [(email,'ham') for email in DataLoader.init_lists(self,"/home/sarper/Desktop/arabamcom/data/enron1/ham/")]
        all_emails = spam_emails + ham_emails
        random.shuffle(all_emails)
        return spam_emails,ham_emails,all_emails

