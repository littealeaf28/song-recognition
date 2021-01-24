from glob import glob
import os
import pandas as pd


def clear_nonsamples(label):
    print(f'Processing {label}...')

    mp3_files = glob(f'cv-corpus-6.1-2020-12-11\\{label}\\clips\\*.mp3')
    misc_files = glob(f'cv-corpus-6.1-2020-12-11\\{label}\\*.tsv')

    for mp3_file in mp3_files:
        os.remove(mp3_file)

    for misc_file in misc_files:
        os.remove(misc_file)

    df.loc[df['Label'] == label, 'Finished Sampling'] = True


df = pd.read_csv('data_links.csv')

samp_df = df.loc[df['Sample Size'] > 193]

[clear_nonsamples(label) for label in samp_df['Label'].values]

df.to_csv('data_links.csv', index=False)

# TODO: Generalize to all available ones that haven't yet been deleted

# Delete all the tsv files

# Add appropriate labels to clips to be processed in notebook by pytorch audio
