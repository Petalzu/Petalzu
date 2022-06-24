package teamwork;

import javafx.beans.value.ObservableValueBase;
import javafx.fxml.Initializable;
import javafx.scene.control.ChoiceDialog;
import javafx.scene.control.ContextMenu;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.SeparatorMenuItem;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.scene.text.Text;
import top.kkoishi.proc.json.JsonParser;
import top.kkoishi.proc.json.JsonSyntaxException;
import top.kkoishi.proc.json.MappedJsonObject;
import top.kkoishi.proc.property.BuildFailedException;
import top.kkoishi.teamwork.MainApplication;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.net.URL;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.ResourceBundle;
import java.util.concurrent.atomic.AtomicBoolean;

/**
 * @author DELL
 */
public final class Control implements Initializable {
    public TextField textField;
    public Menu file;
    public MenuItem newItem;
    public MenuItem open;
    public Menu openRec;
    public MenuItem close;
    public MenuItem save;
    public MenuItem saveAs;
    public MenuItem revert;
    public TreeView<String> structure;
    public TreeItem<String> root;
    public TableColumn<Utils.HistoryData, String> history;
    public TableColumn<Utils.HistoryData, Path> location;
    public TableView<Utils.HistoryData> useTable;
    public ScrollPane workspace;
    public Text searchConfirm;
    private Path path = MainApplication.path;

    static final Runtime R = Runtime.getRuntime();
    static JsonParser D;
    static MappedJsonObject M;
    static Utils.CompType type;
    static AtomicBoolean useAccuracy = new AtomicBoolean(true);
    static final Path ROOT_DIR = null;
    static final String[] OPTIONS = {"Name Only", "Content Include", "Text Match"};

    static {
        // init static field.
        try {
            // parse json and load class fields.
            D = new JsonParser(Files.readString(Path.of("./data/data.json")));
            D.parse();
            M = MappedJsonObject.cast(D.result(), HashMap.class);
            // lookup type and if use accuracy size.
            type = Utils.CompType.valueOf(M.getString("look_up"));
            useAccuracy.set(M.getBool("use_acc"));
        } catch (IOException | BuildFailedException | JsonSyntaxException | InvocationTargetException
                | NoSuchMethodException | InstantiationException | IllegalAccessException e) {
            e.printStackTrace();
        }
    }


    public Control () {
    }

