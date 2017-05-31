# L1TNtuples

In order to run some ntuples you can look at the test directory

```bash
cd test
vi file_list.txt # edit your file list. should be from eos
python launch_l1ntuple_production_on_lxbatch.py
```

You can use bjobs to monitor the status of your jobs.
The files will appear first in the directory where you launched them with and then they will be automatically moved to l1trigger common space under /eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2017/Stage2/NanoDST/<your-user-name>/.

You can change the STOREPATH in the bash script https://github.com/cms-l1-dpg/L1TNtuples/blob/master/test/bjob_launch.sh#L47



