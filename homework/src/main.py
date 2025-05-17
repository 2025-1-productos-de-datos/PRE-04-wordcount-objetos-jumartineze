
from homework.src._internals.write_count_words_mixin import WriteWordCountsMixin
from homework.src._internals.split_into_words_mixin import SplitIntoWordsMixin
from homework.src._internals.read_all_lines_mixin import ReadAllLinesMixin
from homework.src._internals.preprocess_lines_mixin import PreprocessLinesMixin
from homework.src._internals.count_words_mixin import CountWordsMixin
from homework.src._internals.parse_args_mixin import ParseArgsMixin


class WordCountApp(
    ParseArgsMixin,
    ReadAllLinesMixin,
    PreprocessLinesMixin,
    SplitIntoWordsMixin,
    CountWordsMixin,
    WriteWordCountsMixin,
):
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.lines = None
        self.preprocessed_lines = None
        self.words = None
        self.word_counts = None

    def run(self):

        self.parse_args()
        self.read_all_lines()
        self.preprocess_lines()
        self.split_into_words()
        self.count_words()
        self.write_word_counts()


if __name__ == "__main__":
    WordCountApp().run()