    private void searchName (String pattern, Path root) {
        try {
            System.out.println("Search:" + root);
            final ArrayList<Path> result = new ArrayList<>(32);
            Files.walkFileTree(root, new FileVisitor<>() {
                @Override
                public FileVisitResult preVisitDirectory (Path dir, BasicFileAttributes attrs) throws IOException {
                    if (dir.toString().contains(pattern)) {
                        result.add(dir);
                    }
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult visitFile (Path file, BasicFileAttributes attrs) throws IOException {
                    if (file.toString().contains(pattern)) {
                        result.add(file);
                    }
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult visitFileFailed (Path file, IOException exc) throws IOException {
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult postVisitDirectory (Path dir, IOException exc) throws IOException {
                    return FileVisitResult.CONTINUE;
                }
            });
            final Path[] paths = new Path[result.size()];
            for (int i = 0; i < paths.length; i++) {
                paths[i] = result.remove(0);
            }
            final ChoiceDialog<Path> choiceDialog = new ChoiceDialog<>(null, paths);
            choiceDialog.setTitle("Search Result");
            choiceDialog.setContentText("You can choose a result to open it.");
            final var option = choiceDialog.showAndWait();
            if (option.isEmpty()) {
                return;
            }
            if (Files.isDirectory(option.get())) {
                accessDir(option.get());
            } else {
                accessFile(option.get());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void searchExtension (String extension, Path root) {
        try {
            System.out.println("Search:" + root + "<-" + extension);
            final ArrayList<Path> result = new ArrayList<>(32);
            Files.walkFileTree(root, new FileVisitor<>() {
                @Override
                public FileVisitResult preVisitDirectory (Path dir, BasicFileAttributes attrs) throws IOException {
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult visitFile (Path file, BasicFileAttributes attrs) throws IOException {
                    if (file.toString().endsWith(extension)) {
                        result.add(file);
                    }
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult visitFileFailed (Path file, IOException exc) throws IOException {
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult postVisitDirectory (Path dir, IOException exc) throws IOException {
                    return FileVisitResult.CONTINUE;
                }
            });
            final Path[] paths = new Path[result.size()];
            for (int i = 0; i < paths.length; i++) {
                paths[i] = result.remove(0);
            }
            final ChoiceDialog<Path> choiceDialog = new ChoiceDialog<>(null, paths);
            choiceDialog.setTitle("Search Result");
            choiceDialog.setContentText("You can choose a result to open it.");
            final var option = choiceDialog.showAndWait();
            if (option.isEmpty()) {
                return;
            }
            if (Files.isDirectory(option.get())) {
                accessDir(option.get());
            } else {
                accessFile(option.get());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void initialize (URL url, ResourceBundle resourceBundle) {
        searchConfirm.setOnMouseClicked(me -> {
            final ChoiceDialog<String> choiceDialog = new ChoiceDialog<>("Search Types", OPTIONS);
            choiceDialog.setTitle("Choice Search Type");
            choiceDialog.setContentText("");
            final var option = choiceDialog.showAndWait();
            if (option.isEmpty()) {
                return;
            }
            final var item = option.get();
            if ("Name Only".equals(item)) {

            } else if (OPTIONS[1].equals(item)) {
                final var name = textField.getText();
                if (name == null) {
                    return;
                }
                if (name.startsWith("*.")) {
                    searchExtension(name.substring(1), path);
                } else {
                    searchName(name, path);
                }
            } else if ("Text Match".equals(item)) {

            }
        });
        history.setCellValueFactory(df -> new ObservableValueBase<>() {
            @Override
            public String getValue () {
                return df.getValue().name();
            }
        });
        useTable.setOnMouseClicked(me -> {
            if (me.getClickCount() == 2) {
                final var ele = useTable.getSelectionModel().getSelectedItem();
                if (ele != null) {
                    accessFile(ele.location());
                }
            }
        });
        location.setCellValueFactory(df -> new ObservableValueBase<>() {
            @Override
            public Path getValue () {
                return df.getValue().location();
            }
        });
        final MenuItem iconLookup = new MenuItem("Icon Lookup");
        final MenuItem infoLookup = new MenuItem("Information Lookup");
        final MenuItem contentLookup = new MenuItem("Content Lookup");
        final ContextMenu contextMenu = new ContextMenu(
                iconLookup,
                infoLookup,
                contentLookup,
                new SeparatorMenuItem()
        );
        accessDir(path);
        contextMenu.setPrefSize(100, 100);
        workspace.setOnMouseClicked(me -> {
            if (me.isPopupTrigger()) {
                // pop up.
                contextMenu.show(workspace, me.getScreenX(), me.getScreenY());
            }
        });
        root = path == null ? TreeItemImpl.diskRoot : new TreeItemImpl(path);
        root.getChildren();
        structure.setRoot(root);
        structure.setOnMouseClicked(me -> {
            final var count = me.getClickCount();
            if (count == 1) {
                final var selected = structure.getSelectionModel().getSelectedItem();
                if (selected == null) {
                    return;
                }
                ((TreeItemImpl) selected).upgrade();
                selected.setExpanded(!selected.isExpanded());
                System.out.println("Expand:" + selected);
            } else if (count == 2) {
                final var selected = (TreeItemImpl) structure.getSelectionModel().getSelectedItem();
                if (selected == null || selected.path == null) {
                    return;
                }
                if (Files.isDirectory(selected.path)) {
                    accessDir(selected.path);
                } else {
                    accessFile(selected.path);
                }
            }
        });
    }

    public void switchWordspace () {
    }

    public void accessDir (Path path) {
        this.path = path;
        if (path == ROOT_DIR) {
            final var content = Utils.FS.getRootDirectories();
            int count = 0;
            for (final Path value : content) {
                count++;
            }
            final var buffer = new Path[count];
            count = 0;
            for (final Path value : content) {
                buffer[count++] = value;
            }
            try {
                final var pane = new Utils.CellContainer(type, useAccuracy.get(), buffer);
                pane.setAction(this::accessDir);
                workspace.setContent(pane);
            } catch (IOException e) {
                e.printStackTrace();
                // this should not happen.
            }
        } else {
            try {
                final var content = Files.list(path).toArray(Path[]::new);
                final var pane = new Utils.CellContainer(type, useAccuracy.get(), content);
                pane.setAction(this::accessDir);
                workspace.setContent(pane);
            } catch (IOException e) {
                e.printStackTrace();
                // this should not happen.
            }
        }
    }

    public void accessFile (Path path) {
        useTable.getItems().add(new Utils.HistoryData(path.getFileName().toString(), path));
        try {
            R.exec(new String[]{"powershell", "start", "\"" + path.toRealPath() + "\""});
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
