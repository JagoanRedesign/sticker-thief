class Strings:
    START_MESSAGE = ("Halo,\n"
                     "Anda dapat menggunakan saya untuk membuat paket stiker khusus menggunakan stiker yang ada atau file PNG.\n"
                     "\n"
                     "Perintah utama:\n"
                     "/create untuk membuat paket baru\n"
                     "/add untuk menambahkan stiker ke paket yang sudah ada\n"
                     "/help untuk perintah lainnya\n")

    HELP_MESSAGE = ("<b>Daftar perintah lengkap</b>:\n"
                    "- /create: buat paket baru (paket animasi didukung)\n"
                    "- /add: tambahkan stiker ke paket\n"
                    "- /remove: hapus stiker dari paket\n"
                    "- kirimkan saya stiker dan saya akan mengirimkan png-nya kembali\n"
                    "- /list: daftar paket Anda (maks 100 entri)\n"
                    "- /export: ekspor paket stiker sebagai zip file png\n"
                    "- /forgetme: hapus diri Anda dari basis data saya. Paket yang Anda buat <b>tidak</b> akan dihapus dari Telegram\n"
                    "- /readd <code>paket link</code>: menyimpan paket yang dibuat melalui bot, tetapi karena beberapa alasan tidak muncul dalam daftar Anda\n"
                    "- /cleanup: hapus dari daftar paket Anda semua paket yang telah Anda hapus menggunakan @stickers\n"
                    "- /tofile: konversi stiker dan emoji khusus ke file\n"
                    "- /toemoji: mengubah ukuran stiker statis sehingga dapat ditambahkan ke paket emoji khusus\n"
                    "\n"
                    "<b>Operasi lainnya</b>\n"
                    "Anda dapat menghapus paket, mengubah emoji stiker, mengubah urutan stiker, dan melihat statistik stiker / paket dari @stickers\n"
                    "\n"
                    "<b>Tips</b>:\n"
                    "- Saat menambahkan stiker, Anda dapat mengatur emojinya dengan mengirimkannya sebelum mengirim stiker\n"
                    "- Saat menambahkan stiker atau membuat paket, Anda dapat meneruskan stiker atau file PNG\n"
                    "- Saat menambahkan stiker sebagai PNG, Anda dapat meneruskan emojinya di keterangan\n"
                    "- /tofile mendukung emoji bendera <code>-png</code>: itu akan membuat bot mengirim stiker statis/emojis "
                    "sebagai png alih-alih webp\n"
                    "- /toemoji mendukung bendera berikut: <code>-c</code> (akan memotong ruang transparan "
                    "pada batas gambar) dan <code>-r</code> (tidak akan mempertahankan rasio aspek gambar jika "
                    "itu tidak persegi)\n"
                    "\n"
                    "<b>Info lainnya</b>\n"
                    "Semua paket yang Anda buat dengan saya memiliki tautan yang diakhiri oleh \"_by_{}\". Ini tidak dibuat dengan sengaja, "
                    "tapi sesuatu yang dipaksakan oleh Telegram\n"
                    "\n"
                    "<b>Cara yang benar untuk membangun paket kustom Anda sendiri</b>\n"
                    "Gunakan @MyPackBot. Itu tidak mencuri stiker seperti saya. Ini juga sangat cepat. Benar-benar disarankan")

    PACK_CREATION_WAITING_TITLE = ("Baiklah, paket stiker baru! Pilih jenis paket dengan tombol di bawah ini "
                                   "dan <b>kirimkan saya judul paket</b> (tidak boleh melebihi 64 karakter).\n\n"
                                   "Gunakan /cancel untuk membatalkan")

    PACK_CREATION_ANIMATED_WAITING_TITLE = ("Baiklah, paket animasi baru! Tolong kirimkan saya judul paket "
                                            "(tidak boleh melebihi 64 karakter).\n"
                                            "Gunakan /cancel untuk membatalkan")

    PACK_TITLE_TOO_LONG = "Maaf, judulnya harus max 64 karakter. Coba dengan judul lain"

    PACK_TITLE_CONTAINS_NEWLINES = "Maaf, judulnya harus satu baris (tidak ada karakter baris baru)"

    PACK_TITLE_INVALID_MESSAGE = ("Oh tidak! Ini bukan yang saya tunggu! Tolong kirimkan saya "
                                  "judul paket, atau /cancel")

    PACK_CREATION_WAITING_NAME = ("Bagus, ini akan menjadi judul paket: <i>{}</i>\n"
                                  "\n"
                                  "Tolong kirimkan saya apa yang akan menjadi tautan paket (harus maksimal {} karakter. "
                                  "<b>Tidak</b> perlu menyertakan <code>https://t.me/addstickers/</code>)")

    PACK_NAME_TOO_LONG = "Maaf, tautan ini terlalu panjang ({}/{}). Coba lagi dengan tautan lain"

    PACK_NAME_INVALID = ("<b>Tautan tidak valid</b>. Tautan harus:\n"
                         "â€¢ mulailah dengan huruf\n"
                         "â€¢ terdiri secara eksklusif dari huruf, angka atau garis bawah\n"
                         "â€¢ tidak berisi dua garis bawah berturut-turut\n"
                         "â€¢ tidak diakhiri dengan garis bawah\n"
                         "\n"
                         "Silakan coba lagi")

    PACK_NAME_INVALID_MESSAGE = ("Oh tidak! Ini bukan yang saya tunggu! Tolong kirimkan saya "
                                 "tautan paket, atau /cancel")

    PACK_NAME_DUPLICATE = "Maaf, Anda sudah memiliki paket dengan tautan ini disimpan. coba dengan tautan lain"

    PACK_TYPE_BUTTONS_EXPIRED = "Tombol-tombol ini tidak lagi valid"

    PACK_TYPE_CHANGED = "Jenis paket: {}. Sekarang kirimkan saya judul paket!"

    PACK_CREATION_WAITING_FIRST_STATIC_STICKER = ("Mengerti, kita hampir selesai. Sekarang kirimkan saya stiker pertama "
                                                  "paket (atau file png, atau emoji yang digunakan untuk stiker)")

    PACK_CREATION_WAITING_FIRST_ANIMATED_STICKER = ("Mengerti, kita hampir selesai. Sekarang kirimkan saya animasi pertama "
                                                    "stiker paket (atau emoji yang digunakan untuk stiker)")

    PACK_CREATION_WAITING_FIRST_VIDEO_STICKER = ("Mengerti, kita hampir selesai. Sekarang kirimkan saya video pertama "
                                                    "stiker paket (atau emoji yang digunakan untuk stiker)")

    PACK_CREATION_FIRST_STICKER_PACK_DATA_MISSING = ("Ooops, ada yang tidak beres.\n"
                                                     "Silakan ulangi proses pembuatan dengan /create")

    PACK_CREATION_WAITING_FIRST_STICKER_INVALID_MESSAGE = ("Umm ðŸ¤” saya sedang menunggu stiker pertama dari paket. "
                                                           "Tolong kirimkan saya stiker, atau /cancel")

    PACK_CREATION_ERROR_DUPLICATE_NAME = ("Maaf, sudah ada paket dengan <a href=\"{}\">tautan ini</a>.\n"
                                          "Please send me a new link, or /cancel")

    PACK_CREATION_ERROR_INVALID_NAME = ("Maaf, Telegram menolak tautan yang Anda berikan dengan mengatakan itu tidak valid.\n"
                                        "Silakan kirim tautan baru kepada saya, atau /cancel")

    PACK_CREATION_ERROR_GENERIC = ("Kesalahan saat mencoba membuat paket: <code>{}</code>.\n"
                                   "Silakan coba lagi, atau /cancel")

    PACK_CREATION_PACK_CREATED = ("Paket Anda telah dibuat, tambahkan melalui <a href=\"{}\">tautan ini</a>\n"
                                  "Terus kirimi saya stiker untuk menambahkan lebih banyak, atau /done")

    ADD_STICKER_SELECT_PACK = "Pilih paket yang ingin Anda tambahkan stiker, atau /cancel"

    ADD_STICKER_NO_PACKS = "Anda belum memiliki paket apa pun. Pakai /create untuk mulai membuat paket baru"

    ADD_STICKER_SELECTED_TITLE_DOESNT_EXIST = ("Sepertinya paketnya \"{}\" tidak ada.\n"
                                               "Silakan pilih paket yang valid dari keyboard")

    ADD_STICKER_SELECTED_TITLE_MULTIPLE = ("Sepertinya Anda memiliki banyak paket yang cocok dengan judulnya \"{}\".\n"
                                           "Silakan pilih paket yang ingin Anda pilih dari keyboard di bawah ini. Referensi paket:\n"
                                           "â€¢ {}")

    ADD_STICKER_PACK_SELECTED_STATIC = ("Bagus, kita akan menambahkan stiker ke <a href=\"{}\">Paket ini</a>.\n"
                                        "Kirimi saya stiker atau file png, atau /cancel")

    ADD_STICKER_PACK_SELECTED_ANIMATED = ("Bagus, kita akan menambahkan stiker ke <a href=\"{}\">Paket ini</a>.\n"
                                          "Kirimi saya stiker animasi, atau /cancel")

    ADD_STICKER_PACK_SELECTED_VIDEO = ("Bagus, kita akan menambahkan stiker ke <a href=\"{}\">Paket ini</a>.\n"
                                          "Kirimi saya stiker video atau file webp, atau /cancel")

    ADD_STICKER_SELECTED_NAME_DOESNT_EXIST = ("Sepertinya paketnya \"{}\" tidak ada.\n"
                                              "Silakan pilih paket yang valid dari keyboard")

    ADD_STICKER_PACK_DATA_MISSING = ("Ooops, ada yang tidak beres.\n"
                                     "Silakan ulangi prosesnya dengan /add")

    ADD_STICKER_PACK_NOT_VALID = ("Ups, sepertinya <a href=\"{}\">paket ini</a> tidak ada.\n"
                                  "Silakan pilih paket lain")

    ADD_STICKER_PACK_NOT_VALID_NO_PACKS = ("Ups, sepertinya <a href=\"{}\">paket ini</a> tidak ada.\n"
                                           "Silakan buat paket baru dengan /create")

    ADD_STICKER_NO_EMOJI_IN_TEXT = ("Uhm, saya tidak mengerti. Kirimi saya stiker, atau kirimkan saya daftar emoji ke "
                                    "Gunakan untuk stiker berikutnya (atau /done untuk keluar)")

    ADD_STICKER_TOO_MANY_EMOJIS = "Wah, itu banyak emoji! Saya hanya dapat menggunakan maksimal 10, silakan coba lagi"

    ADD_STICKER_EMOJIS_SAVED = "Oh, beberapa emoji! Kami akan menggunakan emoji {} ini untuk stiker berikutnya yang akan Anda kirimkan kepada saya: {}"

    ADD_STICKER_SUCCESS = ("Stiker ditambahkan ke <a href=\"{}\">paket ini</a>. "
                           "Terus kirimi saya stiker untuk menambahkan lebih banyak, gunakan /done setelah selesai")

    ADD_STICKER_SUCCESS_EMOJIS = (" <a href=\"{}\">paket ini</a> menggunakan emoji ini: {}\n"
                                  "Terus kirimi saya stiker untuk menambahkan lebih banyak, gunakan /done setelah selesai")

    ADD_STICKER_PACK_FULL = ("Maaf, <a href=\"{}\">paket ini</a> penuh ({} stiker), "
                             "Anda tidak dapat lagi menambahkan stiker ke dalamnya. Gunakan /remove untuk menghapus beberapa stiker\n"
                             "Anda telah keluar dari mode \"menambahkan stiker\"")

    ADD_STICKER_SIZE_ERROR = ("WhUps, sepertinya terjadi kesalahan saat mengubah ukuran stiker. "
                              "Saya tidak dapat menambahkan stiker ini ke paket karena logika pengubahan ukuran yang salah.\n"
                              "Kirim saya stiker lain, atau gunakan /done setelah selesai")

    ADD_STICKER_INVALID_ANIMATED = ("Sepertinya stiker ini tidak sesuai dengan loger terbaru "
                                    "<a href=\"https://core.telegram.org/animated_stickers\">Pedoman Telegram</a> "
                                    "tentang stiker animasi. Maaf tapi saya tidak bisa menambahkannya :(\n"
                                    "Anda dapat mencoba mengirim stiker lagi atau "
                                    "mengirim stiker animasi lain (atau /cancel)")

    ADD_STICKER_FLOOD_EXCEPTION = ("Uh-oh, it looks like I'm quite busy right now. I cannot create the pack, or "
                                   "Anda telah membuat terlalu banyak paket akhir-akhir ini. "
                                   "Silakan coba lagi dalam: {} jam")

    ADD_STICKER_GENERIC_ERROR = ("Terjadi kesalahan saat menambahkan stiker ini ke <a href=\"{}\">paket ini</a>: "
                                 "<code>{}</code>.\n"
                                 "Coba lagi, kirimi saya stiker lain atau gunakan /done setelah selesai")

    ADD_STICKER_ANIMATED_UNSUPPORTED = ("Maaf, saya belum mendukung stiker animasi :(\n"
                                        "Silakan kirim stiker statis")

    ADD_STICKER_EXPECTING_DIFFERENT_TYPE = ("Uh-oh. Saya sedang menunggu stiker {}, bukan stiker {}. "
                                            "Tolong kirimkan saya stiker baru, atau /cancel")

    ADD_STICKER_INVALID_MESSAGE = "Uhmm ðŸ¤” Saya sedang menunggu stiker untuk ditambahkan. Kirimi saya stiker, atau /cancel"

    REMOVE_STICKER_SELECT_STICKER = "Kirimi saya stiker yang ingin Anda hapus dari paketnya, atau /cancel"

    REMOVE_INVALID_MESSAGE = "Silakan kirim stiker yang ingin Anda hapus dari kemasannya, atau /cancel"

    REMOVE_STICKER_SUCCESS = ("Stiker dihapus dari <a href=\"{}\">paket ini</a>.\n"
                              "Kirimi saya stiker lain untuk dihapus, atau /done setelah selesai")

    REMOVE_STICKER_FOREIGN_PACK = ("Stiker ini berasal dari <a href=\"{}\">paket</a> anda tidak berkreasi melalui saya. "
                                   "Coba dengan stiker yang valid, atau /done")

    REMOVE_STICKER_ALREADY_DELETED = ("Stiker ini tidak lagi menjadi bagian dari <a href=\"{}\">paket ini</a>, "
                                      "coba dengan stiker lain, atau /done")

    REMOVE_STICKER_GENERIC_ERROR = (
        "Terjadi kesalahan saat menghapus stiker ini dari <a href=\"{}\">paket ini</a>: "
        "<code>{}</code>.\n"
        "Coba lagi, kirimi saya stiker lain atau gunakan /selesai setelah selesai")

    READD_WAITING_STICKER = "Tolong kirimkan saya stiker dari paket Anda " \
                                         "ingin menyimpan di antara paket yang saya kelola.\n" \
                                         "Harap diingat bahwa paket itu pasti dibuat oleh saya. " \
                                         "Gunakan /cancel untuk membatalkan"

    READD_STICKER_NO_PACK = "Stiker ini bukan milik paket. Silakan coba dengan paket lain, atau /cancel"

    READD_STICKER_ANIMATED = "Ini hanya berfungsi dengan paket stiker statis (non-animasi). Silakan coba dengan paket lain, atau /cancel"

    READD_UNEXPECTED_MESSAGE = "Uuh, saya tidak mengerti apa yang Anda coba katakan.\n" \
                               "Tolong kirimkan saya nama paket / tautan paket untuk ditambahkan (atau kirimkan saya stiker dari paket), atau /cancel"

    READD_WRONG_PACK_NAME = "Maaf, sepertinya <a href=\"{}\">paket ini </a>nama tidak diakhiri dengan \"<code>{}</code>\", " \
                            "oleh karena itu saya tidak memilikinya: Anda hanya dapat menambahkan paket yang saya buat. Coba dengan paket lain, atau /cancel"

    READD_INVALID_PACK_NAME_PATTERN = "Maaf, sepertinya nama ini bukan nama paket yang valid. " \
                                      "Nama paket stiker adalah yang muncul setelah tautan bagikannya " \
                                      "(<code>https://t.me/addstickers/</code> link).\n\n" \
                                      "Coba lagi dengan nama/link lain, atau kirimkan saya stiker dari paket, " \
                                      "or /cancel"

    READD_PACK_EXISTS = "Sepertinya <a href=\"{}\">paket ini</a> sudah disimpan dalam paket Anda. " \
                            "Coba dengan paket lain, atau /cancel"

    READD_PACK_INVALID = "Maaf, sepertinya Anda tidak membuat <a href=\"{}\">paket ini</a> dengan saya " \
                                  "(atau tidak ada). " \
                                  "Anda hanya dapat menambahkan paket yang saya buat.\n\n" \
                                  "Coba dengan paket lain, atau /cancel"

    READD_UNKNOWN_API_EXCEPTION = "Maaf, sepertinya Anda tidak membuat <a href=\"{}\">paket ini</a> dengan saya, " \
                                  "atau tidak ada (kesalahan: <code>{}</code>). " \
                                  "Anda hanya dapat menambahkan paket yang saya buat.\n\n" \
                                  "Coba dengan paket lain, atau /cancel"

    READD_SAVED = "{} berhasil disimpan ke paket Anda!"

    READD_DUMMY_STICKER_NOT_REMOVED = "Bagaimanapun, untuk memeriksa apakah saya memiliki paket ini atau tidak, " \
                                      "Saya harus menambahkan stiker tiruan ke dalam paket, yang belum dapat saya hapus. " \
                                      "Anda dapat menghapusnya secara manual menggunakan perintah /remove"

    READD_DUMMY_STICKER_NOT_REMOVED_UNKNOWN = "Bagaimanapun, untuk memeriksa apakah saya memiliki paket ini atau tidak, " \
                                              "Saya harus menambahkan stiker tiruan ke dalam paket, " \
                                              "yang belum bisa saya hapus (<code>{}</code>). " \
                                              "Anda dapat menghapusnya secara manual menggunakan perintah /remove"

    FORGETME_SUCCESS = "Sukses, saya telah menghapus semua paket Anda dari database saya"

    CANCEL = "Bagus, kita sudah selesai dengan itu"

    CANCEL_NO_CONVERSATION = "Tidak ada operasi yang terjadi ðŸ˜´"

    TIMEOUT = "ðŸ˜´ Sepertinya Anda tidak aktif, saya telah membatalkan operasi saat ini"

    LIST_NO_PACKS = "Anda tidak memiliki paket apa pun. Gunakan /create untuk membuatnya"

    LIST_FOOTER = "\n\n<b>s</b>: statis\n<b>a</b>: animasi\n<b>v</b>: video"

    ANIMATED_STICKERS_NO_FILE = "Sayangnya saya tidak dapat mengirimi Anda stiker animasi kembali sebagai file :("

    EXPORT_PACK_SELECT = "Tolong kirimkan saya stiker dari paket yang ingin Anda ekspor, atau /cancel"

    EXPORT_PACK_NO_PACK = "Stiker ini bukan milik paket apa pun. Tolong kirimkan saya stciker dari paket, atau /cancel"

    EXPORT_PACK_START = "Mengekspor stiker dari <i>{}</i>... mungkin perlu beberapa menit. Harap tunggu"

    EXPORT_PACK_UPLOADING = "Zip file png dan upload..."

    EXPORT_ANIMATED_STICKERS_NOT_SUPPORTED = "Mengekspor paket animasi belum didukung"

    EXPORT_SKIPPED_STICKERS = " - Saya tidak bisa mengekspor {} stiker!"

    EXPORT_ONGOING = "Tunggu, ekspor sedang diproses..."

    CLEANUP_NO_PACK = ("Sepertinya semua paket Anda masih ada. Tidak ada paket yang dihapus dari database.\n"
                       "Jika Anda baru saja menghapus paket dari @stickers, ingatlah bahwa mungkin perlu waktu untuk bot "
                       "untuk diberitahu tentang penghapusannya.\n\n"
                       "Anda dapat menggunakan /list untuk melihat daftar paket Anda")

    CLEANUP_HEADER = "Ini adalah paket yang tidak ada lagi dan telah dihapus dari database:\n"

    CLEANUP_WAIT = "Tunggu, operasi ini mungkin memakan waktu..."

    TO_FILE_MIME_TYPE = "mime-type: {}"

    TO_EMOJI_WAITING_STICKER = "Kirimi saya stiker statis, " \
                               "Saya akan mengirimkan kembali file yang dapat Anda gunakan sebagai emoji khusus"

    TO_EMOJI_UNEXPECTED_MESSAGE = "Tolong kirimkan saya stiker <b>statis</b>, atau /cancel"

    TO_EMOJI_NON_STATIC_STICKER = "Stiker animasi dan video tidak perlu diubah ukurannya, Anda dapat menggunakan " \
                                  "<code>/tofile</code> untuk mengonversi stiker animasi/static menjadi " \
                                  "File emoji-siap cutom. Gunakan /done setelah selesai dengan perintah ini"

    EMOJI_TO_FILE_VIDEO_NOT_SUPPORTED = "Stiker video tidak didukung ðŸ˜”"

    EMOJI_TO_FILE_TOO_MANY_ENTITIES = "Silakan kirim hanya satu emoji khusus"

    TO_FILE_WAITING_STICKER = "Silakan kirim stiker (statis / video) atau emoji khusus yang ingin Anda konversi " \
                              "file, atau /cancel"

    TO_FILE_UNEXPECTED_MESSAGE = "Saya tidak mengharapkan itu ðŸ¤” silakan kirim stiker atau emoji khusus, atau gunakan /cancel"

    ENABLED_FLAGS = "Bendera yang diaktifkan: "
