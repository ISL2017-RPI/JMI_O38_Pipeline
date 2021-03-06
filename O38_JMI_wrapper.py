import sys
import JMI_O38
import numpy as np

def JMI(data_file = 'trainData.csv', target_file = 'trainTargets.csv', hm_feat = 12):
    my_JMI = JMI_O38.initialize()
    feat = my_JMI.JMI_primitive_O38(data_file, target_file, hm_feat)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    hm_feat = 12
    selected_feature = np.array(JMI(data, target, hm_feat), dtype=np.int16)
    np.savetxt('Features_O38_JMI.csv', selected_feature, delimiter=',')
    print selected_feature
