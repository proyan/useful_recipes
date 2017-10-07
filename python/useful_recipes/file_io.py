def writeJointStateToFile(q_t, filename, DELIMITOR = " "):

    """Write joint state to file. Default delimitor is space

    input: (numpy matrix) q_t, (string) filename, (string) DELIMITOR=" "
    ouput: void
    """
    # q_t is the time sequence of Joint states of the shape (robot.nq, number_of_time_steps)
    n_time_steps = q_t.shape[1]
    robot_nq = q_t.shape[0]
    file_q = open(filename,"w")
    NEWLINE = "\n"
    for k in xrange(n_time_steps):
        line = ""
        for n in xrange(robot_nq):
            if n == robot_nq-1:
                line += str(q_t[n,k]) + NEWLINE
            else:
                line += str(q_t[n,k]) + DELIMITOR
        file_q.write(line)
    file_q.close()

def writeXYZasCSVFile(filename, x,y,z=None, DELIMITOR = ", "):
    """
    Write x, y, z arrays as CSV file. Default Delimitor is comma

    input: (string) filename, (numpy array) x, (numpy array) y, (numpy array) z = None,
           (string) DELIMITOR = ", "
    output: void


    """
    NEWLINE = "\n"
    file_xyz = open(filename, "w")
    if z is None:
        tup_list = zip(x,y)
    else:
        tup_list = zip(x,y,z)
    for tup in tup_list:
        line = ""
        for ind,val in enumerate(tup):
            if ind == len(tup)-1:
                line+= str(val)+NEWLINE
            else:
                line+=str(val)+DELIMITOR
        file_xyz.write(line)
    file_xyz.close()

def writeArraysAsCSVFile(filename, ar_list, DELIMITOR = ", "):
    """
    Write list of arrays as CSV file. Default Delimitor is comma

    input: (string) filename, (numpy array) x, (numpy array) y, (numpy array) z,
           (string) DELIMITOR = ", "
    output: void


    """
    NEWLINE = "\n"
    file_xyz = open(filename, "w")
    tup_list = zip(*ar_list)
    for tup in tup_list:
        line = ""
        for ind,val in enumerate(tup):
            if ind == len(tup)-1:
                line+= str(val)+NEWLINE
            else:
                line+=str(val)+DELIMITOR
        file_xyz.write(line)
    file_xyz.close()

def parseJointStatesFromFile(filename):
    """Inputs a file and ouputs a matrix.
    input: (string) filename
    output: (numpy array) seq
    """
    import pandas as pd
    import numpy as np
    seq = np.array(pd.read_csv(filename,header=None, delim_whitespace=True)).T
    return seq

def writeZippedListToFile(to_write, filename, DELIMITOR = " "):

  """Write List to file. Default delimitor is space                                                   
  """
  file_q = open(filename,"w")
  NEWLINE = "\n"
  for input_line in to_write:
    output_line = ""
    n = len(input_line)
    for i in xrange(n):
      if i == n-1:
        output_line += str(input_line[i]) + NEWLINE
      else:
        output_line += str(input_line[i]) + DELIMITOR
    file_q.write(output_line)
  file_q.close()
