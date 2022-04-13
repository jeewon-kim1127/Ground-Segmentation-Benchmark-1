import os
import numpy as np

if __name__ == "__main__":

	
    src_dir = "//media/jeewon/Elements/semantic_kitti_raw/"
    tgt_dir = "/media/jeewon/Elements/data/gpf_ground_labels/"
    wrong=0

    for seq_id in range(11):
        sequence = "%02d"%seq_id
        src_seq_dir = src_dir + sequence + "/labels/"
        bin_dir = src_dir+sequence+"/velodyne/"
        tgt_seq_dir = tgt_dir + sequence+"/"
        
        src_files = os.listdir(src_seq_dir)
        bin_files = os.listdir(bin_dir)
        tgt_files = os.listdir(tgt_seq_dir)

        num_src = len(src_files)
        num_bin = len(bin_files)
        num_tgt = len(tgt_files)
        
        if (num_src != num_tgt or num_bin!=num_tgt):
            wrong=1
            print("Something's wrong! Check the Seq. %s"%sequence)
            break
        else:
            for label_id in range(num_tgt):
                label="%06d"%label_id
                src_file_name=label+".label"
                tgt_file_name=label+".csv"
                bin_file_name=label+".bin"
                if ((src_file_name not in src_files) or (tgt_file_name not in tgt_files) or (bin_file_name not in bin_files) ):
                    print("missing label or bin or csv file of label %s"%label)
                    wrong=1
                    break
                bin_file = np.fromfile(bin_dir+bin_file_name)
                tgt_file = np.fromfile(tgt_seq_dir+tgt_file_name)
                if (len(bin_file)/8 != len(tgt_file)):
                    print("total counts of veloyne and label csv are different!")
                    wrong=1
                    break

            if (wrong==1): break
            else: print("Pass! Seq. %s"%sequence)

        if (wrong==1):
            printf("error")
            
        
