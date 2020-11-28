"""Useful data cleaning functions

    na_cols : Return columns that only contain NAs.
    one_val_cols : Return columns that only contain one value.

"""

import numpy as np

def na_cols(df, na_vals=None, inplace=False, drop=False):
    """Return all columns from a data frame that only contain NA values.
    
    Parameters
    ----------
    na_strings : list
        Additional values to convert to NA.
        
    inplace : bool
        Whether to overwrite the values inside na_strings in the original dataframe
        (True) or leave the original values (False). 
        
    drop : bool
        Whether to drop the columns from the original dataframe.
        
    Returns
    -------
    list of columns if drop=False, nothing if drop=True

    """
    
    # Check inputs
    NoneType = type(None)
    if not isinstance(na_vals, (list, NoneType)):
        raise TypeError('na_strings must be None or a list of values')
        
    if not isinstance(drop, bool):
        raise TypeError('drop must be of type bool (True or False)')
    
    if na_vals != None:
        
        # Check inplace input
        if not isinstance(inplace, bool):
            raise TypeError('inplace must be of type bool (True or False)')
        
        if inplace == True:
            df.replace(na_vals, np.nan, inplace=inplace)
            df_tmp = df
        else:
            df_tmp = df.replace(na_vals, np.nan, inplace=inplace)
            
    else:
        df_tmp = df
        
    # Count non-null values
    
    cols = []
    
    for col in df_tmp:
        if df_tmp[col].notnull().sum() == 0:
            cols.append(col)
            
    if drop == True:
        df.drop(columns=cols, inplace=True)
        print("The following columns contain only NA values and have been dropped: \n",cols)
    else:     
        print("The following columns contain only NA values: ",cols)
        return cols
    
    
def one_val_cols(df, na_remove=False):
    """Return all columns from a data frame that only contain one value.
            
    Returns
    -------
    list of columns
    
    """
    
    cols = []
    vals = []
    
    for col in df:
        if df[col].nunique() == 1:
            cols.append(col)
            vals.append(df[col].value_counts().index[0])  
            
    print("The following columns contain only 1 unique value: \n")
    for i in range(len(cols)): 
        print(cols[i], " : ", vals[i])
    
    return cols
