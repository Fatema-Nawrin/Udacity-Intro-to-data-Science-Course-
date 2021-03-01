
import pandas
import pandasql

def select_first_50():
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    aadhaar_data = pandas.read_csv('aadhaar_data.csv')
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax. 
    #
    # Note that "enrolment_agency" is spelled with one l. Also, the order
    # of the select does matter. Make sure you select registrar then enrolment agency
    # in your query.
    #
    # You can download a copy of the aadhaar data that we are passing 
    # into this exercise below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/aadhaar_data.csv
    q = """
    SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50;
    """

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

def aggregate_query():
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    
    aadhaar_data = pandas.read_csv('aadhaar_data.csv')
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Write a query that will select from the aadhaar_data table how many men and how 
    # many women over the age of 50 have had aadhaar generated for them in each district.
    # aadhaar_generated is a column in the Aadhaar Data that denotes the number who have had
    # aadhaar generated in each row of the table.
    #
    # Note that in this quiz, the SQL query keywords are case sensitive. 
    # For example, if you want to do a sum make sure you type 'sum' rather than 'SUM'.
        
    q = "SELECT Gender, District, sum(Aadhaar_generated) FROM aadhaar_data WHERE Age>50 GROUP BY Gender, District;"

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution


if __name__ == '__main__':
    print(select_first_50())
    print(aggregate_query())



