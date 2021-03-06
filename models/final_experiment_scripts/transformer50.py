from eICU_preprocessing.split_train_test import create_folder
from models.run_transformer import BaselineTransformer
from models.initialise_arguments import initialise_transformer_arguments


if __name__=='__main__':

    c = initialise_transformer_arguments()
    c['mode'] = 'test'
    c['exp_name'] = 'Transformer50'
    c['percentage_data'] = 50
    c['n_epochs'] = 14

    log_folder_path = create_folder('models/experiments/final', c.exp_name)
    transformer = BaselineTransformer(config=c,
                                      n_epochs=c.n_epochs,
                                      name=c.exp_name,
                                      base_dir=log_folder_path,
                                      explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    transformer.run()