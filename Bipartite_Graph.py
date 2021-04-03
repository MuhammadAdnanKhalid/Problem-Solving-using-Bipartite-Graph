import pandas as pd

# Python program to find
# maximal Bipartite matching.

class GFG:
    def __init__(self, graph):

        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

        # A DFS based recursive function

    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:

                # Mark v as visited
                seen[v] = True

                '''If job 'v' is not assigned to 
                   an applicant OR previously assigned  
                   applicant for job v (which is matchR[v])  
                   has an alternate job available.  
                   Since v is marked as visited in the  
                   above line, matchR[v]  in the following 
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False
        

    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs
        
        unassigned_applicants = []

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):

            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
            else:
                unassigned_applicants.append('Applicant number: {} not assigned any job'.format(i+1))
        print('\n------')
        print('Result')
        print('------')
        print('\n=>Maximum number of applicants that can get a job is: {}'.format(result))
        print()
        print('-----------')
        print('Final State')
        print('-----------')
        print('\n=>Jobs Assigned\n')
        
        # print assigned jobs data
        jobs_assigned = []
        counter = 1 
        for i in matchR:
            if i is not -1:
                jobs_assigned.append([counter,i+1])
            else:
                jobs_assigned.append([counter, 'not assigned!'])
            counter += 1
        df = pd.DataFrame(jobs_assigned, columns=['Job','Assigned To Applicant'])
        print(df.to_string(index=False))
        
        # print unassigned applicants data
        print('\n=>Unassigned Applicants\n')
        for i in unassigned_applicants:
            print(i)

# try:
number_of_applicants = int(input('Enter number of applicants: '))
number_of_jobs = int(input('Enter number of jobs available: '))

if number_of_applicants > 0 and number_of_jobs > 0:
    graphArray = []
    graphInitial = []

    print('\n=>Please enter 1 if interested in job else enter 0')
    for i in range(number_of_applicants):
        temp = []
        jobs_interested = ''
        print()
        print('-------------------------------------')
        print('Enter details for applicant number: {}'.format(i+1))
        print('-------------------------------------')
        for j in range(number_of_jobs):
            print('Applicant Number: {} | Job Number: {}'.format(i+1,j+1))
            while True:
                var = input('Interested?: ')
                if var == '0' or var == '1':
                    temp.append(int(var))
                    if var == '1':
                        jobs_interested += ' {}'.format(j+1)
                    break
        graphArray.append(temp)
        if len(jobs_interested) < 1:
            jobs_interested = None
        graphInitial.append([i+1,jobs_interested])

    # print initial graph (adjacent matrix)
    df = pd.DataFrame(graphInitial, columns=['Applicant','Interested In Jobs'])
    print()
    print('-------------')
    print('Initial State')
    print('-------------')
    print(df.to_string(index=False))

    g = GFG(graphArray)

    # print final state
    g.maxBPM()
else:
    print('Please enter value greater than 0 for number of jobs and number of applicants')