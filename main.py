import fasttext
import sys
import ipdb

if __name__ == "__main__":
    """Entry point

    Run two pipeline
        train:
            saves GB sizes model.bin binaries containing models, its weights and word vectors
                (no need to save .vec as contained in .bin)
        predict:
            load model and use to make inferences
    """
    arg = sys.argv[1]

    if arg == "train":

        print("\nSKIPGRAM ======\n")

        # train model
        skipgram_model = fasttext.train_unsupervised("data/ft.train", model="skipgram")

        # save model (.bin)
        skipgram_model.save_model("model/skipgram_model.bin")

        # list of words in dictionary
        print(skipgram_model.words)  # list of words in dictionary
        print("""King's embedding:\n""")  # get the vector of the word 'king'
        print(skipgram_model["life"])  # get the vector of the word 'king'

        print("\nCBOW ======\n")

        # train model
        cbow_model = fasttext.train_unsupervised("data/ft.train", model="cbow")

        # list of words in dictionary
        print(cbow_model.words)  # list of words in dictionary
        print("""\nKing's embedding:\n""")  # get the vector of the word 'king'
        print(cbow_model["life"])  # get the vector of the word 'king'

        # save model (.bin)
        cbow_model.save_model("model/cbow_model.bin")

    elif arg == "predict":

        print("\SKIPGRAM ======\n")
        skipgram_model = fasttext.load_model("model/skipgram_model.bin")
        life_vec = skipgram_model.get_word_vector("life")
        print(life_vec)
        nn = skipgram_model.get_nearest_neighbors("life")
        print(nn)

        print("\nCBOW ======\n")
        cbow_model = fasttext.load_model("model/cbow_model.bin")
        life_vec = cbow_model.get_word_vector("life")
        print("\n", life_vec, "\n")
        nn = cbow_model.get_nearest_neighbors("life")
        print("\n", nn, "\n")
